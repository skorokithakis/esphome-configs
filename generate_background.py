from PIL import Image
from PIL import ImageDraw

WIDTH = 240
HEIGHT = 240

img = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(img)

# Horizon line position (middle of screen).
horizon_y = (HEIGHT // 2) + 40

gray = (60, 60, 60)

# Vertical grid lines: parallel at horizon, spread out at bottom.
# Lines are evenly spaced at horizon and fan out toward the bottom.
num_vertical = 15
center_x = WIDTH // 2
spread_factor = 2.5

for i in range(num_vertical + 1):
    # Position at horizon (evenly spaced).
    horizon_x = int(i * WIDTH / num_vertical)

    # Position at bottom (spread out from center).
    offset_from_center = horizon_x - center_x
    bottom_x = int(center_x + offset_from_center * spread_factor)

    draw.line([(horizon_x, horizon_y), (bottom_x, HEIGHT)], fill=gray, width=1)

# Horizontal grid lines with perspective (closer together near horizon).
num_horizontal = 12
for i in range(1, num_horizontal + 1):
    t = i / num_horizontal
    y = int(horizon_y + (HEIGHT - horizon_y) * (t**1.5))
    draw.line([(0, y), (WIDTH, y)], fill=gray, width=1)

# Horizon line.
horizon_color = (80, 80, 80)
draw.line([(0, horizon_y), (WIDTH, horizon_y)], fill=horizon_color, width=1)

img.save("synthwave_bg.png")
print("Created synthwave_bg.png")
