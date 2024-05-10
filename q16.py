import pandas as pd
df = pd.Timestamp("2024-04-02")#[M,T,W,TH,F,SAT,SU - 0,1,2,3,4,5,6]
print(df.dayofweek)
