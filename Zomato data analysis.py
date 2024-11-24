import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # type: ignore


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe)


# convert datatype column - rate
def handleRate(value):
    value = str(value).split('/')
    value= value[0];
    return float(value)
    
dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head()) 


dataframe.info()

dataframe.head()


# most order genrate from dining
sns.countplot(x= dataframe['listed_in(type)'])
plt.xlabel("type of resturant")



 
 
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.title ("Resturant votes")
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="red", size=15)
plt.ylabel("Votes", c="red", size=15)
plt.show()

# conclusion  : dinning resturants has received maximum votes


plt.hist(dataframe['rate'] , bins= 5)
plt.title ("rating distribution")
plt.show()
# conclusion - the majority resturants received ratings from 3.5 to 4


data=dataframe['approx_cost(for two people)']
sns.countplot(x=data) 


# # conclusion - majority couples spend 300 rs


plt.figure(figsize=(6,6))  
sns.boxplot (x='online_order' , y='rate' , data = dataframe)


# Create the pivot table
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)

# Create the heatmap
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')

# Add titles and labels
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")

# Display the plot
plt.show()