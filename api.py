import tempfile
import requests
import re
from PIL import Image
from io import BytesIO
import imageio
from flask import Flask, request, send_file
from waitress import serve

app = Flask(__name__)


def generate(filename, base_url: str, count: int, fps: float) -> bytes:
    start_page = requests.get(f"{base_url}/index.htm")

    matches = re.findall(r'\s+array_nom_imagen\[\d+\]="([^"]+)"', start_page.text)
    # print(matches)

    images = []

    for i in range(0, count):
        response = requests.get(f"{base_url}/IMAGESDisplay/{matches[i]}")
        image = Image.open(BytesIO(response.content))
        images.append(image)

    images.reverse()

    imageio.mimwrite(filename, images, loop=0, duration=1, fps=fps, extension="gif")
    # bytes = imageio.imwrite("<bytes>", images, duration=1, loop=0, extension=".gif")


@app.route("/", methods=["GET"])
def entry():
    base_url = request.args.get('base_url')
    count = request.args.get('count')
    fps = request.args.get('fps')
    with tempfile.NamedTemporaryFile(suffix=".gif") as temp:
        generate(temp.name, base_url, int(count), float(fps))
        return send_file(temp.name, mimetype='image/gif')


serve(app, host="0.0.0.0", port=8080)


# generate('https://eumetview.eumetsat.int/static-images/MSG/RGB/NATURALCOLOR/CENTRALEUROPE', 5)

# https://eumetview.eumetsat.int/static-images/MSG/RGB/NATURALCOLOR/CENTRALEUROPE/index.htm
# https://eumetview.eumetsat.int/static-images/MSG/RGB/NATURALCOLOR/CENTRALEUROPE/IMAGESDisplay/Zskz7
