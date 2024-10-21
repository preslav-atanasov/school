import cv2
import numpy as np
import mss
import time
from pynput.mouse import Controller

# Set up pyautogui
import pyautogui

pyautogui.PAUSE = 0
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0

# Load the image to find
image_to_find = "black_ball.png"
target_image = cv2.imread(image_to_find, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded correctly
if target_image is None:
    print(f"Error: Could not load image '{image_to_find}'. Please check the file path.")
    exit()

# Resize the template image for faster matching
scale_percent = 90  # Resize scale
width = int(target_image.shape[1] * scale_percent / 100)
height = int(target_image.shape[0] * scale_percent / 100)
dim = (width, height)
target_image_resized = cv2.resize(target_image, dim, interpolation=cv2.INTER_AREA)

# Set up the region to search (full screen example)
region = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}  # Adjust as necessary

# Setup mss for fast screenshot capturing
with mss.mss() as sct:
    print("Starting image tracking...")

    # Create mouse controller instance once
    mouse = Controller()

    while True:
        # Capture the screen
        screenshot = np.array(sct.grab(region))

        # Convert screenshot from BGRA (MSS format) to BGR (OpenCV format)
        screenshot_bgr = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

        # Convert to grayscale for matching
        screenshot_gray = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)

        # Perform template matching
        result = cv2.matchTemplate(screenshot_gray, target_image_resized, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Print the maximum confidence value for debugging
        print(f"Max confidence: {max_val}")

        # If the confidence is high enough (above the threshold), move the mouse
        if max_val >= threshold:
            # Get the dimensions of the target image
            h, w = target_image_resized.shape

            # Calculate the center of the matched region
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2

            # Move the mouse instantly to the center of the detected area
            mouse.position = (center_x, center_y)  # Move instantly

            # Optional: Add a short sleep to limit the frequency of movements
        else:
            continue
