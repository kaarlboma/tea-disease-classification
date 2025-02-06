from fastapi import FastAPI, File, UploadFile
import numpy as np
import pickle
from functions import image_to_array
from PIL import Image
from io import BytesIO
import mimetypes

# Load model
model_name = 'xgb_reg.pkl'
model_path = 'models/' + model_name
model = pickle.load(open(model_path, "rb"))

# Create FastAPI object
app = FastAPI()

# API operations
@app.get("/")
def health_check():
    return {'health_check': 'OK'}

@app.post("/classify")
def classify(file: UploadFile = File(...)):
    mime_type, _ = mimetypes.guess_type(file.filename)
    if not mime_type or not mime_type.startswith("image/"):
        return {"error": "File must be an image"}
    
    try:
        # Read the uploaded file as bytes
        contents = file.file.read()
        print(f"Received file with {len(contents)} bytes.")  # Log the byte size

        # Attempt to open the image using BytesIO
        try:
            img = Image.open(BytesIO(contents))
            img.verify()  # Verify the image integrity
            print("Image opened and verified successfully.")  # Log success
        except Exception as e:
            return {"error": f"Error opening image: {e}"}

        # Convert image to array
        arr = image_to_array(contents)
        print(f"Image converted to array with shape: {arr.shape}")  # Log shape of the array

        # Ensure the input matches model expectations
        predictions = model.predict(arr)
        print(f"Predictions: {predictions}")  # Log predictions

        # Return predictions as a list
        return {"predictions": predictions.tolist()}
    
    except Exception as e:
        return {"error": f"Failed to process image or predict: {e}"}
