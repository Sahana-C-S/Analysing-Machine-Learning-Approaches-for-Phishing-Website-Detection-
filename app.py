#importing required libraries

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
warnings.filterwarnings('ignore')
from feature import generate_data_set
# Gradient Boosting Classifier Model
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_selection import RFECV

data = pd.read_csv("phishing.csv")
#droping index column
data = data.drop(['Index'],axis = 1)
# Splitting the dataset into dependant and independant fetature

X = data.drop(["class"],axis =1)
y = data["class"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)
rfecv = RFECV(estimator=gbc, step=5, cv=5, verbose=2, scoring='accuracy', n_jobs=-1)
rfecv = rfecv.fit(X_train, y_train)
X_train_rfecv = rfecv.transform(X_train)
X_test_rfecv = rfecv.transform(X_test)
clf_rfecv_model = gbc.fit(X_train_rfecv, y_train)
gbc.fit(X_train_rfecv, y_train)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", xx= -1)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":

        url = request.form["url"]
        x = np.array(generate_data_set(url)).reshape(1,30) 
        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        return render_template('index.html',xx =round(y_pro_non_phishing,2),url=url )
        # else:
        #     pred = "It is {0:.2f} % unsafe to go ".format(y_pro_non_phishing*100)
        #     return render_template('index.html',x =y_pro_non_phishing,url=url )
    return render_template("index.html", xx =-1)


if __name__ == "__main__":
    app.run(debug=True)