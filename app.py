
from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin
import pickle
import sklearn
import numpy as np
import pandas as pd
app = Flask(__name__)

    
model=pickle.load(open('GBR.pkl','rb'))
car=pd.read_csv('df_full.csv')

@app.route('/', methods=['Get', 'POST'])
def index():
    make = sorted(car['Make'].unique())
    model = car['Model'].unique()
    year = sorted(car['Year'].unique(), reverse=True)
    mileage = car['Mileage'].unique()

    return render_template('index.html', make=make, models=model, years=year, mileage=mileage)


@app.route("/predict", methods=["POST"])
def predict():
    make = request.form.get("make")
    model = request.form.get('model')
    year = request.form.get('year')
    mileage = request.form.get('mileage')

    data = {'Make': make,
            'Model': model,
            'Year': year,
            'Mileage': mileage, }

    features = pd.DataFrame(data, index=[0])
    pred = load_lr.predict(features)

    return render_template("predict.html", prediction=np.round(pred[0], 2))


if __name__ == "__main__":
    app.run(debug=True)
