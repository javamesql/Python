#Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
#The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame: 
    columns = ['student_id', 'age']
    result = pd.DataFrame(student_data, columns=columns)
    return result

#Write a solution to calculate and display the number of rows and columns of players.
#Return the result as an array: [number of rows, number of columns]
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

#Write a solution to display the first 3 rows of this DataFrame.
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

#Write a solution to select the name and age of the student with student_id = 101.
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]

#Write a solution to create a new column name "bonus" that contains the doubled values of the salary column.
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees

#Write a solution to remove these duplicate rows and keep only the first occurrence.
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])

#Write a solution to remove the rows with missing values.
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset = ['name'], inplace=True)
    return students

#Write a solution to modify the salary column by multiplying each salary by 2.
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary']*2
    return employees

#Write a solution to rename the columns as follows:
#id to student_id
#first to first_name
#last to last_name
#age to age_in_years
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns={
            'id':'student_id',
            'first':'first_name',
            'last':'last_name',
            'age':'age_in_years',
    })
    return students

#The grade column is stored as floats, convert it to integers.
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

#Write a solution to fill in the missing value as 0 in the quantity column.
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products

#Write a solution to concatenate these two DataFrames vertically into one DataFrame.
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    concatenated_df = pd.concat([df1, df2], ignore_index=True)
    return concatenated_df

#Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot_table(index='month', columns='city', values='temperature', aggfunc='max')

#Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')

#Write a solution to list the names of animals that weigh strictly more than 100 kilograms.
#Return the animals sorted by weight in descending order.
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]












