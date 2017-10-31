from macify import macify
from wayback import wayback
import requests
from flask import request, Flask

app = Flask(__name__)
session = requests.Session()

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def get(path):
    print("GET: " + request.url)
    url = request.url
    wayback_url = wayback(url)
    print("GET Wayback: " + wayback_url)

    headers = {'User-Agent': 'Mozilla/3.0 (Macintosh; I; 68K)'}

    resp = session.get(wayback_url, params=request.args, headers=headers)
    return resp.content, resp.status_code
    #return macify(resp.content), resp.status_code

@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def post(path):
    print("POST: " + request.url)
    url = request.url
    resp = session.post(url, data=request.form, allow_redirects=True)
    return macify(resp.content), resp.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
