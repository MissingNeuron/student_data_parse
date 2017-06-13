# -*- coding: utf-8 -*-
import numpy as np

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