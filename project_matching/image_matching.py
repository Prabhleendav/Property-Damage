import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Function to calculate match percentage
def calculate_match_percentage(before, after):
    # Convert images to grayscale
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    # Ensure both images have the same size
    if before_gray.shape != after_gray.shape:
        after_gray = cv2.resize(after_gray, (before_gray.shape[1], before_gray.shape[0]))

    # Convert images to float64 (SSIM requires this format)
    before_gray = before_gray.astype("float64") / 255.0
    after_gray = after_gray.astype("float64") / 255.0

    # Compute SSIM
    try:
        score, _ = ssim(before_gray, after_gray, full=True)
        return score * 100
    except ValueError as e:
        print(f"SSIM calculation error: {e}")
        return 0  # Return 0% if SSIM fails
