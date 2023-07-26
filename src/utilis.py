import os
import sys

import dill
from src.exception import customizedException
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score

try:
    def save_object(file_path,obj):
         path=os.path.dirname(file_path)
         
         os.makedirs(path,exist_ok=True)



         with open(file_path,"wb") as file_object:
             dill.dump(obj,file_object)


except Exception as e:
     raise customizedException(e,sys)
try:
    def evalution_model(true,prediction):
        score=accuracy_score(true,prediction)
        
    
        return score
except Exception as e:
    raise customizedException(e,sys)





try:
    def model_evalution(X_train,X_test,Y_train,Y_test,models):
         models_list=[]
         accu_score=[]
         
         for i in range(len(list(models))):
             model=list(models.values())[i]
    
             #training the model
             model.fit(X_train,Y_train)
    
             #prediction:
             Y_predict=model.predict(X_test)
    
             score=evalution_model(Y_test,Y_predict)
    
   
             models_list.append(list(models.keys())[i])
    
        
             accu_score.append(score)
    
            
             

         return models_list,accu_score
except Exception as e:
    raise customizedException(e,sys)



def load_object(file_path):  
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise customizedException(e,sys)
    
    
             
       
          
          

