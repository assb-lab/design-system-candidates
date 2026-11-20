#!/usr/bin/env python3
"""Small, stdlib-first figure preflight. NOT a publisher compliance certificate."""
from __future__ import annotations
import argparse
import json
import struct
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROFILE = SCRIPT_DIR.parent / "assets" / "figure-presets.json"


def dimensions(path: Path):
    """Return (width_px, height_px) or None for vector/unknown formats."""
    suffix = path.suffix.lower()
    if suffix == ".png":
        with path.open("rb") as handle:
            head = handle.read(24)
        if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
            raise ValueError("Invalid PNG header")
        return struct.unpack(">II", head[16:24])
    if suffix in (".tif", ".tiff", ".jpg", ".jpeg", ".webp", ".bmp"):
        try:
            from PIL import Image
        except ImportError as exc:
            raise RuntimeError("Install Pillow in the Python environment to inspect this raster format") from exc
        with Image.open(path) as image:
            return image.size
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Check output dimensions, size and effective raster DPI; manual figure checks remain required")
    parser.add_argument("file", type=Path)
    parser.add_argument("--width-mm", type=float, required=True, help="Intended FINAL printed width of the whole submitted file")
    parser.add_argument("--height-mm", type=float, help="Intended FINAL printed height of the whole submitted file")
    parser.add_argument("--kind", choices=("photo", "grayscale", "line"), default="photo")
    parser.add_argument("--column", choices=("single", "double"), help="Validate against the chosen column limit where available")
    args = parser.parse_args()

    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    if args.width_mm <= 0 or (args.height_mm is not None and args.height_mm <= 0):
        parser.error("width-mm and height-mm must be positive")
    if not args.file.is_file():
        parser.error(f"file not found: {args.file}")

    problems = []
    warnings = []
    width = profile["figure_width_mm"]
    bound = width.get(args.column) if args.column else width.get("max")
    if bound and args.width_mm > float(bound) + 0.05:
        problems.append(f"width {args.width_mm:g} mm exceeds the {args.column or 'overall'} example maximum {bound:g} mm")
    if width.get("min") and args.width_mm < float(width["min"]) - 0.05:
        warnings.append(f"width {args.width_mm:g} mm is below the general guideline {width['min']:g} mm; check target journal")
    if width.get("max_height") and args.height_mm is not None and args.height_mm > float(width["max_height"]) + 0.05:
        problems.append(f"height {args.height_mm:g} mm exceeds example maximum {width['max_height']:g} mm")
    if profile.get("max_file_mb") and args.file.stat().st_size > float(profile["max_file_mb"]) * 1024 * 1024:
        problems.append(f"file exceeds {profile['max_file_mb']} MiB guideline")

    try:
        size = dimensions(args.file)
    except (RuntimeError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Profile: {profile['publisher']} — {profile['scope']}")
    print(f"File: {args.file}  |  final target: {args.width_mm:g} mm wide  |  kind: {args.kind}")
    if size:
        effective = size[0] / (args.width_mm / 25.4)
        print(f"Raster: {size[0]} x {size[1]} px; effective horizontal density: {effective:.1f} dpi")
        minimum = profile["raster_min_dpi"].get(args.kind)
        if minimum is not None and effective < float(minimum):
            problems.append(f"effective DPI {effective:.1f} below the selected example guideline of {minimum} dpi")
        elif minimum is not None:
            print(f"PASS: effective DPI meets {minimum} dpi profile threshold")
        if args.kind == "line" and profile.get("vector_line_art_preferred"):
            warnings.append("For line plots, editable vector PDF/EPS/SVG is normally preferable")
        preferred = profile.get("raster_preferred_dpi", {}).get(args.kind)
        if preferred and effective < float(preferred):
            warnings.append(f"consider at least {preferred} dpi for higher-quality output when raster is needed")
    else:
        warnings.append("Vector/unknown file: embedded image DPI, actual dimensions and editable fonts were NOT inspected")

    print("Important: the effective DPI assumes the WHOLE file occupies the requested width.")
    print("Embedded SEM/TEM panels may have LOWER effective resolution and need independent checks.")
    print("Fonts, line weights, color gamut, scale bars, panel ordering, journal-specific exceptions, AI and licensing policies require manual checks.")
    for item in warnings:
        print("NOTE:", item)
    for item in problems:
        print("FAIL:", item)
    print("RESULT:", "NEEDS FIXES" if problems else "BASIC PREFLIGHT PASSED (not publisher certification)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
