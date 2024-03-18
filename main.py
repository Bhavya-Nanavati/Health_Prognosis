from flask import Flask,redirect,render_template,url_for,request

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/welcome',methods=['POST','GET'])
def welcome():
    return 'hell'
    


if  __name__=='__main__':
    app.run(debug=True)