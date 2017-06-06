zip_codes <- read.csv("PATH/zip_info.csv")
unique_zips <- unique(data$Contact_Postal)
unique_zips <- data$Contact_Postal[which(formated$Zipcode_inf_avail == "NULL")]

formated$Zipcode_inf_avail <- as.character(formated$Zipcode_inf_avail)
formated$Population <- as.character(formated$Population)
formated$Median_Age <- as.character(formated$Median_Age)
formated$Median_Income <- as.character(formated$Median_Income)
formated$Education <- as.character(formated$Education)
formated$Immigrants <- as.character(formated$Immigrants)
formated$Poverty <- as.character(formated$Poverty)

count <- 0

for( i in unique_zips){
  print(count)
  count <- count + 1
  if(i %in% zip_codes$zip){
    zip_index <- which(zip_codes$zip == i)
    logic_tree <- data$Contact_Postal == i
    formated$Zipcode_inf_avail[logic_tree] <- as.character("1")
    formated$Population[logic_tree] <- as.character(zip_codes$Census.2010.Total.Population[zip_index])
    formated$Median_Age[logic_tree] <- as.character(zip_codes$Median.Age[zip_index])
    formated$Median_Income[logic_tree] <- as.character(zip_codes$Median.Household.Income[zip_index])
    formated$Education[logic_tree] <- as.character(zip_codes$Educational.Attainment..Percent.high.school.graduate.or.higher[zip_index])
    formated$Immigrants[logic_tree] <- as.character(zip_codes$Foreign.Born.Population[zip_index])
    formated$Poverty[logic_tree] <- as.character(zip_codes$Individuals.below.poverty.level[zip_index])
    
  }else{
    logic_tree <- data$Contact_Postal == i
    formated$Zipcode_inf_avail[logic_tree] <- as.character("0")
    formated$Population[logic_tree] <- as.character("0")
    formated$Median_Age[logic_tree] <- as.character("0")
    formated$Median_Income[logic_tree] <- as.character("0")
    formated$Education[logic_tree] <- as.character("0")
    formated$Immigrants[logic_tree] <- as.character("0")
    formated$Poverty[logic_tree] <- as.character("0")
  }
}
