from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import sys
import os
from src.exception import customizedException
from src.logger import logging
import pandas as pd
import numpy as np
from src.utilis import save_object
from dataclasses import dataclass


@dataclass
class Data_transfromationConfig:
    preprocessor_path=os.path.join("Artifacts","preprocessor.pkl")

class data_transformation:
    def __init__(self):
        self.data_tranformation_config=Data_transfromationConfig()

    def data_transformation_object(self):

        numerical_features=['CreditScore','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember',
                            'EstimatedSalary',]
        categorical_features=['Geography','Gender']

        


        

    

        num_pip=Pipeline(steps=[
            ('imputer',SimpleImputer(strategy='mean')),
            ('scaler',StandardScaler())
            ])
        cat_pip=Pipeline(steps=[
            ('imputer',SimpleImputer(strategy="most_frequent")),
            ('encoder',OneHotEncoder())
            
        ])
                          
        preprocessor=ColumnTransformer([
            ('num_pip',num_pip,numerical_features),
            ('cat_pip',cat_pip,categorical_features)
        ])
        
        return preprocessor

    def data_transformation_object_iniatited(self,train_path,test_path):
        logging.info("data_transformation_object_started")
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

         

            logging.info("spling of data")

            target_variable='Exited'

            train_input_features=train_df.drop(target_variable,axis=1)
            train_target=train_df[target_variable]

            test_input_features=test_df.drop(target_variable,axis=1)
            test_target=test_df[target_variable]

            preprocessor_obj=self.data_transformation_object()
            train_input_features_arr=preprocessor_obj.fit_transform(train_input_features)
            test_input_features_arr=preprocessor_obj.transform(test_input_features)

            train_ar=np.c_[train_input_features_arr ,np.array(train_target)]

            test_ar=np.c_[test_input_features_arr,np.array(test_target)]

            save_object(file_path=self.data_tranformation_config.preprocessor_path,
                    obj=preprocessor_obj)

            return (
                train_ar,
                 test_ar
            )
        except Exception as e:
            raise customizedException(e,sys)

        

