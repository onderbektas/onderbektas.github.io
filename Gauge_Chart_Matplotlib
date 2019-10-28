# library
import matplotlib.pyplot as plt
import numpy as np
fig , ax = plt.subplots(figsize=(8,8))
 
# create data
size1=[50,10,10,10,10,10]


# Create a circle for the center of the plot
my_circle=plt.Circle( (0,0), 0.85, color='white')

# Give color names
ax.pie([200,1], colors=['white','black'], 
       counterclock=False, startangle=60)
ax.plot(np.linspace(0,0.5,100),np.linspace(0,0.85,100),color='black', linewidth=4)
ax.pie(size1, colors=['white','floralwhite','moccasin','orange','orangered','brown'], 
       counterclock=False, startangle=0)

ax.pie(size1, colors=['white','floralwhite','moccasin','orange','orangered','brown'], 
       counterclock=False, startangle=0)

ax.text(0, -0.1, '70 %', horizontalalignment='center', 
        verticalalignment='center', fontsize=20)

ax=plt.gcf()
ax.gca().add_artist(my_circle)

plt.show()