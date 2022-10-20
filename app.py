from flask import Flask, send_file
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
    path=random.choice(os.listdir("static/images"))    
    return send_file(f"static/images/{path}", mimetype='image/PNG')


if __name__ == '__main__':
     app.run()
