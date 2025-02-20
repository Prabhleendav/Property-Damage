import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Function to calculate match percentage
def calculate_match_percentage(before, after):
    # Convert the images from RGB (PIL) to BGR (OpenCV)
    before = cv2.cvtColor(before, cv2.COLOR_RGB2BGR)
    after = cv2.cvtColor(after, cv2.COLOR_RGB2BGR)

    # Convert images to grayscale
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    # Resize the images to ensure they are of the same size
    if before_gray.shape != after_gray.shape:
        after_gray = cv2.resize(after_gray, (before_gray.shape[1], before_gray.shape[0]))

    # Calculate Structural Similarity Index (SSIM)
    score, _ = ssim(before_gray, after_gray, full=True)
    
    # Return the match percentage
    return score * 100
