import numpy as np
import re
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


#getUniqueList takes a list of elements that contains multiple entries on each
#row, extracts each entry from each row, and places them in a list 
#Returns set of all entries available
#Array matrix of the elemts to split
#seperator used to split the entries
def getUniqueList(array , seperator):
    returnSet = set()
    for row in array:
        row = str(row)
        row = row.lower()
        #List of charachters to remove. This will combine different writtings 
        #of the same word
        regReplace = r',|_|-|–| |/|[0-9]|march|nov|dec|\.|al|spring|summer|interested'
        row = re.sub( regReplace , "" , row)
        tokens = row.split(seperator)
        returnSet = returnSet.union(tokens)
    return returnSet

#getSourceEncoding Returns encoding array activated for each entry present in 
#each row
#EX : row school;dual will return the following
# school pool event dual
#   1     0     0    1
#setObg Set off all possible entries
#Applicant source array
#seperator used to split the entries
def getSourceEncoding(setObj , array , seperator):
    #Create return array dimensions
    sourceArr = array.as_matrix();
    returnArr = np.zeros((sourceArr.shape[0] , len(setObj)) )
    #Create hashmap to map index
    hashMap = dict.fromkeys(setObj , 0)
    #loop over the hash map to set the value as a unique index to be used in 
    #the returnArr
    i = 0
    for key in setObj:
        hashMap[key] = i
        i += 1
        
    #loop over the applicant source array
    #For each row, extract each entry
    #Activate the correct entries for that entry in the returnArray
    
    for idx,row in enumerate(sourceArr):
        row = str(row)
        row = row.lower()
        #List of charachters to remove. This will combine different writtings 
        #of the same word
        regReplace = r',|_|-|–| |/|[0-9]|march|nov|dec|\.|al|spring|summer|interested'
        row = re.sub( regReplace , "" , row)
        tokens = row.split(seperator)
        #Loop over the tokens to activate the correct hash map 
        for tok in tokens:
            #Get the index of the token from the hashmap
            hashIdx = hashMap[tok]
            #Activate the matched values
            returnArr[idx , hashIdx] = 1

    return returnArr.astype(np.float64)