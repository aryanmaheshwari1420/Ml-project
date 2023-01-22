from flask import Flask,render_template,request
import pickle
import pandas as pd
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
    
    result = knn.predict([[MinTemp,MaxTemp,Sunshine]])[0,1]
    
    if result==1:
        # return render_template('index.html',label=1)
        return "yes will happen tomorrow"
    else:
        # return render_template('index.html',label=-1)
        return "no will not happen tomorrow"

#     return "The Mintemp is {} , Maxtemp is{} and sunshine is{}".format(mintemp,maxtemp,sunshine)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)