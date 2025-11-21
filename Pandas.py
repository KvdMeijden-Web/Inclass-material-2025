import pandas

#Read the CSV file
dataframe = pandas.read_csv("grade.csv")

#Calculate the average grade for each student and add it as a new column
avarage_grade = dataframe[["Math","Science","English"]].mean(axis=1)
dataframe["Avarage"] = avarage_grade
print(dataframe)