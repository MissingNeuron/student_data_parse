import pandas as pd 
import numpy as np
import data_type_model as dtm
import data_np_formater as dnf

from keras.models import Sequential
from keras.layers import Activation, Dense

df = pd.read_csv("../../data/predict.csv" , low_memory=False)
zip_codes = pd.read_csv("../../data/zip_info.csv" , low_memory=False , encoding = "latin1" , dtype=str)

#Create data encoder class
denc = dtm.dataTypeEncoder();

sourceEnc = denc.getSourceEncoding(df["Source"] , denc.source_ , "nan" ,";")

zip_colnames = ['Zipcode_inf_avail' , 'Population' , 'Median_Age' , 
                'Education' ,'Median_Income' ,'Immigrants' ,'Poverty']
zip_info = denc.getZipInfo(df["Contact_Postal_Code"] , 
                           zip_codes , range(0 , len(df)) , zip_colnames)

citizen = df["Citizenship_Flag"].as_matrix().astype(np.int)

race = denc.encodeArray(df["Race"] , denc.race_, "nan")

gender = denc.encodeArray(df["Gender"] , denc.gender_, "Other")

#Fix wrong degree values
df["Degree"][df["Degree"] == "asn" ] = "Associate of Applied Science"
df["Degree"][df["Degree"] == "Certificate" ] = "Technical Certificate"
df["Degree"][df["Degree"] == "Non-Credit" ] = "Courses Only"
df["Degree"][df["Degree"] == "Associates Degree" ] = "Associate of General Studies"
df["Degree"][df["Degree"] == "Associates of Applied Science" ] = "Associate of Applied Science"

degree = denc.encodeArray(df["Degree"] , denc.degree_, "nan")

std_seg = denc.encodeArray(df["Student_Segment"] , denc.std_seg_, "nan")

#Fix studenttype
df["Student_Type"][df["Student_Type"] == "New First Time" ] = "High School Student;New First Time"
df["Student_Type"][df["Student_Type"] == "Returning-DO NOT USE" ] = "Returning"
df["Student_Type"][df["Student_Type"] == "New Program-DO NOT USE" ] = "New Program"

std_type = denc.encodeArray(df["Student_Type"] , denc.std_type_, "nan")

app_type = denc.encodeArray(df["Applicant_Type"] , denc.app_type_, "nan")

#Get DOB, age when applied, and age when finished high school
#Remove the first 4 chars from the DOB to get the yaer only
dob = df["Date_of_Birth"].as_matrix()
dob = np.array([str(x)[0:4] for x in dob])
#Convert nan values to 0
dob[dob == "nan"] = 0 
dob = dob.astype(np.int)

#same thing for age when applied Created_Time
year_applied = df["Created_Time"].as_matrix()
year_applied = np.array([str(x)[0:4] for x in year_applied])
#Convert nan values to 0
year_applied[year_applied == "nan"] = 0 
year_applied = year_applied.astype(np.int)

#year finished highschool 
year_finished = df["High_School_Graduation_Year"].as_matrix()
year_finished[np.isnan(year_finished)] = 0
year_finished = year_finished.astype(np.int)

awa = year_applied - dob
afh = year_finished - dob

#Get zip info from our zip code array
zip_code = dnf.getNPFromPandas(zip_info["Zipcode_inf_avail"] , [] , 1 , 0)
population = dnf.getNPFromPandas(zip_info["Population"] , [","] , 20000 , 0)
median_age = dnf.getNPFromPandas(zip_info["Median_Age"], [] , 37 , 0)
education = dnf.getNPFromPandas(zip_info["Education"], ["%"] , 100 , 0)
median_income = dnf.getNPFromPandas(zip_info["Median_Income"], [","] , 45000 , 0)
immigrants = dnf.getNPFromPandas(zip_info["Immigrants"], [","] , 1500 , 0)
poverty = dnf.getNPFromPandas(zip_info["Poverty"], ["%"] , 100 , 0)

#Get classes from predict array
roles = df["Student Role"].as_matrix()
roles[roles != "Student"] = 0
roles[roles == "Student"] = 1
roles = roles.astype(np.float64)
roles[np.isnan(roles)] = 0

#Create the final array to pass to the model
data = np.vstack([zip_code ,citizen , awa , afh , population , median_age , 
                  education , median_income , immigrants , poverty  ])

data = np.append(data , race.T , axis = 0)
data = np.append(data , gender.T , axis = 0)
data = np.append(data , degree.T , axis = 0)
data = np.append(data , std_seg.T , axis = 0)
data = np.append(data , std_type.T , axis = 0)
data = np.append(data , app_type.T , axis = 0)
data = np.append(data , sourceEnc.T , axis = 0)
roles = np.resize( roles ,(1 , roles.shape[0]))
data = np.append(data , roles , axis = 0)

data = data.T

#Extract the end values
Y = data[ : , -1: ]
X = data[: , :-1]


#We need to train the model first.
#That should be done before running this file to load the object on memory
prediction = model.predict(X)
score_ = prediction * 10
score_ = score_.astype(np.int)
score_ += 1

score = model.evaluate(X, Y, verbose=0)
print(score)

tag = pd.read_csv("../../data/tag.csv" , low_memory=False)
tag["mn_rating1"] = score_ 
tag.to_csv("../../data/tag_mn.csv", sep=',')