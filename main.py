import re
import base64
from flask import Flask, render_template,request
import cv2
import joblib

model=joblib.load('KNN-Handwritten-Written-Digits.sav')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('drawdigits.html')

@app.route('/predictdigits/', methods=['GET','POST'])
def predict_digits():
    parseImage(request.get_data())
    
    img=cv2.imread('output.png')
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.resize(img,(8,8))
    img=img.reshape(1,64)
    img=(img/255.0)*15.0
    img=15-img

    prediction=model.predict(img)

    return str(prediction[0])

def parseImage(imgData):
    # parse canvas bytes and save as output.png
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

if __name__ == '__main__':
    app.run(debug=True)
