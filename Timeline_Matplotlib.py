#!/usr/bin/env python
# coding: utf-8

# In[99]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.pyplot import figure
import pandas as pd

# https://gitlab.rlp.net/-/profile/personal_access_tokens

try:
    # Fetch JSON data
    
    import urllib.request
    import json

    url = "https://raw.githubusercontent.com/MonikaBarget/GeoHumTutorials/master/Historische%20Karten%20Kurmainz.json"
    data = json.loads(urllib.request.urlopen(url, timeout=.4).read().decode())
    
    print("No. of items found: ", len(data))
    
    dates_1650=[]
    dates_1700=[]
    dates_1750=[]
    dates_1800=[]
    dates_new =[]
    names_1650=[]
    names_1700=[]
    names_1750=[]
    names_1800=[]
    
    for item in data:
        date=item['issued']['date-parts']
        #print(date)
        date_str = date[0][0]
        #print(date_str)
        if int(date_str)<=1650:
            dates_1650.append(date_str)
            names_1650.append(item['title'][:20])
        if 1651<=int(date_str)<=1700:
            dates_1700.append(date_str)
            names_1700.append(item['title'][:20])
        if 1701<=int(date_str)<=1750:
            dates_1750.append(date_str)
            names_1750.append(item['title'][:20])
        if 1751<int(date_str)<=1800:
            dates_1800.append(date_str)
            names_1800.append(item['title'][:20])
    
    print("Number of items to be plotted: ", len(dates))

except ValueError:
    print("no data")
    
# split large data sets into several graphs

print(dates_1650)
print(names_1650)
time_range=[dates_1650, dates_1700, dates_1750, dates_1800]
name_range=[names_1650, names_1700, names_1750, names_1800]
graph_num=range(0, 4)

for g in graph_num:
    print(g)
    dates_new=time_range[g]
    names_new=name_range[g]
    print(names_new)
    
    # Create plot
    
    fig, ax = plt.subplots(figsize=(20, 20))
    ax.set(title="Publikationsdatum")
    ax.scatter(sorted(dates_new), names_new, c='#bcbd22', marker=5)
    
    # Axes.scatter(self, x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=<deprecated parameter>, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)

    ax.set_xlabel(r'Publikationsdatum', fontsize=15)
    ax.set_xlim(min(dates_new), max(dates_new))
    ax.set_ylabel(r'Kartentitel', fontsize=15)
    ax.set_title('Historische Karten zu Kurmainz')
    
    # Highlight reproductions
    
    df = pd.DataFrame(dates_new) 
    duplicates=df[df.duplicated()]
    plt.scatter(dates_new, names_new, color="red")
    
    # Set axes details  
        
    plt.xticks(dates_new, rotation=45, horizontalalignment='right')
    #plt.tick_params(axis='x', colors='red', direction='out', length=13, width=7)
    ax.tick_params(axis='both', which='major', pad=20)
    ax.set_aspect(aspect=0.5)
    plt.tight_layout()
    plt.show()
    plt.savefig("graph%s.svg" % i, dpi = 300)
    plt.close()
    
print("DONE")


# In[ ]:





# In[ ]:




