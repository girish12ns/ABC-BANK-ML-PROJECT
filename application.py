import sys
from flask import Flask,render_template,request
from src.data_pipeline.predict_pipeline import Custom_data,PredictPipe

from src.exception import customizedException
import pandas as pd
import numpy as np
from src.logger import logging



application=Flask(__name__)

app=application

@app.route("/")
def welcome():
    return render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_data():
    try:
        if request.method=='GET':
            return render_template('home.html')
        else:
            data=Custom_data(
                 Geography=request.form.get('Geography'),
                 Gender=request.form.get('Gender'),
                 CreditScore=request.form.get('CreditScore'),
                 Age=int(request.form.get('Age')),
                 Tenure=int(request.form.get('Tenure')),
                 Balance=float(request.form.get('Balance')),
                 NumOfProducts=float(request.form.get('NumOfProducts')),
                 HasCrCard=float(request.form.get('HasCrCard')),
                 IsActiveMember=float(request.form.get('IsActiveMember')),
                 EstimatedSalary=float(request.form.get('EstimatedSalary')))
            
            logging.info("data_frame started")
             
            pred_df=data.get_data_frame()
            print(pred_df)

            predict_pipe=PredictPipe()
            results=predict_pipe.predict_data(pred_df)

            return render_template('home.html',results=results[0])
    except Exception as e:
        raise customizedException(e,sys)


if __name__=="__main__":
    app.run(debug=False)