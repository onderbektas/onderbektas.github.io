import pandas as pd
import matplotlib.pyplot as plt
  
# initialize list of lists 
data = [['Istanbul', 70], ['Ankara', 73], ['Izmir', 75], ['Antalya', 76], ['Adana', 79], ['Mugla', 80]] 

# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['City', 'Percentage']) 

# Circular Bar Chart With Matplotlib

def circular_bar_chart(colname1, colname2, data, size = 0.1):
    fig, ax = plt.subplots(figsize=(8,8))    
    rows, cols = df.shape
    for ii in range(rows):  
        ax.pie([df[colname2].iloc[ii],100 - df[colname2].iloc[ii]], radius=1-ii*size, colors=['teal','white'], 
               rotatelabels=True, wedgeprops=dict(width=size, edgecolor='w'), startangle=90 ,counterclock=False)
        ax.text(-0.25, 1-(2*ii+1)*size/2, df[colname1].iloc[ii]+'  '+str(df[colname2].iloc[ii])+' %', horizontalalignment='center', 
                verticalalignment='center', fontsize=12)
        ax.set(aspect="equal", title='')
        
circular_bar_chart('City','Percentage', df)