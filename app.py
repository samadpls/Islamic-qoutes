from distutils.log import debug
from flask import Flask, send_file
from PIL import Image 
from io import BytesIO
app = Flask(__name__)

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route("/", methods=["GET"])
def index():
    import os, random
    path=random.choice(os.listdir("/static/images"))    
    sel_img = Image.open(f"/static/images/{path}")
    img_io = BytesIO()
    sel_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/PNG')


if __name__ == '__main__':
     app.run()