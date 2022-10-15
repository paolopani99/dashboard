#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from jupyter_dash import JupyterDash
from dash import html, Input, Output, dcc, Dash
import plotly.express as plt


# In[2]:


df=pd.read_excel(r"C:\Users\paolo\OneDrive\Documenti\Imprese artigiane.xlsx")


# In[3]:


df.columns


# In[4]:


print(df["Regione"].unique())
df.tail(7)


# In[15]:


app=JupyterDash()
regione=dcc.Dropdown(options=df["Regione"].unique(), value="ITALIA")
app.layout=html.Div(children=[
    html.H1(children="Variazione numero imprese nel settore autotrasporti"),
    regione,
    dcc.Graph(id="Regione")
])

@app.callback(
    Output(component_id="Regione", component_property="figure"),
    Input(component_id= regione, component_property="value")
)
def update_graph(selected_region):
    filtered_reg=df[df["Regione"]==selected_region]
    line_fg= plt.line(filtered_reg, y="Imprese artigiane totali ", x="Anno", title=f"Variazione numero imprese artigiane in {selected_region} (ITALIA/sigla regione) negli ultimi dieci anni")
    return line_fg
if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




