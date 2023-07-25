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
        score_f1=f1_score(true,prediction)
        precision=precision_score(true,prediction)
        recall=recall_score(true,prediction)
    
        return score,score_f1,precision,recall
except Exception as e:
    raise customizedException(e,sys)





try:
    def model_evalution(x_train,x_test,y_train,y_test,models):
         models_list=[]
         accu_score=[]
         f1score=[]
         precisonscore=[]
         recallscore=[]
         for i in range(len(list(models))):
             model=list(models.values())[i]
    
             #training the model
             model.fit(x_train,y_train)
    
             #prediction:
             Y_predict=model.predict(x_test)
    
             score,score_f1,precision,recall=evalution_model(y_test,Y_predict)
    
   
             models_list.append(list(models.keys())[i])
    
        
             accu_score.append(score)
    
            
             f1score.append(score_f1)
    
            
             precisonscore.append(precision)
    
          
             recallscore.append(recall)

         return models_list,accu_score,f1score,precisonscore,recallscore
except Exception as e:
    raise customizedException(e,sys)
    
try:
    def load_object(file_path):

        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
except Exception as e:
    raise customizedException(e,sys)
    
    
             
       
          
          

