from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import data_parser as dp
import image_overlay as io
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def get_data():
    """Receives a request from React Native app and sends back a response"""
    url = request.headers.get('spotifyUrl')
    print(url)
    data = is_valid_url(url)
    response = jsonify(data)
    return response


def is_valid_url(url):
    """Checks if a url is valid, if it is, a printout is generated"""
    data = dp.route_album_or_playlist(url)
    if "error" not in data:
        io.generate_printout(data)
    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
