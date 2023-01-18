#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
import pickle


# In[4]:


app = Flask(__name__)

pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    mintemp = request.form.get('MinTemp')
    maxtemp = request.form.get('MaxTemp')
    sunshine = request.form.get('Sunshine')
    
    return "The mintemp is{} , maxtemp is{} and the sunshine is{}".format(MinTemp,MaxTemp,Sunshine)

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:




