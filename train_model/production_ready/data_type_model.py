# -*- coding: utf-8 -*-
import numpy as np
import re
import pandas as pd 

class dataTypeEncoder:
    
    std_type_ = ['High School Student','Transfer',
                 'High School Student;New First Time','Readmit','Guest',
                 'Continuing','New Program','Returning','Non-Credit',
                 'New Degree','Between Regions','Transient']
    race_ = ['Multi-racial','White','Black or African American',
                'Asian','American Indian or Alaska Native',
                'Native Hawaiian or Other Pacific Islander',
                'Hispanic or Latino']
    gender_ = ['Male', 'Female', 'Other']
    degree_ = ['Courses Only','Associate of General Studies',
                  'Associate of Applied Science','Indiana College Network',
                  'Associate of Science','Technical Certificate',
                  'Associate of Arts','Associate of Fine Arts']
    std_seg_ = ['ASAP','21st Century Scholar','Career Pathways',
                '4-YR Pathways','Returning Students','Achieve your Degree',
                '4 Year Deferral','4 year deferral','Future Applicant']
    app_type_ = ['Dual Credit','Transfer-Previous College',
                 'First Time Attend','Readmit','Guest','High School Student',
                 'Continuing New Degree','Continuing New Program',
                 'Additional Ivy Tech Degree','Internal Transfer-Regions',
                 'Non Credit/Continuing Ed','Transient-Do not use for Guest',
                 'Do not use']
    
    source_ = ['aged', 'agedprospect','berryplastics','bridgeback','ducredit',
               'educationfair','emberlist','ffaseniors','flin','flto','iche',
               'ichecomplete','isir','isu','itttech','iupui','iusb',
               'millerbrooksrfi','nacac','nan','next','openhouse',
               'purduencentr','radioad','recruiterimport','recruiterrfi','sat',
               'specirfitest','statewideenrolledscholarrosterfromcohort',
               'stcentury','stcenturylistjan','stopoutlist','straighttoapprfi',
               'taa','techday','webrfi']
    
    #encodeArray returns an encoded on hot array based on the train model
    #New entries will be encoded as the deault value
    #Array to encode
    #arrDict to keep the mapping consistent
    #Default value
    def encodeArray( self , array , arrDict , default):
        array = array.as_matrix()
        dictMap = self.getDict(arrDict)
        returnArr = np.zeros((len(array) , len(dictMap) ))
        for i,key in enumerate(array):
            key = str(key)
            idx = default
            if key in dictMap:
                idx = key                
            if idx in dictMap:
                returnArr[ i , dictMap[idx]] = 1
            
        return returnArr
    
    #Returns dict for mapping indexs
    #Loops over the keys, and assign them each a unique index.
    #Index will be consistant, and will assure the same shape of the array
    #regradelss of missing data
    def getDict(self , keys):
        hashMap = dict.fromkeys( keys , 0)
        i = 0
        for key in hashMap:
            hashMap[key] = i
            i += 1
        return hashMap
    
    
    
    def getSourceEncoding(self , array , arrDict , default, seperator):
        #Create return array dimensions
        sourceArr = array.as_matrix()
        returnArr = np.zeros((sourceArr.shape[0] , len(self.source_)) )
        #Create hashmap to map index
        dictMap = self.getDict(arrDict)
            
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
                hashIdx = dictMap[tok]
                #Activate the matched values
                returnArr[idx , hashIdx] = 1
    
        return returnArr.astype(np.float64)
    
    def getZipInfo(self , zips , info , index , columns):
        #Create empy data frame
        df =  pd.DataFrame("0" , index , columns)
        zips = zips.as_matrix()
        #Keep the first 5 numbers of the zip code only
        zips = [str(x)[0:5] for x in zips]
        #If the zip code is found, fill in the needed info
        #Else, keep everything as 0
        for idx, key in enumerate(zips):
            if key in info.zip.values:
                rez = info[info["zip"] == key ] 
                df['Zipcode_inf_avail'][idx] = 1
                df['Population'][idx] = rez['Census 2010 Total Population'].values[0]
                df['Median_Age'][idx] = rez['Median Age'].values[0]
                df['Education'][idx] = rez['Educational Attainment: Percent high school graduate or higher'].values[0]
                df['Median_Income'][idx] = rez['Median Household Income'].values[0]
                df['Immigrants'][idx] = rez['Foreign Born Population'].values[0]
                df['Poverty'][idx] = rez['Individuals below poverty level'].values[0]
        return df
        