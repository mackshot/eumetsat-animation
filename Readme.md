# Animated EUMETSAT / Meteosat images

## EUMETSAT latest images
[Here](https://eumetview.eumetsat.int/static-images/latestImages.html) you can find the latest images from Meteosat at 0° and 41.5°E \
Please carefully read and follow there usage and update frequency notes.

## Usage
You can deploy the service as Docker container or just start the api.py (`python3 api.py` or `python3.exe api.py`) \
The base_url needed can be found by navigation to the corresponding service in section [Real-Time Imagery](https://eumetview.eumetsat.int/static-images/)


## Examples

- `http://127.0.0.1:PORT/?base_url=https://eumetview.eumetsat.int/static-images/MSGIODC/PRODUCTS/MPE/SOUTHERNASIA&count=5&fps=1`
- `http://127.0.0.1:PORT/?base_url=https://eumetview.eumetsat.int/static-images/MSG/RGB/NATURALCOLOR/CENTRALEUROPE&count=9&fps=3`

You have to replace PORT with the port your instance is running on (8080 w/o Docker and 8085 w Docker example).
