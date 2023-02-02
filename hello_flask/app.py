from flask import Flask,render_template,request,jsonify
import pickle
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
app = Flask(__name__)

knn = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    BP_rate = request.form.get('BP')
    BMI_rate = request.form.get('BMI')
    age = request.form.get('Age')
    
    result = knn.predict([[float(BP_rate),float(BMI_rate),float(age)]])[0]

    # return "this result is {}".format(result)
    
    if result==1:
        # return jsonify({'label':1})
        return render_template('index.html',label=1)
        # return "yes will happen tomorrow"
    else:
        # return jsonify({'label':-1})
        return render_template('index.html',label=-1)
        # return "no will not happen tomorrow"

#     return "The Mintemp is {} , Maxtemp is{} and sunshine is{}".format(mintemp,maxtemp,sunshine)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False,host='0.0.0.0', port=443)
