import os
import sys
import pandas as pd

d1 = "./ccer/D2/abt.csv"
d2 = "./ccer/D2/buy.csv"
gt = "./ccer/D2/gt.csv"

N = 100

# Get first N entities
d1 = pd.read_csv(d1, sep='|', engine='python', na_filter=False)
d2 = pd.read_csv(d2, sep='|', engine='python', na_filter=False)
gt = pd.read_csv(gt, sep='|', engine='python')



d1_subset = d1[d1['id'] < N]
d2_subset = d2[d2['id'] < N]


print(d1_subset)
print(d2_subset)

gt_subset = gt[(gt['D1'] < N) & (gt['D2'] < N)]


print(gt_subset)

# merged = pd.merge(gt, d1.head(N), on="id")

# print(merged)

d1_subset.to_csv('abt_100.csv',index=False, sep='|')
d2_subset.to_csv('buy_100.csv',index=False, sep='|')
gt_subset.to_csv('gt_100.csv',index=False, sep='|')