import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("covid19.csv")#read the real world data
print("COVID-19 Data Analysis: Confirmed, Deaths, and Recovered cases by Country\n")
if data.isnull().sum().sum()!=0 :
 data.dropna(inplace=True) #remove null values

print("\nthe head value of the data for knowing the table:")

print(data.head()) #provides the first 5 data from the table

print("\nthe Summary of the table:")

data.info() #provides overall summary of the table i.e. num of rows,cols, data type of rows also it prints by default

print("\nthe statistical summary of the table:")

print(data.describe()) #provides the necessary statistics i.e. mean,median,standard deviation of the table

print("\nthe total number of confirmed cases from the highest to lowest(only top 10 data by the countries)")

total_conf = data.groupby('Country/Region')['Confirmed'].max().sort_values(ascending=False) #top confirmed cases according to country/region 

print(total_conf.head(10))

print("\nthe total number of confirmed deaths from the highest to lowest(only top 10 data by the countries)")

total_deaths  =data.groupby('Country/Region')['Deaths'].max().sort_values(ascending=False) #top death cases according to country/region 

print(total_deaths.head(10))

total_rec = data.groupby('Country/Region')['Recovered'].max().sort_values(ascending=False)#top recovered cases according to country/region 

print(total_rec.head(10))

#plots the given data in a bar graph(for confirmed cases)
plt.figure(figsize=(10, 6))
total_conf.head(10).plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Countries by Confirmed COVID-19 Cases')
plt.ylabel('Confirmed Cases')
plt.xlabel('Country/Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#plots the given data in a bar graph(for death cases)
plt.figure(figsize=(10,6))
total_deaths.head(10).plot(kind='bar',color='red',edgecolor='black')
plt.title('Top 10 Countries by DEATHs COVID-19 Cases')
plt.ylabel('Death cases')
plt.xlabel('Country/Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#plots the given data in a bar graph(for recovered cases)
plt.figure(figsize=(10,6))
total_rec.head(10).plot(kind='bar',color='green',edgecolor='black')
plt.title('Top 10 Countries by Recovered COVID-19 Cases')
plt.ylabel('Recovered cases')
plt.xlabel('Country/Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
total_conf.to_csv('top_confirmed.csv')
total_deaths.to_csv('top_deaths.csv')
total_rec.to_csv('top_recovered.csv')

# Dataset source: https://www.kaggle.com/datasets/imdevskp/corona-virus-report
