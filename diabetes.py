import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import csv

fh=open("diabetes.csv","a")

data=csv.writer(fh)

df=pd.read_csv("diabetes.csv")

y=df['diabetes']
x=df[['glucose', 'diastolic', 'triceps', 'insulin', 'bmi', 'dfp', 'age',]]

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.9)

model=LogisticRegression()


model.fit(x_train,y_train)

y_pred=model.predict(x_test)

print("accuracy=",accuracy_score(y_test,y_pred)*100,"%")

glucose=int(input("enter glucose"))
diastolic=int(input("enter diastolic"))
triceps=int(input("enter triceps"))
insulin=int(input("enter insulin"))
bmi=float(input("enter bmi"))
dfp=float(input("enter dfp"))
age=int(input("enter age"))
diabetic=model.predict([[glucose,diastolic,triceps,insulin,bmi,dfp,age,]])
if diabetic==0:
  print("the person is not diabetes")
else:
  print("the person is diabetic")
  diabetic=1

li=[glucose,diastolic,triceps,insulin,bmi,dfp,age,diabetic]
data.writerow(li)

fh.close()
'''
file=open("diabetes.csv","r")

df=pd.read_csv("diabetes.csv")

print(df)
'''
