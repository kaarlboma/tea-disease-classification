from PIL import Image
import numpy as np
from io import BytesIO

def image_to_array(file: bytes):
    # Open the image from the binary file content
    img = Image.open(BytesIO(file)).resize((100, 100))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    # Convert the image to a NumPy array, flatten it, and reshape
    return np.array(img).flatten().reshape(1, -1)