# library
import matplotlib.pyplot as plt
import numpy as np

fig , ax = plt.subplots(figsize=(7,7))
 
# create data (In this demo it is ercentage)
size1=[42,58] 

textLabel = 'Instagram' + ' \n' + str(size1[0]) + ' %'

# Create a circle for the center of the plot
my_circle=plt.Circle( (0,0), 0.85, color='white')

# Create Circular Gauge Plot

ax.pie(size1, colors=['teal','lightgray'], counterclock=False, startangle=90)
ax.text(0, 0, textLabel, horizontalalignment='center', 
        verticalalignment='center', fontsize=30)
ax=plt.gcf()
ax.gca().add_artist(my_circle)

# Show The Circular Gauge Plot
plt.show()