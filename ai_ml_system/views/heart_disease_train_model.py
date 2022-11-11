from django.shortcuts import render
import pandas as pd
# from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import pickle
import warnings

warnings.filterwarnings("ignore")


def train_heart_disease_model(request):
    data = pd.read_csv('dataset/heart_disease/heart.csv')
    print(data)
    y = data['target']
    x = data.drop(['target'], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, random_state=1, test_size=0.2
    )
    model_set = SVC(gamma="auto")
    model_set.fit(x_train, y_train)

    with open("dataset/save_train_data/heart_db_pickle", "wb") as f:
        pickle.dump(model_set, f)

    # with open("dataset/save_train_data/heart_db_pickle", "rb") as f:
    #   new_model =  pickle.load(f)
    #
    #
    #
    #
    # perdictions2 = new_model.predict([[52,1,0,125,212,0,1,168,0,1,2,2,3]])
    #
    # perdictions = new_model.predict(x_test)
    #
    #
    #
    # print(perdictions)
    # print(accuracy_score(y_test, perdictions))
    #
    # print(perdictions2)
    # # print(accuracy_score(y_test, perdictions2))

    return render(request, "AI/train_heart_disease.html")
