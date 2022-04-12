
from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin
import pickle
import sklearn
import numpy as np
import pandas as pd
app = Flask(__name__)

    
model=pickle.load(open('GBR.pkl','rb'))
car=pd.read_csv('df_full.csv')

@app.route('/',methods=['GET','POST'])
def index():
    Make=sorted(car['Make'].unique())
    Model=sorted(car['Model'].unique())
    Year=sorted(car['Year'].unique(),reverse=True)
    Usage_level=car['Usage_level'].unique()
    
    Make.insert(0,'Select Your Car Manufacturer')
    return render_template('index.html',Make=Make, Model=Model, Year=Year,Usage_level=Usage_level)
    
@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    Make=request.form.get('Make')

    Model=request.form.get('Model')
    Year=request.form.get('Year')
    
    Usage_level=request.form.get('Usage_level')
    Mileage=request.form.get('Mileage')
    
    prediction=model.predict(pd.DataFrame(columns=['Year', 'Mileage', 'Make', 'Model','Usage_level'],
                              data=np.array([Year, Mileage, Make, Model,Usage_level]).reshape(1, 5)))
    print(prediction)
    
    return str(np.round(prediction[0],2))


@app.route("/predict", methods=['POST'])
def pred():
    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug = True)
