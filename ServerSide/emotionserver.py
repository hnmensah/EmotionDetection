from tkinter import *
from threading import *
import os
#Flask
from flask import Flask
from flask import jsonify, request

from sklearn.externals import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import nltk
import re
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
#from nltk.corpus import stopwords

import string



app=Flask(__name__)


msg1=""
String1=""

@app.route('/',methods=['POST','GET'])

def pred():
    print("In predict")
    
    


    
   
    
    
    
    try:





        
        
        #print(request)
        #print(request.args)
        #print(request.get_json())
        #print(request.values)
        #print(request.data)
        print(request.form['name'])
        #for i in request.form:
            #print(i)
        #print(request.read_json())
        
        
        msg1 = request.form['name']
        print(msg1)
    except:
        print("Exception")
        msg1="what are the plans for tomorrow must be an exciting weekend "

    Y=[]
    corpus=[]

    x=re.sub('[^a-zA-Z]', ' ',msg1)
    x=x.lower()
    x=x.split()
    ps=PorterStemmer()
    x=[ps.stem(word) for word in x if not word in set(stopwords.words('english'))]
    x=' '.join(x)
    corpus.append(x)
    #print(corpus)
    new=open("COUNTVECTORIZER.pickle","rb")
    cv=pickle.load(new)
    new.close()
    X=cv.transform(corpus).toarray()
    new=open("nlp.pickle","rb")
    clf=pickle.load(new)
    new.close()
    predict=clf.predict(X)
    print(predict[0])


    
    

    
    
    return predict[0],200
app.run()





