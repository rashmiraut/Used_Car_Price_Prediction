# Used Car Price Prediction

## App Link
If you want to view the deployed model, click on the following link:<br />
https://tccarpriceprediction.herokuapp.com/

## About the App
The Car Price Prediction is a flask web application which predicts prices of used cars based on given independent features like Year,	Mileage, Make and Model. The dataset is provided by truecars.com.

The original dataset contained:

Price: This is the price of the used car displayed in the website(Numeric)

Mileage: Mileage of the used car(Numeric)

Year: Shows the manufacturing year of the car(Numeric)

City: Shows the city where the car belongs to(Nominal)

State: Shows the state from which the city belongs to(Nominal)

Make: Manufacturer of the car(Nominal)

Model: The model of the car(Nominal)

Vin: Vehicle identification number of the car

## This project consists of the following sections

1) Data pre-processing
2) Exploratory Data Analysis
3) Data modeling : Gradient Boosting
4) Deploying the model using Flask and Heroku

## Data modeling

For the modeling, Price is considered as the dependent variable. Year, Mileage, Make and Model are the independent variables.

The gradient booster model has an accuracy of 86%

## Deployment

Flask and Heroku are used to deploy this model

## Conclusion

The price of the used car depends on year of car purchase (Newer the car higher the price)


