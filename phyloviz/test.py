from phyloviz import model
from model import Model
from phyloviz.model import Tree
import pandas as pd

m = Model('./astral.MR.rooted.nid.nosup.nwk', 'newick','ncbi.t2t.txt','metadata.txt')
#edgeM = m.retrive_view_coords()
#print(edgeM)
cv_pairs = {'branch_color': '#444444', 'width': 0.5}
edge = m.updateEdgeCategory('marker_count',cv_pairs ,lower=300,upper=500)
print(edge)

'''
meta_internal = model.read_internal_node_metadata("./ncbi.t2t.txt")
meta = model.read_leaf_node_metadata("./metadata.txt")
print(type(meta))
print(meta_internal)
left = pd.DataFrame({'dummy':[1,2,3],'node id': [1,2,3],'coordinates':[3,3,3]})
right = pd.DataFrame({'too':[2,2],'node id': [1,3],'label':[4,4]})
print(left.columns.values)
print(right.columns.values)
result = pd.merge(left,right,how='left',on='node id')
print(result)
'''
