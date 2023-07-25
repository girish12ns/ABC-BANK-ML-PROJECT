from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from src.exception import customizedException
from src.logger import logging
from src.utilis import save_object,model_evalution
import sys
import os
from sklearn.metrics import accuracy_score

class Model_trainerConfig:
    path=os.path.join('Artifacts','model_trainer.pkl')

class Model_trainer:
    def __init__(self):
        self.model_trainer_config=Model_trainerConfig()


    def Model_trainer_initiated(self,test_ar,train_ar):
        try:
            x_train,x_test,y_train,y_test=(train_ar[:,:-1],
                                       test_ar[:,:-1],
                                       train_ar[:,-1],
                                       test_ar[:,-1])
        
            models={'logistic_reggresion':LogisticRegression(),
            'Naive_bayes':GaussianNB(),
            'KNeighbors':KNeighborsClassifier(),
            'Decision_tree':DecisionTreeClassifier(),
            'SVC':SVC(),
            'Random_forest':RandomForestClassifier(),
            'GradientBoostingClassifier':GradientBoostingClassifier()}
        
            models_list,accu_score,f1score,precisonscore,recallscore=model_evalution(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)
            
            best_score_models={}
            for model,score in zip(models_list,accu_score):
                best_score_models[model]=score
        
            best_models=list(sorted(best_score_models.items(),key=lambda x:x[1],reverse=True))


           


            best_model=models[best_models[0][0]]


            save_object(file_path=self.model_trainer_config.path,obj=best_model)

            best_model.fit(x_train,y_train)

            predict=best_model.predict(x_test)

            score=accuracy_score(y_test,predict)

            print(score)




            return(
                best_model
            )


           
        except Exception as e:
            raise customizedException(e,sys)











            








