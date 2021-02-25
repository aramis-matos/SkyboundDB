import pandas as pd

df = pd.read_csv("gran_fd.csv")
df.style.hide_index()
moves = list(df.columns)
stats = list(df.index)
for i in range(len(moves)):
    print(df[str(moves[i])])
