from flask import Flask, request, jsonify
from flask_cors import CORS
import tesseract_call as tr

app = Flask(__name__)
CORS(app)

# data = request.get_json()
# print(data['message'])


@app.route('/')
def main():
    return '<center>' \
           '<h1>Welcome To Python Server Edit last 21/5/2023</h1>' \
           '<h2>Python Version (3.9)</h2>' \
           '<h3>Flask Version (2.2.2)</h3>' \
           '<p> Image To Text Easy OCR</p>' \
           '</center>'


@app.route('/img-to-text', methods=['POST'])
def img_to_text():
    data = request.json
    url_img = data['url_img']
    ter = tr.tesseract_call(url_img)
    result = ter.set_data()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
