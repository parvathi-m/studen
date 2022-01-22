import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv('data.csv')
studen = df.loc[df['student_id']=='TRL_xsl'] 
print(studen)

fig = go.Figure(go.Bar(
    x = studen.groupby('level')['attempt'].mean(),
    y = ['Level 1','Level 2','Level 3','Level 4'],orientation = 'h' 
))
fig.show()  