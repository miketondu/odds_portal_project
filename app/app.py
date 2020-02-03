# Dependencies
from flask import Flask, request, jsonify, render_template
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

lr = joblib.load("model.pkl") # Load "model.pkl"
#print ('Model loaded')
model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
#print ('Model columns loaded')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    
    json_ = request.form.items()
    #print(json_)
    query = pd.get_dummies(pd.DataFrame(json_))
    query = query.reindex(columns=model_columns, fill_value=0)
    
    prediction = list(lr.predict(query))
    output = jsonify(prediction)
    
    
    return render_template('index.html', prediction_text='Winner {}'.format(output))



@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = lr.predict([np.array(list(data.values()))])

    output = prediction[0]
    
    return output



if __name__ == "__main__":
 

    app.run(port =12345, debug=True)