import sys
import pandas as pd
from src.exception import customizedException
from src.utilis import load_object
from src.logger import logging


class PredictPipe:
    def __init__(self):
        pass
    
    def predict_data(self,features):
        logging.info("The logging has input data started")
        try:
            model_path='Artifacts/model_trainer.pkl'
            processor_path='Artifacts/preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=processor_path)
            logging.info("got model pkl and preprocessor pkl")
            
            scaled_data=preprocessor.transform(features)
            predict=model.predict(scaled_data)

            return predict
        except Exception as e:
            raise customizedException(e,sys)




class Custom_data:
    def __init__(self,Geography:str,Gender:str,CreditScore:int,Age:int,Tenure:int,Balance:float,NumOfProducts:int,HasCrCard:int,
                 IsActiveMember:int,EstimatedSalary:int):
        self.Geography=Geography

        self.Gender=Gender

        self.CreditScore=CreditScore

        self.Age=Age

        self.Tenure=Tenure

        self.Balance=Balance

        self.NumOfProducts=NumOfProducts

        self.HasCard=HasCrCard

        self.IsActiveMember=IsActiveMember

        self.EstimatedSalary=EstimatedSalary

    def get_data_frame(self):
        try:
            custom_data_input={
                "Geography":[self.Geography],
                "Gender":[self.Gender],
                "CreditScore":[self.CreditScore],
                "Age":[self.Age],
                "Tenure":[self.Tenure],
                "Balance":[self.Balance],
                "NumOfProducts":[self.NumOfProducts],
                "HasCrCard":[self.HasCard],
                "IsActiveMember":[self.IsActiveMember],
                "EstimatedSalary":[self.EstimatedSalary]
            }
        
            return pd.DataFrame(custom_data_input)
         
        except Exception as e:
            raise customizedException(e,sys)


       