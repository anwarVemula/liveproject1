import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



application = Flask(__name__)
app = application

# import ridge regressor and standard sclaer pickle
ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predictdata',methods = ['GET','POST'])
d