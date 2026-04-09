#!/usr/bin/env python3

from __future__ import annotations

import fnmatch
import os
import re
import sys
from pathlib import Path


DEFAULT_MAX_DEPTH = 3
DEFAULT_MAX_PATH_LENGTH = 65
DEFAULT_IGNORE_FILE = ".filenameignore"
CHECKED_EXTENSIONS = {".qmd", ".rmd", ".rmarkdown", ".html"}
DEFAULT_EXCLUDED_DIRS = {".git", ".github", ".quarto", "_site"}
NAME_PATTERN = re.compile(r"^[a-z]+(?:-[a-z]+)*$")


def read_int_env(name: str, default: int) -> int:
    raw = os.getenv(name, str(default)).strip()
    try:
        value = int(raw)
    except ValueError:
        print(f"Error: {name} must be an integer (got: {raw}).")
        raise SystemExit(2)

    if value < 1:
        print(f"Error: {name} must be at least 1.")
        raise SystemExit(2)
    return value


def printable_path(path: Path) -> str:
    return "/" + path.as_posix()


def load_ignore_patterns(root: Path, ignore_file: str) -> list[str]:
    ignore_path = root / ignore_file
    if not ignore_path.exists():
        return []

    patterns: list[str] = []
    for raw_line in ignore_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        patterns.append(line)
    return patterns


def is_ignored(path: Path, patterns: list[str]) -> bool:
    rel = path.as_posix()
    rel_dir = rel + "/"

    for pattern in patterns:
        normalized = pattern.rstrip("/")
        if fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch(rel, normalized):
            return True
        if fnmatch.fnmatch(rel_dir, pattern + "/") or fnmatch.fnmatch(rel_dir, pattern):
            return True
    return False


def has_default_excluded_dir(path: Path) -> bool:
    return any(part in DEFAULT_EXCLUDED_DIRS for part in path.parts)


def is_checked_extension(path: Path) -> bool:
    return path.suffix.lower() in CHECKED_EXTENSIONS


def path_depth(path: Path) -> int:
    return len(path.parts)


def scan_files(root: Path, patterns: list[str], explicit_files: list[str] | None) -> list[Path]:
    found: set[Path] = set()

    if explicit_files is not None and explicit_files:
        candidates = [Path(file_path) for file_path in explicit_files]
    else:
        candidates = [p.relative_to(root) for p in root.rglob("*") if p.is_file()]

    for candidate in candidates:
        rel_path = candidate
        if candidate.is_absolute():
            try:
                rel_path = candidate.relative_to(root)
            except ValueError:
                continue

        if not rel_path.parts:
            continue
        if has_default_excluded_dir(rel_path):
            continue
        if is_ignored(rel_path, patterns):
            continue
        if not is_checked_extension(rel_path):
            continue

        found.add(rel_path)

    return sorted(found)


def segment_is_valid(segment: str) -> bool:
    if not segment:
        return False
    if any(char.isdigit() for char in segment):
        return False
    return bool(NAME_PATTERN.fullmatch(segment))


def validate_name_segments(path: Path) -> list[str]:
    invalid: list[str] = []
    for part in path.parts:
        stem = Path(part).stem
        if not segment_is_valid(stem):
            invalid.append(part)
    return invalid


def main() -> int:
    root = Path(os.getenv("CHECK_ROOT", ".")).resolve()
    max_depth = read_int_env("MAX_DEPTH", DEFAULT_MAX_DEPTH)
    max_path_length = read_int_env("MAX_PATH_LENGTH", DEFAULT_MAX_PATH_LENGTH)
    ignore_file = os.getenv("IGNORE_FILE", DEFAULT_IGNORE_FILE)
    explicit_files = sys.argv[1:] if len(sys.argv) > 1 else None

    ignore_patterns = load_ignore_patterns(root, ignore_file)
    files = scan_files(root, ignore_patterns, explicit_files)

    if not files:
        print("No matching files found. Nothing to validate.")
        return 0

    depth_violations: list[tuple[str, int]] = []
    length_warnings: list[tuple[str, int]] = []
    naming_violations: list[tuple[str, list[str]]] = []

    for rel_path in files:
        display_path = printable_path(rel_path)
        depth = path_depth(rel_path)
        path_length = len(display_path)
        bad_segments = validate_name_segments(rel_path)

        if depth > max_depth:
            depth_violations.append((display_path, depth))
        if path_length > max_path_length:
            length_warnings.append((display_path, path_length))
        if bad_segments:
            naming_violations.append((display_path, bad_segments))

    print(
        "Checked "
        f"{len(files)} file(s) with max depth={max_depth} and "
        f"max path length={max_path_length}."
    )

    if depth_violations:
        print(
            f"\nDepth violations (allowed <= {max_depth} path segments):"
        )
        for path, depth in depth_violations:
            print(f"  - {path} (depth: {depth})")

    if naming_violations:
        print(
            "\nNaming violations (use lowercase kebab-case and avoid digits "
            "for files/folders):"
        )
        for path, bad_segments in naming_violations:
            formatted = ", ".join(bad_segments)
            print(f"  - {path} (invalid segment(s): {formatted})")

    if length_warnings:
        print(
            f"\nLong path warnings (limit <= {max_path_length} characters):"
        )
        for path, length in length_warnings:
            print(f"  - {path} (length: {length})")

    has_failures = bool(depth_violations or naming_violations or length_warnings)
    if not has_failures:
        print("All checks passed.")
        return 0

    print("\nValidation failed. See messages above for fixes.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())