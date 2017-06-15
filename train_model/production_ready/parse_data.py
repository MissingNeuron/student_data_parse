import pandas as pd 
import numpy as np
import data_np_formater as dnf
import data_type_model as dtm

from keras.models import Sequential
from keras.layers import Activation, Dense

#Create data encoder class
denc = dtm.dataTypeEncoder();

df = pd.read_csv("../../data/final.csv" , low_memory=False)

#Buildig matrix for training

#Creates encoding that is triggered for each source that the applicant belongs to
sourceEnc = denc.getSourceEncoding(df["Source"] , denc.source_ , "nan" ,";")

#Extract the zip info
#Get zipcode_inf_avail 1 if we have zip code info else 0
#Use normalize as 1 to skip normalizing the values 
zip_code = dnf.getNPFromPandas(df["Zipcode_inf_avail"] , [] , 1 , 0)

#Get Citizenship_flag
citizen = dnf.getNPFromPandas(df["Citizenship_Flag"] , [] , 1 , 0)

#Get one hot array for race
race = denc.encodeArray(df["Race"] , denc.race_, "nan")

#Get one hot array for gender
gender = denc.encodeArray(df["Gender"] , denc.gender_, "Other")

#Get one hot array for Degree
degree = denc.encodeArray(df["Degree"] , denc.degree_, "nan")

#Add student segment, type, and application type
std_seg = denc.encodeArray(df["Student_Segment"] , denc.std_seg_, "nan")
std_type = denc.encodeArray(df["Student_Type"] , denc.std_type_, "nan")
app_type = denc.encodeArray(df["Applicant_Type"] , denc.app_type_, "nan")

#The normalize value is the almost the average of the data. EX 20000 is the average population of a zip code

#Age when applies
awa = dnf.getNPFromPandas(df["Age"] , [] , 18 , 0)

#Get age when finished high school
#Deviding by the national average. Some values are set to 0 if the information was not available
afh = dnf.getNPFromPandas(df["Age_Finished_HS"] , [] , 18 , 0)

#Get population
population = dnf.getNPFromPandas(df["Population"] , [","] , 20000 , 0)

#Get Median_Age
median_age = dnf.getNPFromPandas(df["Median_Age"], [] , 37 , 0)

#Get Education
education = dnf.getNPFromPandas(df["Education"], ["%"] , 100 , 0)

#Get Median_Income
median_income = dnf.getNPFromPandas(df["Median_Income"], [","] , 45000 , 0)

#Get Immigrants
immigrants = dnf.getNPFromPandas(df["Immigrants"], [","] , 1500 , 0)

#Get Poverty
poverty = dnf.getNPFromPandas(df["Poverty"], ["%"] , 100 , 0)

#Get one hot array from roles
roles = df["Role"].as_matrix()

#Transform stage into a binary matrix. 0 is closed else 1
roles[roles != "Student"] = 0
roles[roles == "Student"] = 1
roles = roles.astype(np.float64)
roles[np.isnan(roles)] = 0

#Merging all data together
data = np.vstack([zip_code ,citizen , awa , afh , population , median_age , 
                  education , median_income , immigrants , poverty  ])

#Adding race
data = np.append(data , race.T , axis = 0)
#Adding gender
data = np.append(data , gender.T , axis = 0)
#Adding degree
data = np.append(data , degree.T , axis = 0)
#Add student segment, type, and application type
data = np.append(data , std_seg.T , axis = 0)
data = np.append(data , std_type.T , axis = 0)
data = np.append(data , app_type.T , axis = 0)
#Add source enc
data = np.append(data , sourceEnc.T , axis = 0)
#Adding the roles 
roles = np.resize( roles ,(1 , roles.shape[0]))
data = np.append(data , roles , axis = 0)

data = data.T

#Permutate the data
np.random.shuffle(data)

#Extract the end values
Y = data[ : , -1: ]
X = data[: , :-1]

#Set the train data number
trainSize = 466058

trainX= X[:trainSize , :]
trainY= Y[:trainSize , :]
testX= X[trainSize:  , :]
testY= Y[trainSize: , :]

model = Sequential()
model.add(Dense(X.shape[1] , input_dim=X.shape[1]))
model.add(Activation('relu'))

model.add(Dense(50))
model.add(Activation('relu'))

model.add(Dense(50))
model.add(Activation('relu'))

model.add(Dense(50))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='mean_squared_error',optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(trainX, trainY, batch_size=1000, epochs=3, verbose=1)

#score = model.evaluate(testX, testY, verbose=0)
prediction = model.predict(testX)

score = model.evaluate(testX, testY, verbose=0)
print(score)

tolerance = 0.5
prediction[prediction >= tolerance] = 1
prediction[prediction < 1] = 0

prediction = prediction.astype(np.int16)
testY = testY.astype(np.int16)

true_p = sum((prediction == 0 ) & (testY == 0))[0]
false_p = sum((prediction == 0 ) & (testY == 1))[0]
true_n = sum((prediction == 1 ) & (testY == 1))[0]
false_n = sum((prediction == 1 ) & (testY == 0))[0]

prec = true_p / (true_p + false_p)
recall = true_p / (true_p + false_n)

fscore = 2 * (prec * recall ) / (prec + recall)

print(fscore)