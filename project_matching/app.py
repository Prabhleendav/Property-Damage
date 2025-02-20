import streamlit as st
import numpy as np
from PIL import Image
from image_matching import calculate_match_percentage  # Importing the image matching function

# Streamlit app UI
def main():
    st.title('Image Comparison - Match Percentage')

    # Upload 'before' and 'after' images
    uploaded_before = st.file_uploader("Upload 'Before' Image", type=["png", "jpg", "jpeg"])
    uploaded_after = st.file_uploader("Upload 'After' Image", type=["png", "jpg", "jpeg"])

    if uploaded_before is not None and uploaded_after is not None:
        # Read the images
        before_image = np.array(Image.open(uploaded_before))
        after_image = np.array(Image.open(uploaded_after))

        # Show the uploaded images
        st.image(before_image, caption="Before Image", use_column_width=True)
        st.image(after_image, caption="After Image", use_column_width=True)

        # Calculate the match percentage using the imported function
        match_percentage = calculate_match_percentage(before_image, after_image)

        # Display the result
        st.write(f"Match Percentage: {match_percentage:.2f}%")

if __name__ == "__main__":
    main()
