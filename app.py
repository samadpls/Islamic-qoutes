from flask import Flask, send_file,redirect
import requests,os,random
from bs4 import BeautifulSoup
app = Flask(__name__)


url = "https://www.betterlyf.com/articles/inspirational-quotes/islamic-quotes/"
className = "wp-block-image"

def getImages(url,className):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    images = soup.find_all("figure", {"class": className})
    imgs = []
    base = "https://www.betterlyf.com/articles/wp-content/uploads/2021/02/"
    for image in images:
        img = image.find("img")
        src = img["src"]
        name = src.split("/")[-1]
        imgs.append(base+name)

    return  imgs

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route("/", methods=["GET"])
def index():
    path=random.choice(os.listdir("static/images"))    
    return send_file(f"static/images/{path}", mimetype='image/PNG')

@app.route("/random", methods=["GET"])
def randomImage():
    imgs = getImages(url,className)
    img = random.choice(imgs)
    return redirect(location=img)



if __name__ == '__main__':
     app.run()


    

print(getImages(url,className))