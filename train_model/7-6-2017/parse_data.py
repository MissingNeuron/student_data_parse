import pandas as pd 
import numpy as np
import data_np_formater as dnf

from keras.models import Sequential
from keras.layers import Activation, Dense

df = pd.read_csv("../../data/final.csv" , low_memory=False)

#Buildig matrix for training

#Extract the zip info
#Get zipcode_inf_avail 1 if we have zip code info else 0
#Use normalize as 1 to skip normalizing the values 
zip_code = dnf.getNPFromPandas(df["Zipcode_inf_avail"] , [] , 1 , 0)

#Get Citizenship_flag
citizen = dnf.getNPFromPandas(df["Citizenship_Flag"] , [] , 1 , 0)

#Get one hot array for race
race = pd.get_dummies(df["Race"]).as_matrix().astype(np.float64)

#Get one hot array for gender
gender = pd.get_dummies(df["Gender"]).as_matrix().astype(np.float64)

#Get one hot array for Degree
degree = pd.get_dummies(df["Degree"]).as_matrix().astype(np.float64)

#Add student segment, type, and application type
std_seg = pd.get_dummies(df["Student_Segment"]).as_matrix().astype(np.float64)
std_type = pd.get_dummies(df["Student_Type"]).as_matrix().astype(np.float64)
app_type = pd.get_dummies(df["Applicant_Type"]).as_matrix().astype(np.float64)

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
roles = pd.get_dummies(df["Role"]).as_matrix().astype(np.float64)

#Merging all data together
data = np.vstack([zip_code ,citizen , awa , afh , population , median_age , education , median_income , immigrants , poverty  ])

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
#Adding the roles
data = np.append(data , roles.T , axis = 0)
#Flipping the data back 
data = data.T

#Permutate the data
np.random.shuffle(data)

#Extract the end values
Y = data[ : , -3: ]
X = data[: , :-3]

#Set the train data number
trainSize = 466058

trainX= X[:trainSize , :]
trainY= Y[:trainSize , :]
testX= X[trainSize:  , :]
testY= Y[trainSize: , :]

model = Sequential()
model.add(Dense(20 , input_dim=X.shape[1]))
model.add(Activation('sigmoid'))

model.add(Dense(20))
model.add(Activation('sigmoid'))

model.add(Dense(3))
model.add(Activation('sigmoid'))

model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

model.fit(trainX, trainY, batch_size=32, nb_epoch=4, verbose=1)

score = model.evaluate(testX, testY, verbose=0)
print(score)