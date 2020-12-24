# -*- coding: utf-8 -*-
#importing the libraries
#import flask library 
from flask import Flask, request, render_template
#import numpy
import numpy as np
#import regular expression package
import re
#import request library
import requests

#Defining the app
app = Flask(__name__)

#Defining the Output Function
def check(output):

    url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"
    
    querystring = {"image_url":output,"sourceType":"url"}
    
    payload = '''{\r\n    \"image_url\": "'''+output+'''" ,\r\n    \"sourceType\": \"url\"\r\n}'''
    headers = {
    'x-rapidapi-key': "458cf98460mshb89d2eea976a445p1d4e09jsne5bc3b367bac", #Add your API 
    'x-rapidapi-host': "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com"
    }
    
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text) 
    return response.json()["results"][0]["plate"],response.json()["results"][0]["confidence"]
    
 
#Routing the html page
#home page
@app.route('/')
def home():
    return render_template('base.html')

#Define Predict function
@app.route('/predict',methods=['POST'])
def predict():
    output=request.form['output']
    plate,conf=check(output)
    return render_template('base.html',output=plate+" with confidence score: "+str(round(conf))+"%")

    
if __name__ == "__main__":
    app.run(debug=True)