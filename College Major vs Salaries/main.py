import os
import pandas as pd

# Folder where the script is located
script_dir = os.path.dirname(__file__)

# CSV file name
csv_file_name = "salaries_by_college_major.csv"

# Full path to the CSV file
csv_path = os.path.join(script_dir, csv_file_name)

# Check if the file exists
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV file not found at: {csv_path}")

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# to understand the structure of the data, we can use the .head() method to display the first few rows, and other methods to get more information about the dataset. like .info(), .columns, and .shape.

#now we can check the df.isna() to see if there are any missing values in the dataset. If there are, we can decide how to handle them, such as dropping rows with missing values or filling them with a specific value.

#and we can use df.tail() to see the last few rows of the dataset to get a sense of the data at the end of the DataFrame.

# when we used print (df.tail()) method, we observed that the last row contained summary statistics rather than actual data about a college major. To ensure our analysis focuses solely on relevant data, we decided to remove this last row from the DataFrame. This step helps maintain the integrity of our analysis by excluding non-essential information.

clean_df = df.dropna()

#***************************************************************
#______________How to remove NaN values______________
#***************************************************************

# here we used df.dropna() 

# method to remove the last row because we knew that the last row was the only row with missing values. In a more general case, if there were multiple rows with missing values, we would need to investigate further to determine the best approach for handling them, which could include filling in missing values or removing multiple rows.

# we could of also used df.iloc[:-1] to remove the last row specifically without relying on the presence of NaN values.

#***************************************************************
#______________finding index of row for highest starting median salary______________
#***************************************************************

# by print(clean_df ['Starting Median Salary'].idxmax())

# we can find the index of the row with the highest starting median salary. This allows us to identify which college major offers the best starting salary for graduates.

# then with print(clean_df['Undergraduate Major'][43]) we can find the name of the major associated with that index. In this case, it tells us that the major with the highest starting median salary is "Physician Assistant".

#***************************************************************
#______________presenting highest median salary for mid-career professionals______________
#***************************************************************

#print(clean_df['Mid-Career Median Salary'].max())
#print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
#print(clean_df['Undergraduate Major'][8])

# these three lines of code help us identify the college major that offers the highest median salary for mid-career professionals.

#***************************************************************
#______________how to find the lowest risk majors______________
#***************************************************************

#spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
#clean_df.insert(1, 'Spread', spread_col)
#low_risk_majors = clean_df.nsmallest(5, 'Spread')
#print(low_risk_majors[['Undergraduate Major', 'Spread']])

# this code calculates the salary spread for each major by subtracting the 10th percentile salary from the 90th percentile salary. It then adds this information as a new column called 'Spread' to the DataFrame. Finally, it identifies and displays the five majors with the smallest salary spreads, indicating lower risk in terms of salary variability.  


#***************************************************************
#______________how to find the highest potential majors______________
#***************************************************************

#highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
#highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

# this code sorts the DataFrame based on the 'Mid-Career 90th Percentile Salary' in descending order, allowing us to identify the majors with the highest earning potential for mid-career professionals. It then displays the top entries, showing both the major and its corresponding 90th percentile salary.

#***************************************************************
#______________how to find the greateset spread in salaries______________
#***************************************************************


#highest_spread = clean_df.sort_values('Spread', ascending=False)
#highest_spread[['Undergraduate Major', 'Spread']].head()

# this code sorts the DataFrame based on the 'Spread' column in descending order, allowing us to identify the majors with the highest salary variability. It then displays the top entries, showing both the major and its corresponding salary spread.


#***************************************************************
#______________grouping and pivoting data______________
#***************************************************************


#clean_df.groupby('Group').count()
#(clean_df.groupby('Group').mean())
#pd.options.display.float_format = '{:,.2f}'.format 

# this code groups the DataFrame by the 'Group' column and counts the number of majors in each group. It also calculates the mean values for each group, providing insights into the average salaries and other statistics for different categories of majors. The last line formats the display of floating-point numbers to two decimal places for better readability.