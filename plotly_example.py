"""
pip install plotly==5.14.1
pip install dash

Documentation: https://plotly.com/python/getting-started/
"""

import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html('first_figure.html', auto_open=True)