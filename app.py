from flask import Flask,render_template,request
import joblib  
import numpy as np 
model = joblib.load('Heart_Attack_Prediction.pkl')
app=Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/predict", methods=["POST"])  
def predict():  
  age = float(request.form["age"])  
  sex = float(request.form["sex"] ) 
  cp = float(request.form["chestpain"])
  trestbps = float(request.form["resting_blood_pressure"])  
  chol =float( request.form["cholesterol"])  
  fbs = float(request.form["fasting_blood_sugar"])
  restecg = float(request.form["resting_electrocardiographic"])    
  thalach = float(request.form["max_heart_rate"])
  exang = float(request.form["exercise_induced_angina"] ) 
  oldpeak = float(request.form["oldpeak"]) 
  slope = float(request.form["slope"])   
  ca = float(request.form["num_major_vessels"])    
  thal = float(request.form["thalassemia"])  
   
  pred = model.predict(np.array([[age, sex, cp, trestbps,  
            chol, fbs, restecg, thalach,  
            exang, oldpeak, slope, ca,  
            thal]]))  
  if pred == 0:  
    return render_template('no.html')  
  else:  
    return render_template('yes.html') 
   
if  __name__=='__main__':
  app.run(debug=True)