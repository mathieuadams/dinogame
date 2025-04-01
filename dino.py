import pyautogui
from PIL import ImageGrab
import time

# print("Move your mouse to the top-left corner of the game area.")
# time.sleep(5)
# print(pyautogui.position())
#
# print("Now move your mouse to the bottom-right corner.")
# time.sleep(5)
# print(pyautogui.position())


def detect_obstacle(screen_region):
    img = ImageGrab.grab(bbox=screen_region)
    pixels = img.load()

    dark_pixel_count = 0
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y][:3]
            if r < 90 and g < 90 and b < 90:
                dark_pixel_count += 1

    print(f"Dark pixels: {dark_pixel_count}")  # 👈 live debug
    return dark_pixel_count > 5


def jump():

    pyautogui.press("space")


print("Starting in 3 seconds...")
time.sleep(3)

# Adjusted detection zone (smaller height, same location)
# obstacle_region = (266, -357, 327, -314)
obstacle_region = (173, 699, 259, 772)




print("Region shown. Close the image window to continue.")

while True:
    if detect_obstacle(obstacle_region):
        jump()
        time.sleep(0.1)
