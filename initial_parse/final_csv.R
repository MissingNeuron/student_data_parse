library(lubridate)

data <- read.csv("C:/Users/Max/Desktop/students_data/complete/complete.csv")

formated <- as.data.frame(matrix(data="NULL" , nrow=665798 , ncol = 30))

colnames(formated) <- c("Email" , "Stage" , "Age" , "Race" , "Ethnicity" , "Gender" , "Citizenship_Flag" , "X19" , "American_Honors" , "HS_Year" , "Age_Finished_HS" , "HS_Info" , "Anticp_Register_Term_Avail" , "Major"  , "Area_Of_Study" , "Degree" , "Student_Segment" , "Student_Type" , "Applicant_Type" , "Source" , "Lead_Source" , "Event_Name" , "Zipcode_inf_avail" , "Population" , "Median_Age" , "Education" , "Median_Income" , "Immigrants" , "Poverty" , "Role")

date_of_Birth <- as.Date(data$Date_of_Birth , "%m/%d/%Y")
created_Time <- as.Date(data$Created_Time , "%m/%d/%Y %H:%M")
hs_year <- as.Date(data$High_School_Graduation_Year , "%Y")

age <- year(created_Time) - year(date_of_Birth)
Age_Finished_HS <- year(hs_year) - year(date_of_Birth)

formated$Email <- data$Email
formated$Stage <- data$Student.Stage
formated$Age <- as.character(age)
formated$Race <- data$Race
formated$Ethnicity <- data$Ethnicity
formated$Gender <- data$Gender
formated$Citizenship_Flag <- data$Citizenship_Flag
formated$X19 <- data$X19_or_older
formated$American_Honors <- data$American_Honors
formated$HS_Year <- as.character(hs_year)
formated$Age_Finished_HS <- as.character(Age_Finished_HS)
formated$HS_Info <- paste( data$Most.Recently.Attended.HS , data$High_School_Name , data$High_School_City , data$High_School_Graduation_Year , data$High_School_State , sep="|")
formated$Anticp_Register_Term <- data$Anticipated_Start_Term
formated$Major <- data$Major
formated$Degree <- data$Degree
formated$Student_Segment <- data$Student_Segment
formated$Student_Type <- data$Student_Type
formated$Applicant_Type <- data$Applicant_Type
formated$Source <- data$Source
formated$Lead_Source <- data$Lead_Source
formated$Event_Name <- data$Event_Name
formated$Role <- data$Student.Role