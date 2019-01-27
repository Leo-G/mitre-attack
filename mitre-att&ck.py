#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:37:33 2019

@author: leo G
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a Bar graph script for the mitre attack
"""



import plotly
import plotly.graph_objs as go
import pandas as pd

csv_file = 'mitre-attack.csv'

df = pd.read_csv(csv_file)
count = df.count()
count_dict = count.to_dict()



data = [go.Bar(
            x= df.columns,
            y= df.count().sort_values(),
            width = 0.5
           
    )]

layout = go.Layout(
        title='No of Possible Cyber Security Attack Techniques as per the MITRE ATT&CK Enterprise  Matrix',
        xaxis=dict(
        title='Tactics',
        
        
    ),
    
  
    yaxis=dict(
        title='No of Possible Techniques',
        
        
    ),
    
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='basic-bar')