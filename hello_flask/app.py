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
    MinTemp = request.form.get('MinTemp')
    MaxTemp = request.form.get('MaxTemp')
    Sunshine = request.form.get('Sunshine')
    
    result = knn.predict([[float(MinTemp),float(MaxTemp),float(Sunshine)]])[0]

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
    app.run(debug=True, use_reloader=False)