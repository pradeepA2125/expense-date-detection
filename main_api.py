from flask import Flask,jsonify,request
from rekognitionCode import detect_text
from helper import date_formatter
import boto3
import re
import base64

app = Flask(__name__)


@app.route('/')
def welcome():
    return "<h1>welcome! please use post method or client program provided to detext expenes date</h1>"

@app.route('/extract_date', methods = ['post'])
def call_rekognition():

    base64_image = request.form['base_64_image_content'] # reception of base 64 encoded image
    #print(base64_image)
    image = base64.b64decode(base64_image) # decode it ,since python sdk boto3 for rekognition api does encoding internally
    text_detected = detect_text(image)  #calls the function which makes API call to aws rekognition to detect text
    #print(text_detected)
    date = date_formatter(text_detected)  # method to detect and format date from detected text.
    if date is None:
        date = 'null'

    return jsonify({"date": date})

if __name__ == "__main__":
    app.run()





