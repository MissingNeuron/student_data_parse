library("lubridate")
formated <- read.csv("C:/Users/Max/Desktop/students_data/complete/final.csv" , colClasses = rep('character', 29))

modelReady <- as.data.frame(matrix(data="0" , nrow=665798 , ncol =1))
colnames(modelReady) <- c("email")

modelReady$email<- formated$Email != "NULL"
modelReady$email[modelReady$email == TRUE] <- 1
modelReady$email[modelReady$email == FALSE] <- 0

age <- formated$Age
modelReady$age <- formated$Age


stage <- formated$Stage
stage[is.na(stage)] <- "NULL"
stage <- data.frame(stage = stage , stringsAsFactors = T)
stage <- as.data.frame(model.matrix(~stage + 0   , stage))

race <- formated$Race
race[is.na(race)] <- "NULL"
race <- data.frame(race = race , stringsAsFactors = T)
race <- as.data.frame(model.matrix(~race + 0   , race))

ethnicity <- formated$Ethnicity
ethnicity[is.na(ethnicity)] <- "NULL"
ethnicity <- data.frame(ethnicity = ethnicity , stringsAsFactors = T)
ethnicity <- as.data.frame(model.matrix(~ethnicity + 0 , ethnicity))


gender <- formated$Gender
gender[is.na(gender)] <- "NULL"
gender <- data.frame(gender = gender , stringsAsFactors = T)
gender <- as.data.frame(model.matrix(~gender + 0 , gender))


modelReady$Citizenship_Flag<- formated$Citizenship_Flag 
modelReady$Citizenship_Flag[modelReady$Citizenship_Flag == TRUE] <- 1
modelReady$Citizenship_Flag[modelReady$Citizenship_Flag == FALSE] <- 0
modelReady$Citizenship_Flag[is.na(modelReady$Citizenship_Flag)] <- 0

modelReady$X19<- formated$X19 == "Yes"
modelReady$X19[modelReady$X19 == TRUE] <- 1
modelReady$X19[modelReady$X19 == FALSE] <- 0
modelReady$X19[is.na(modelReady$X19)] <- 0

modelReady$Honors<- formated$American_Honors == "YES"
modelReady$Honors[modelReady$Honors == TRUE] <- 1
modelReady$Honors[modelReady$Honors == FALSE] <- 0
modelReady$Honors[is.na(modelReady$Honors)] <- 0

hs_year <- formated$HS_Year
hs_year[is.na(hs_year)] <- "NULL"
hs_year <- data.frame(hs_year = hs_year , stringsAsFactors = T)
hs_year <- as.data.frame(model.matrix(~hs_year + 0 , hs_year))

age_finished <- formated$Age_Finished_HS
age_finished[is.na(age_finished)] <- "NULL"
age_finished <- data.frame(age_finished_hs = age_finished , stringsAsFactors = T)
age_finished <- as.data.frame(model.matrix(~age_finished_hs + 0 , age_finished))

degree <- formated$Degree
degree[is.na(degree)] <- "NULL"
degree <- data.frame(degree = degree , stringsAsFactors = T)
degree <- as.data.frame(model.matrix(~degree + 0 , degree))

type <- formated$Student_Type
type[is.na(type)] <- "NULL"
type <- data.frame(type = type , stringsAsFactors = T)
type <- as.data.frame(model.matrix(~type + 0 , type))

segment <- formated$Student_Segment
segment[is.na(segment)] <- "NULL"
segment <- data.frame(segment = segment , stringsAsFactors = T)
segment <- as.data.frame(model.matrix(~segment + 0 , segment))

applicant_type <- formated$Applicant_Type
applicant_type[is.na(applicant_type)] <- "NULL"
applicant_type <- data.frame(applicant_type = applicant_type , stringsAsFactors = T)
applicant_type <- as.data.frame(model.matrix(~applicant_type + 0 , applicant_type))

#source <- formated$Source
#source[is.na(source)] <- "NULL"
#source <- data.frame(source = source , stringsAsFactors = T)
#source <- as.data.frame(model.matrix(~source + 0 , source))

#lead_source <- formated$Lead_Source
#lead_source[is.na(lead_source)] <- "NULL"
#lead_source <- data.frame(lead_source = lead_source , stringsAsFactors = T)
#lead_source <- as.data.frame(model.matrix(~lead_source + 0 , lead_source))

#event_name <- formated$Event_Name
#event_name[is.na(event_name)] <- "NULL"
#event_name <- data.frame(event_name = event_name , stringsAsFactors = T)
#event_name <- as.data.frame(model.matrix(~event_name + 0 , event_name))

modelReady <- cbind(modelReady , stage , race , ethnicity , gender , hs_year , age_finished , degree , type , segment , applicant_type )

modelReady$zip_avail<- formated$Zipcode_inf_avail
modelReady$Population<- formated$Population
modelReady$Poverty<- formated$Poverty
modelReady$Median_Age<- formated$Median_Age
modelReady$Median_Income<- formated$Median_Income
modelReady$Education<- formated$Education
modelReady$Immigrants<- formated$Immigrants

Y <- formated$Role
Y[is.na(Y)] <- "NULL"
Y <- data.frame(Y = Y , stringsAsFactors = T)
Y <- as.data.frame(model.matrix(~Y + 0 , Y))

modelReady <- cbind(modelReady , Y)
