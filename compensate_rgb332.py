#!/usr/bin/env python3
"""
Compensate an image for RGB332 color quantization.

RGB332 has unequal bit depth: 3 bits red, 3 bits green, 2 bits blue.
This causes grays to appear green/yellow because blue is under-represented.
This script pre-adjusts colors so they appear correct after RGB332 conversion.
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)


def quantize_rgb332(r: int, g: int, b: int) -> tuple[int, int, int]:
    """Simulate RGB332 quantization."""
    r_out = (r >> 5) * 255 // 7
    g_out = (g >> 5) * 255 // 7
    b_out = (b >> 6) * 255 // 3
    return (r_out, g_out, b_out)


def compensate_pixel(r: int, g: int, b: int) -> tuple[int, int, int]:
    """
    Adjust pixel color to compensate for RGB332 quantization.

    The goal is to find input values that, after RGB332 quantization,
    produce colors as close as possible to the original intended color.
    """
    # RGB332 quantization levels.
    r_levels = [i * 255 // 7 for i in range(8)]  # 0, 36, 73, 109, 146, 182, 219, 255
    g_levels = [i * 255 // 7 for i in range(8)]
    b_levels = [i * 255 // 3 for i in range(4)]  # 0, 85, 170, 255

    def find_best_input(target: int, levels: list[int], bits: int) -> int:
        """Find input value that quantizes closest to target."""
        best_input = 0
        best_diff = 256

        # The quantization threshold for each level.
        shift = 8 - bits
        for test_input in range(256):
            level_index = test_input >> shift
            quantized = levels[level_index]
            diff = abs(quantized - target)
            if diff < best_diff:
                best_diff = diff
                best_input = test_input
                if diff == 0:
                    break

        return best_input

    # Find input values that quantize closest to original colors.
    r_comp = find_best_input(r, r_levels, 3)
    g_comp = find_best_input(g, g_levels, 3)
    b_comp = find_best_input(b, b_levels, 2)

    return (r_comp, g_comp, b_comp)


def process_image(input_path: Path, output_path: Path) -> None:
    """Process image with RGB332 compensation."""
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            pixels[x, y] = compensate_pixel(r, g, b)

    img.save(output_path)
    print(f"Saved compensated image to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Compensate image colors for RGB332 display quantization."
    )
    parser.add_argument("input", type=Path, help="Input image file")
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output file (default: input_compensated.png)"
    )

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: {args.input} not found")
        sys.exit(1)

    if args.output is None:
        args.output = args.input.with_stem(args.input.stem + "_compensated")

    process_image(args.input, args.output)


if __name__ == "__main__":
    main()
