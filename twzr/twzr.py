# twzr.py 

import pandas as pd 
import numpy as np 
import os 
import time  
import re 

f = lambda x,y: x.filter(regex=re.compile(y,re.IGNORECASE))
vc = lambda x,y,d=False,n=True: x[y].value_counts(dropna=d,normalize=n)

def wvc(df,c,n=True):
    gb = df.groupby([c]).sum()
    if n:
        gb = gb/gb.sum()

    return gb 


cross = lambda x,y: x + " x " + y


def cross_col(df,x,y):
    df[cross(x,y)] = cross(df[x],df[y])


def ch_val(df,c,mask,nv): 

    df[c] = np.where(
        mask,
        nv,
        df[c]
        )


def ch_vals(df,c,masks:list,nvs:list):
    for mask,nv in zip(masks,nvs):
        ch_val(df,c,mask,nv)


def ch_val_from(df,c,ov,nv): 
    if not isinstance(ov,list):
        ov = [ov]
    
    ch_val(df,c, df[c].isin(ov),nv)


def ch_vals_from(df,c,ovs:list,nvs:list):
    for ov,nv in zip(ovs,nvs):
        ch_val_from(df,c,ov,nv)


def xt(df,row_col,col_col,w="auto_weight",normalize="index"):
    if w is not None:
        return pd.crosstab(
            df[row_col],
            df[col_col],
            df[w],
            aggfunc="sum",
            normalize=normalize
            )
    else:
        return pd.crosstab(
            df[row_col],
            df[col_col],
            normalize=normalize
            )


def move_col(df,col,new_index=None):
    # TODO allow for string name
    # defaults to last column 
    if new_index is None:
        new_index = df.shape[1]-1
    xs = df.pop(col)
    df.insert(new_index,col,xs)

help_str = """
    current functions are:
        f
        vc
        wvc
        cross
        cross_col
        ch_val
        ch_vals
        ch_val_from
        ch_vals_from
        xt
        move_col

    
"""


def help():

if __name__ == "__main__":
    
    fd = r""
    os.chdir(fd)
    fn = ""

    df = pd.read_csv(fn)

    ts = time.strftime("_%Y%m%d-%H%M")