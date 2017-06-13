import numpy as np
#getNPFromPandas takes a data frame, formates data ,and returns a numpy array
#Array df frame to formate
#split, list of characters to remove from entries
#Value to normalize by
#NanVal, the value to assign nan entries
def getNPFromPandas(array , split , normalize , nanVal):
    returnArr = array.as_matrix()
    #Loop over split list to remove elements from each item
    for rep in split:
        returnArr = np.array(list(map(lambda x:str.replace(str(x)  , rep , "" ) , returnArr )))
    #Transform array to numerical
    returnArr = returnArr.astype(np.float64)
    #Assign nan new value
    returnArr[np.isnan(returnArr)] = nanVal
    #Divide by normalize value
    returnArr /= normalize
    return returnArr
