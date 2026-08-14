import streamlit as st
from PIL import Image

st.title("Image Viewer")

file = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg"]
)

if file is not None:
    image = Image.open(file)

    st.image(
        image,
        caption="Uploaded image"
    )

    st.write(f"Width: {image.width}px")
    st.write(f"Height: {image.height}px")
    st.write(f"Format: {image.format}")
    st.write(f"Mode: {image.mode}")