from flask import Flask, request, jsonify
from keras.models import load_model
import numpy as np
import io
import base64
from PIL import Image
import re

app = Flask(__name__)
model = load_model('bestmodel.h5')

def preprocess_image(image_data):
    image_data = re.sub('^data:image/.+;base64,', '', image_data)
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    image = image.convert('L')
    image = image.resize((28, 28))
    image = np.array(image)
    image = image.astype('float32') / 255
    image = np.expand_dims(image, axis=0)
    image = np.expand_dims(image, axis=-1)
    return image

@app.route('/predict', methods=['POST'])
def predict_digit():
    data = request.get_json()
    image_data = data['image_data']
    image = preprocess_image(image_data)
    prediction = model.predict(image)
    predicted_digit = np.argmax(prediction)
    return jsonify({'predicted_digit': int(predicted_digit)})

if __name__ == '__main__':
    app.run(debug=True)
