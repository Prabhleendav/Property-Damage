import streamlit as st
import numpy as np
import cv2
from PIL import Image
from image_matching import calculate_match_percentage

# Streamlit app UI
def main():
    st.title('Image Comparison - Match Percentage')

    # Upload images
    uploaded_before = st.file_uploader("Upload 'Before' Image", type=["png", "jpg", "jpeg"])
    uploaded_after = st.file_uploader("Upload 'After' Image", type=["png", "jpg", "jpeg"])

    if uploaded_before and uploaded_after:
        # Convert images to OpenCV format (BGR)
        before_image = np.array(Image.open(uploaded_before))
        after_image = np.array(Image.open(uploaded_after))

        before_cv = cv2.cvtColor(before_image, cv2.COLOR_RGB2BGR)
        after_cv = cv2.cvtColor(after_image, cv2.COLOR_RGB2BGR)

        # Display images
        st.image(before_image, caption="Before Image", use_column_width=True)
        st.image(after_image, caption="After Image", use_column_width=True)

        # Calculate match percentage
        match_percentage = calculate_match_percentage(before_cv, after_cv)

        # Display result
        st.success(f"Match Percentage: {match_percentage:.2f}%")

if __name__ == "__main__":
    main()
