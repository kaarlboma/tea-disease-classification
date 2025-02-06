import streamlit as st
import requests
from PIL import Image
import io
import re

st.markdown("<h1 style='text-align: center; color: white;'>Tea Leaf Disease Identifier</h1>", unsafe_allow_html=True)

url = "http://18.191.119.113/classify"
uploaded_file = st.file_uploader("Choose a file", type = ['png', 'jpg'])

labels_dict = {'white spot': 0,
               'Anthracnose': 1,
               'healthy': 2,
               'gray light': 3,
               'bird eye spot': 4,
               'algal leaf': 5,
               'brown blight': 6,
               'red leaf spot': 7}

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image)

    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")  # Save as PNG or match the uploaded format
    img_bytes.seek(0)  # Move cursor to the start of the file

    # Send image to API
    files = {"file": ("image.png", img_bytes, "image/png")}
    response = requests.post(url, files=files)

    # Show API response
    if response.status_code == 200:
        result = response.json()  # Convert response to Python dictionary
        
        # Ensure result['predictions'] is displayed correctly
        predictions = result.get("predictions", [])
        
        if isinstance(predictions, list) and len(predictions) > 0:
            final_prediction = [key for key,value in labels_dict.items() if value == predictions[0]]
            pattern = "[a-zA-Z ]+"
            final_p = re.search(pattern, str(final_prediction)).group()
            st.write(f"### Prediction: {final_p}")
        else:
            st.write("### Prediction Result: Invalid response format")
    else:
        st.write("Error:", response.text)