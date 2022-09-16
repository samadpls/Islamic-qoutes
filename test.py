from flask import Flask, render_template
import random
from PIL import Image 
import time
app = Flask(__name__)

@app.route('/')
def index():
    import os
    x=random.randint(1,6)
    t=f"static/images/image{str(x)}.png"
    im1 = Image.open(t)
    im1=im1.save("static/images/image.png")
    time.sleep(2) 
    return render_template("index.html")

if __name__ == '__main__':
   app.debug = True
   app.run()