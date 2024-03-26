from flask import Flask,render_template,request
import joblib  
import pandas as pd  
import numpy as np 
# model = joblib.load('Heart_Disease_Prediction.pkl')
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')

# @app.route("/predict", methods=["POST"])  
# def predict():  
#    age = request.form["age"]  
#    sex = request.form["sex"]  
#    trestbps = request.form["trestbps"]  
#    chol = request.form["chol"]  
#    oldpeak = request.form["oldpeak"]  
#    thalach = request.form["thalach"]  
#    fbs = request.form["fbs"]  
#    exang = request.form["exang"]  
#    slope = request.form["slope"]  
#    cp = request.form["cp"]  
#    thal = request.form["thal"]  
#    ca = request.form["ca"]  
#    restecg = request.form["restecg"]  
#    arr = np.array([[age, sex, cp, trestbps,  
#             chol, fbs, restecg, thalach,  
#             exang, oldpeak, slope, ca,  
#             thal]])  
#    pred = model.predict(arr)  
#    if pred == 0:  
#      return render_template('no.html')  
#    else:  
#      return render_template('yes.html') 
if  __name__=='__main__':
    app.run(debug=True)