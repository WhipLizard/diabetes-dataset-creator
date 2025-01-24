import csv
import random
import time

start=time.time()
fh=open("diabetes.csv","w")
data=csv.writer(fh)
data.writerow(['glucose','diastolic','triceps','insulin','bmi','dfp','age','diabetes'])
for i in range(2000):
    #glucose level is based on fasting blood sugar data
    glucose=random.randint(70,130)
    
    if glucose >70 and glucose<99:
        #diastolic pres is the pres in the arteries when the heart is at rest betwn the beats
        diastolic=random.randint(60,80)
    elif glucose>99 and glucose<125:
        diastolic=random.randint(80,90)
    elif glucose>125:
        diastolic=random.randint(90,110)
        
    #tricep for normal weighted people
    triceps=random.randint(6,20)
    
    if glucose <99 :
        insulin=random.randint(5,20)
    elif glucose>99 and glucose<120:
        insulin=random.randint(20,50)
    elif glucose>120:
        insulin=random.randint(70,180)
        
    #normal person bmi 18.5-24.9
    #diabetic person bmi
    bmi=round(random.uniform(18,25),2)
    
    #dfp diabetic foot pathology
    dfp=round(random.uniform(0.1,2.0),3)
    
    age=random.randint(10,85)
    diabetic=0
    if glucose >= 126 or insulin > 50 or bmi > 24.9 or age>45:
        diabetic = 1

    li=[glucose,diastolic,triceps,insulin,bmi,dfp,age,diabetic]
    data.writerow(li)

fh.close()
end=time.time()
print("done time recq = ",end-start)
    
    
        
    
    
    
    

    
        
    

