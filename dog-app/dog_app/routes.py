import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dog_app import app

from flask import Flask
from flask import render_template, request, redirect

from detectors import dog_breed_detector 

@app.route('/')
@app.route('/index')
def index():
    # render web page with plotly graphs
    return render_template('master.html')
# web page that handles user query and displays model results
@app.route('/go', methods=["GET", "POST"])
def go():
    if request.method == "POST":
        if request.files:
            query = request.files["image"]

            file_name = "static/pic"
            query.save("dog_app/static/pic")
                     
            prediction = dog_breed_detector("dog_app/static/pic")
            
            os.remove("dog_app/static/pic")    
            
            if len(prediction) > 30:
                dog_pic = "static/dog_images/error.jpg"
            elif len(prediction)>0:
                dog_pic = "static/dog_images/" + prediction + "_.jpg"
            
            return render_template(
        'go.html', prediction = prediction, dog_pic = dog_pic)

    return render_template('master.html')

