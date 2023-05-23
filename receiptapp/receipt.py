from flask import Flask, request
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded.', 400

    file = request.files['file']
    if file.filename == '':
        return 'No file selected.', 400

    image = Image.open(file)
    text = pytesseract.image_to_string(image)

    return text

if __name__ == '__main__':
    app.run()
