import pandas as pd 
import numpy as np
import data_type_model as dtm

df = pd.read_csv("../../data/predict.csv" , low_memory=False)
zip_codes = pd.read_csv("../../data/zip_info.csv" , low_memory=False , encoding = "latin1" , dtype=str)

#Create data encoder class
denc = dtm.dataTypeEncoder();
zip_colnames = ['Zipcode_inf_avail' , 'Population' , 'Median_Age' , 
                'Education' ,'Median_Income' ,'Immigrants' ,'Poverty']
zip_info = denc.getZipInfo(df["Contact_Postal_Code"] , 
                           zip_codes , range(0 , len(df)) , zip_colnames)

