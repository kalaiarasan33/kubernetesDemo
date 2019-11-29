from flask import Flask, render_template, redirect, url_for, session, flash,request
import requests
import json



app = Flask(__name__)

@app.route('/')
def index():


    return render_template('feedback.html')


@app.route('/api', methods=['POST'])
def api():
    user=request.form['user']  
    email=request.form['email']
    feedback=request.form['feedback']
    phone=request.form['phone']
    d={"user": user,"email":email,"feedback":feedback,"phone":phone}
    url="http://feedback:5000/test"
    r=requests.post(url,d)    


    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
