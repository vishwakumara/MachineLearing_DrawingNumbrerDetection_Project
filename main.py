import re
import base64
import numpy as np
import cv2
import joblib
from flask import Flask, render_template, request, jsonify

# Load the trained model
try:
    model = joblib.load('KNN-Handwritten-Written-Digits.sav')
except Exception as e:
    print("Model loading failed:", e)
    model = None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('drawdigits.html')

@app.route('/predictdigits/', methods=['POST'])
def predict_digits():
    if not model:
        return "Model not loaded", 500

    if request.method == 'POST':
        try:
            parseImage(request.get_data())
            
            img = cv2.imread('output.png', cv2.IMREAD_GRAYSCALE)
            if img is None:
                return "Image processing failed", 400
            
            img = cv2.resize(img, (8, 8))
            img = img.reshape(1, 64).astype(np.float32)
            img = (img / 255.0) * 15.0
            img = 15 - img  # Invert for compatibility with training data

            prediction = model.predict(img)
            return str(prediction[0])
        except Exception as e:
            return f"Prediction failed: {str(e)}", 500

def parseImage(imgData):
    # Parse base64 image and save as 'output.png'
    try:
        imgstr = re.search(b'base64,(.*)', imgData).group(1)
        with open('output.png', 'wb') as output:
            output.write(base64.decodebytes(imgstr))
    except Exception as e:
        raise ValueError("Failed to decode image: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
