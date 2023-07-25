import os

from sklearn.model_selection import train_test_split

from src.exception import customizedException
import pandas as pd
import numpy  as np
import sys
from dataclasses import dataclass
from src.logger import logging
from src.components.data_transformation import data_transformation
from src.components.Model_trainer import Model_trainer

@dataclass
class DataConfig:
    train_path=os.path.join('Artifacts','train.csv')
    test_path=os.path.join('Artifacts','test.csv')
    raw_path=os.path.join('Artifacts','raw.csv')

class Data_ingestion:
    def __init__(self):
        self.data_ingestionconfig=DataConfig()

    def data_ingestion_intiated(self):
        logging.info("data_ingestion started")
        try:
            churn_df=pd.read_csv('Note book\data\ABC_BANK.csv')

            os.makedirs(os.path.dirname(self.data_ingestionconfig.raw_path),exist_ok=True)

            churn_df.to_csv(self.data_ingestionconfig.raw_path)

            train_set,test_set=train_test_split(churn_df,test_size=0.2,random_state=42)

            train_set.to_csv(self.data_ingestionconfig.train_path)

            test_set.to_csv(self.data_ingestionconfig.test_path)
            
            logging.info("data ingestion started")
            return (
                self.data_ingestionconfig.train_path,
                self.data_ingestionconfig.test_path
            )
            

        except  Exception as e:
            raise customizedException(e,sys)
        

if __name__=="__main__":
    data=Data_ingestion()
    train_set,test_set=data.data_ingestion_intiated()

    data=data_transformation()
    train_ar,test_ar=data.data_transformation_object_iniatited(train_set,test_set)

    model_trainer=Model_trainer()
    model_trainer.Model_trainer_initiated(train_ar,test_ar)

    





