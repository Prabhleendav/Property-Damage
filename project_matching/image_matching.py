import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def calculate_match_percentage(before, after):
    # Convert the images from RGB (PIL) to BGR (OpenCV)
    before = cv2.cvtColor(before, cv2.COLOR_RGB2BGR)
    after = cv2.cvtColor(after, cv2.COLOR_RGB2BGR)

    # Convert images to grayscale
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    # Resize to ensure same dimensions
    after_gray = cv2.resize(after_gray, (before_gray.shape[1], before_gray.shape[0]))

    # Convert images to float32 for SSIM
    before_gray = before_gray.astype("float32") / 255.0
    after_gray = after_gray.astype("float32") / 255.0

    # Compute SSIM
    score, _ = ssim(before_gray, after_gray, full=True)

    return score * 100
