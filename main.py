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
           '<h1>Welcome To Python Server Edit last 10/6/2023</h1>' \
           '<p> Image To Text Easy OCR  Version : 1.6.3</p>' \
           f'<p>Status :{tr.tesseract_call.result["status"]}</p>' \
           '</center>'


@app.route('/img-to-text', methods=['POST'])
def img_to_text():
    data = request.json
    url_img = data['url_img']
    ter = tr.tesseract_call(url_img)
    result = ter.set_data()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2000)
    # app.run(debug=True)
