Notes Jun 12 2017
================

### Test 1

#### Neural Network shape
1. 99 Dense activation: relu input: 99
2. 25 Dense activation: relu
3. 25 Dense activation: relu
4. 25 Dense activation: relu
5. 1 Dense activation: sigmoid

#### Data used
1. Is zip code available
2. Is citizen
3. Age when applies
4. Age when finished high school
5. Race
6. Gender
7. Degree
8. Student type
9. Student segment
10. Applicant Type
11. Source of student info
12. Zip info:
    1. Population
    2. Median Age
    3. Education
    4. Median Income
    5. Immigrants
    6. Poverty


#### Results
* **Accuracy**: 0.87567337538919809
* **Fscore**: 0.903643862937
* **Loss**: 0.08402949282583369

____

### Test 2

##### Removed zip code information to test its usefulness

#### Neural Network shape
1. 92 Dense activation: relu input: 92
2. 25 Dense activation: relu
3. 25 Dense activation: relu
4. 25 Dense activation: relu
5. 1 Dense activation: sigmoid

#### Data used
1. Is zip code available
2. Is citizen
3. Age when applies
4. Age when finished high school
5. Race
6. Gender
7. Degree
8. Student type
9. Student segment
10. Applicant Type
11. Source of student info


#### Results
* **Accuracy**: 0.86451386803559882
* **Fscore**: 0.896186099326
* **Loss**: 0.088665593797987233

____

### Test 3

##### Removed age related information to test its usefulness

#### Neural Network shape
1. 97 Dense activation: relu input: 97
2. 25 Dense activation: relu
3. 25 Dense activation: relu
4. 25 Dense activation: relu
5. 1 Dense activation: sigmoid

#### Data used
1. Is zip code available
2. Is citizen
3. Race
4. Gender
5. Degree
6. Student type
7. Student segment
8. Applicant Type
9. Source of student info
10. Zip info:
    1. Population
    2. Median Age
    3. Education
    4. Median Income
    5. Immigrants
    6. Poverty


#### Results
* **Accuracy**: 0.87578852509215654
* **Fscore**: 0.90462094418
* **Loss**: 0.084864992523552646

____

### Test 4

##### Removed age gender and race 

#### Neural Network shape
1. 87 Dense activation: relu input: 87
2. 25 Dense activation: relu
3. 25 Dense activation: relu
4. 25 Dense activation: relu
5. 1 Dense activation: sigmoid

#### Data used
1. Is zip code available
2. Is citizen
3. Degree
4. Student type
5. Student segment
6. Applicant Type
7. Source of student info
8. Zip info:
   1. Population
   2. Median Age
   3. Education
   4. Median Income
   5. Immigrants
   6. Poverty


#### Results
* **Accuracy**: 0.87484229498825306
* **Fscore**: 0.903428427945
* **Loss**: 0.085151130160725466

___

### Test 5

#### Keep only zipcode info

#### Neural Network shape
1. 8 Dense activation: relu input: 8
2. 25 Dense activation: relu
3. 25 Dense activation: relu
4. 25 Dense activation: relu
5. 1 Dense activation: sigmoid

#### Data used
1. Is zip code available
2. Zip info:
   1. Population
   2. Median Age
   3. Education
   4. Median Income
   5. Immigrants
   6. Poverty


#### Results
* **Accuracy**: 0.61530990288089771
* **Fscore**: 0.750936766632
* **Loss**: 0.23592530873023057