import plotly.graph_objects as go
from plotly.offline import plot


bar = go.Bar(x = ['bob', 'boba', 'boban'], y= [21, 19, 17] )

layout = go.Layout(title='Ages', xaxis= dict(title = 'students') ,  yaxis= dict( title= 'ages') )

fig = go.Figure(data = [bar], layout = layout )

plot(fig)