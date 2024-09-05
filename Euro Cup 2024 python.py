#!/usr/bin/env python
# coding: utf-8

# In[15]:


#import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#import the dataset
data= pd.read_csv('euro2024_players.csv')
data.head()


# In[3]:


#Checking the rows and columns in the dataset
data.shape


# In[4]:


#Checking if there are any null values in the dataset
data.isnull().sum()


# In[5]:


#info of the dataset to check the column names, data-types
data.info()


# # Exploratory Data Analysis:-

# In[6]:


#Player with most goals
most_goals_index = data['Goals'].idxmax()
player_most_goals = data.loc[most_goals_index]

print("Player with the most goals:")
print(player_most_goals)


# In[7]:


#Player with most caps
most_caps_index = data['Caps'].idxmax()
player_most_caps = data.loc[most_caps_index,['Name','Caps']]

print("Player with the most caps:")
print(player_most_caps)


# #### So, No surprises there, Cristiano Ronaldo is the most capped player in the Euros 2024 and also the top position in the number of goals scored.

# In[8]:


# Define vertical Bar Graph using matplotlib
foot = data['Foot'].value_counts()
plt.figure(figsize=(10, 6))
foot.plot(kind='bar')
plt.title('Distribution of Player according to their dominant foot')
plt.xlabel('Foot')
plt.ylabel('Number of Players')
plt.show()


# #### Majority of the players are right-footed.

# In[9]:


# Define horizontal Bar Graph using matplotlib
data_grouped = data.groupby('Country').sum().reset_index()
plt.figure(figsize=(10, 15))
goalplot=sns.barplot(x='Goals',y='Country',data = data_grouped)
plt.title('Total Number of Goals Scored by players of a Country ')
plt.xlabel('Number of Goals')
plt.ylabel('Name of Country')
for p in goalplot.patches:
    goalplot.annotate(format(p.get_width(), '.1f'), 
                     (p.get_width(), p.get_y() + p.get_height() / 2.), 
                     ha = 'center', va = 'center', 
                     xytext = (20, 0), 
                     textcoords = 'offset points')

plt.show()


# #### Players of Portugal as a collective have scored the highest number of goals for their country. Albania ranks last with 40.

# In[10]:


# Define horizontal Bar Graph using matplotlib
plt.figure(figsize=(10, 15))
goalplot2=sns.barplot(x='MarketValue',y='Country',data = data_grouped)
plt.title('Total MarketValue of Players of a Country')
plt.xlabel('Total Market Value')
plt.ylabel('Name of Country')
for p in goalplot2.patches:
    goalplot2.annotate(format(p.get_width(), '.1f'), 
                     (p.get_width(), p.get_y() + p.get_height() / 2.), 
                     ha = 'center', va = 'center', 
                     xytext = (20, 0), 
                     textcoords = 'offset points')

plt.show()


# #### The Dataset unfortunately doesnot specify any particular currency so we will just call it units. English players have the highest combined Market Value with total exceeding 1.5 billion units.

# In[11]:


#Player with highest Market Value
most_mv_index = data['MarketValue'].idxmax()
player_max_value = data.loc[most_caps_index,['Name','MarketValue']]

print("Player with the highest Market Value:")
print(player_max_value)


# In[12]:


data_group = data.groupby('Club').sum().reset_index()
top_10_clubs = data_group.sort_values(by='MarketValue', ascending=False).head(10)


# In[14]:


# Define horizontal Bar Graph using matplotlib
plt.figure(figsize=(10, 5))
sns.barplot(x='MarketValue',y='Club',data = top_10_clubs)
plt.title('Total Market Value of Players in a club (Top 10)')
plt.xlabel('Total Market Value')
plt.ylabel('Name of Clubs')
plt.show()


# #### This notebook is made to help people get started, quite a few more comparisons and plots can be done. Hope this helps!!!

# In[18]:


#checking duplicate values  
data= pd.read_csv('euro2024_players.csv')
data.nunique()


# In[19]:


# describing the data 
data.describe() 


# In[20]:


#column to list  
data.columns.tolist()


# In[33]:


# Assuming 'data' is your DataFrame 
Goals_counts = data['Goals'].value_counts() 
  
# Using Matplotlib to create a count plot 
plt.figure(figsize=(50,30)) 
plt.bar(Goals_counts.index, Goals_counts, color='pink') 
plt.title('Count Plot of Goals') 
plt.xlabel('Goals') 
plt.ylabel('Country') 
plt.show() 


# In[34]:


# Assuming 'data' is your DataFrame 
Caps_counts = data['Caps'].value_counts() 
  
# Using Matplotlib to create a count plot 
plt.figure(figsize=(50,30)) 
plt.bar(Caps_counts.index, Caps_counts, color='Blue') 
plt.title('Count Plot of Caps') 
plt.xlabel('Caps') 
plt.ylabel('Country') 
plt.show() 


# In[41]:


# Set Seaborn style 
sns.set_style("darkgrid") 
 
# Identify numerical columns 
numerical_columns = data.select_dtypes(include=["int64", "float64"]).columns 
 
# Plot distribution of each numerical feature 
plt.figure(figsize=(14, len(numerical_columns) * 3)) 
for idx, feature in enumerate(numerical_columns, 1): 
   plt.subplot(len(numerical_columns), 2, idx) 
   sns.histplot(data[feature], kde=True) 
   plt.title(f"{feature} | Skewness: {round(data[feature].skew(), 2)}") 
 
# Adjust layout and show plots 
plt.tight_layout() 
plt.show() 


# In[51]:


# Set the color palette 
sns.set_palette("Pastel1") 
  
# Assuming 'data' is your DataFrame 
plt.figure(figsize=(10, 6)) 
  
# Using Seaborn to create a pair plot with the specified color palette 
sns.pairplot(data) 
  
plt.suptitle('Pair Plot for DataFrame') 
plt.show() 


# In[68]:


# Pie Charts using Matplotlib in Python
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
# Mesurment of Age of the following Players.
x = np.array([24,28,32,34,38])
mylabels = ["Nico Schlotterbeck","Jonathan Tah","Marc-André ter Stegen","Nico Schlotterbeck","Nico Schlotterbeck"]
plt.pie(x, labels = mylabels)
plt.show()


# In[72]:


# Pie Charts using Matplotlib in Python
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
# Define win rates of following countries.
labels = ('France','Germany','Portugal','Spain','England')
sizes = ([30,55,25,10,20])
plt.pie(sizes, labels = labels, autopct = '%1.f%%', counterclock = False)
#Display th figure
plt.show()


# In[101]:


#Line Charts using Matplotlib in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig, ax1 = plt.subplots()
Countries = ['spain','Germany','France','Portugal','England']
Foot = [10,50,30,40,20]
Goals = [5,1,7,8,3]
Caps = [110,125,106,101,122]


ax1.plot(Countries,Foot,color = "red")
ax2 = ax1.twinx()
ax2.plot(Countries,Goals,color = "blue")
ax3 = ax1.twinx()
ax3.plot(Countries,Caps,color = "green")
#ax3.spines['right'].set_position(('outward',60))
ax3.spines['right'].set_position(('axes',1.15))

ax1.set_ylabel("Foot",color="red")
ax2.set_ylabel("Goals",color="blue")
ax3.set_ylabel("Caps",color="green")

ax1.tick_params(axis='y',colors = "red")
ax2.tick_params(axis='y',colors = "blue")
ax3.tick_params(axis='y',colors = "green")

ax2.spines['left'].set_color("red")
ax3.spines['right'].set_color("blue")
ax3.spines['right'].set_color("green")

plt.show()

#fig.tight_layout()
fig.savefig("3-axis-v2.png",bbox_inches='tight')


# In[1]:


# Scatterplot using Seaborn in Python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
Countries_data = pd.read_csv('euro2024_players.csv')

sns.scatterplot(x = Countries_data['Caps'], y = Countries_data['Goals'], hue = Countries_data['Foot'])


# In[110]:


# Boxplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
data = pd.read_csv('euro2024_players.csv')
data = pd.DataFrame(np.random.rand(10,5), columns =['A','B','C','D','E'])
data.plot.box(grid='True')


# In[113]:


# Boxplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv('euro2024_players.csv')
data.head()



# In[118]:


# Boxplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv('euro2024_players.csv')
sns.boxplot(data["Caps"])


# In[119]:


data.describe()


# In[127]:


# Boxplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
Countries_data = pd.read_csv('euro2024_players.csv')
sns.boxplot(x = "Age", y = "Height", data= Countries_data)


# In[30]:


# Define Comperison Box plot using seaborn in Python
plt.figure(figsize=(30,10))
sns.boxplot(x = "Country", y = "Goals",data = Countries_data)


# In[31]:


# Barplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

Countries_data = pd.read_csv('euro2024_players.csv')
sns.barplot(x = "Age", y = "Height", data= Countries_data)


# In[8]:


# Barplot using seaborn in Python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

plt.figure(figsize=(30,10))
Countries_data = pd.read_csv('euro2024_players.csv')
sns.barplot(x = "Country", y = "Goals", data= Countries_data)


# In[12]:


# Define Comperison Bar graph using seaborn in Python
plt.figure(figsize = (15,5))

sns.barplot( x = 'Age',y = 'Goals', hue = "Country", data= Countries_data )


# In[13]:


# Comparison Pie Charts using in python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Countries_data = pd.read_csv('euro2024_players.csv')
Countries_data = {"Countries":['France','Germany','Portugal','Spain','England'],
                 "Goals":[15,8,18,10,5]}
data = pd.DataFrame(Countries_data)
data


# In[28]:


# Define Comperison Pie chart using matplotlib in Python
plt.pie(data['Goals'],labels=data['Countries'] ,autopct='%1.2f%%',explode=(0,0,0.2,0,0.15),shadow=True)
plt.title('Goal Percentage of every Country')


# 

# In[28]:


#import the liberies 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 


# In[6]:


# import the dataset
data= pd.read_csv('euro2024_players.csv')
data


# In[8]:


# import the first five data from the entire dataset
data.head(5)


# In[9]:


# import the last fine data from the entire dataset
data.tail(5)


# In[10]:


# Define information about the entire dataset
data.info()


# In[11]:


# Define Description of entire dataset
data.describe().T


# In[13]:


# Define T-plot using Bar Graph
data.describe().T.plot(kind='bar')


# In[15]:


# Checking the duplicate value into dataset
data.duplicated().sum()


# In[19]:


# Define Correlation Matrix using Seaborn in Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

numeric_cols = data.select_dtypes(include=np.number).columns                                         
plt.figure(figsize=(12, 8))
sns.heatmap(data[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[20]:


# import column by using Python
data.columns.to_list()


# In[22]:


# Most Successful Goal Keeper 
least_goals_index = data['Goals'].idxmin()


player_least_goals = data.loc[least_goals_index]

print("Player with the least goals:")
print(player_least_goals)


# In[23]:


# Define vertical Bar Graph using matplotlib 
data_grouped = data.groupby('Country').sum().reset_index()
plt.figure(figsize=(15, 10))                                             
goalplot = sns.barplot(x='Country', y='Goals', data=data_grouped)
plt.title('Total Number of Goals Scored by Players of a Country')
plt.xlabel('Name of Country')
plt.ylabel('Number of Goals')

for p in goalplot.patches:
    goalplot.annotate(format(p.get_height(), '.1f'), 
                      (p.get_x() + p.get_width() / 2., p.get_height()), 
                      ha='center', va='center', 
                      xytext=(0, 10), 
                      textcoords='offset points')

plt.xticks(rotation=90)
plt.show()  


# In[24]:


# Define vertical Bar Graph using matplotlib 
data_grouped = data.groupby('Country').sum().reset_index()
plt.figure(figsize=(15, 10))


goalplot2 = sns.barplot(x='Country', y='MarketValue', data=data_grouped)
plt.title('Total Market Value of Players by Country')
plt.xlabel('Country')
plt.ylabel('Total Market Value')


for p in goalplot2.patches:
    goalplot2.annotate(format(p.get_height(), '.1f'), 
                       (p.get_x() + p.get_width() / 2., p.get_height()), 
                       ha='center', va='center', 
                       xytext=(0, 10), textcoords='offset points')


plt.xticks(rotation=90)  
plt.show()


# In[25]:


# Define horizontal Bar Graph using matplotlib 
data_group = data.groupby('Club').sum().reset_index()
top_10_clubs = data_group.sort_values(by='MarketValue', ascending=False).head(10)
plt.figure(figsize=(10, 15))
sns.barplot(x='MarketValue',y='Club',data = top_10_clubs)
plt.title('Total Market Value of Players in a club (Top 10)')
plt.xlabel('Total Market Value')
plt.ylabel('Name of Clubs')
plt.show()


# In[1]:


# import different types of Bar graphs using Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly import express

data= pd.read_csv('euro2024_players.csv')
for column in ['Name',
 'Position',
 'Age',
 'Club',
 'Height',
 'Foot',
 'Caps',
 'Goals',
 'MarketValue',
 'Country']:
    express.histogram(data_frame=data, x=column).show()
    


# In[ ]:





# In[27]:


# import different types of Bar graphs using Python
data.hist(bins = 20, figsize = (20,20), color = 'green')
plt.show()


# ![](WorldCloud.png)

# ![title](WordCloud.png)

# 

# In[13]:


# from IPython.display import Image
Image(filename="Euro cup 2024.py.jpg",width=1000,height=400)


# # THANK YOU SO MUCH !!!!!

# 
