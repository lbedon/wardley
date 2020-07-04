#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 23:47:58 2020

@author: Manzanito
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



class product(object):
    '''
    name, dev_grad, value
    '''
    def __init__(self, name, dev_grad=0, value=0):
        self.name = name
        self.value = value
        self.dev_grad = dev_grad
        self.connections = []
      
    @staticmethod  
    def link(a,b):
        '''
        method to link two product instances
        '''     
        a.connections.append(b)
        a.connections = list(set(a.connections))
        b.connections.append(a)
        b.connections = list(set(b.connections))
    
    @staticmethod
    def plot(product_list):
        points = []
        edges = []
        for i in product_list:
            points.append([i.dev_grad,i.value,i.name])
            edges.append([frozenset([i,j]) for j in i.connections])
        edges = set([i for k in edges for i in k]) # set of flattened object
        plt.scatter(np.array(points)[:,0].astype('int'),
                    np.array(points)[:,1].astype('int'))
        for i in points:
            plt.text(i[0]+.1, i[1], i[2])
        for i in edges:
            alpha = [k for k in i]
            plt.plot([alpha[0].dev_grad,alpha[1].dev_grad],[alpha[0].value,alpha[1].value])
        
        plt.show()
    
# %% create instances
n = 10
df = pd.DataFrame()
df['name'] = [[''.join(np.random.choice([chr(i) for i in range(ord('a'),ord('z'))],5))][0] \
              for i in range(n)]
df['dev_grad'] = (np.random.rand(n)*4).astype('int')
df['value'] = (np.random.rand(n)*10).astype('int')

inst = []
for i in df.values:
    inst.append(product(i[0],i[1],i[2]))

df['product_instances'] = inst

# %% determine links between instances
df_links = pd.DataFrame()

links_list = []
links_names = []
for i in range(int(n*.8)):
    links_list.append(np.random.choice(range(n),2,replace=False))
    links_names.append([df['name'][links_list[-1][0]],
                        df['name'][links_list[-1][1]]]
                        )
df_links['links'] = links_list
df_links['links_names'] = links_names


for i in df_links.values:
    product.link(df['product_instances'][i[0][0]],df['product_instances'][i[0][1]])
# %% visualize    

product.plot(df['product_instances'].tolist())

# %% check
df
df_links
[i.name for i in df['product_instances'][0].connections]


# %% 
a = product('component_a',4,5)
b = product('component_b',3,9)
c = product('c',1,2)
d = product('d',2,9)
e = product('e',7,3)
f = product('f',1,10)

product.link(a,b)
product.link(a,e)
product.link(b,d)
product.link(c,b)
product.link(d,f)
#product.link(a,c)

a.connections
c.connections

product.plot([a,b,c,d,e,f])


