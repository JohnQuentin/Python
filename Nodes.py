import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#load the first book
df = pd.read_csv("book1.csv")

#We only look at rows where the weight is greater than 10
df = df.loc[df['weight']>10, :]

# load pandas df as networkx graph
G = nx.from_pandas_edgelist(df, 
                            source='Source', 
                            target='Target', 
                            edge_attr='weight')
print("No of unique characters:", len(G.nodes))
print("No of connections:", len(G.edges))

# import pyvis
from pyvis.network import Network
# create vis network
net = Network(notebook=True, width=1000, height=600)
# load the networkx graph
net.from_nx(G)
# show
net.show("example.html")
