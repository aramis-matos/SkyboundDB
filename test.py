import pandas as pd

def printblockname(a):
    for k in range(len(a)):
        if a[k] == 'm':
            print("mid", end=' ')
        if a[k] == 'a':
            print("air", end=' ')
        if a[k] == 't':
            print("throw", end=' ')
        if a[k] == 't':
            print("throw", end=' ')
        if a[k] == 'l':
            print("low", end=' ')



df = pd.read_csv("gran_fd.csv")
df.style.hide_index()
moves = list(df.columns)
stats = list(df.index)
for i in range(len(moves)):
    print(moves[i])
    data = list(df[moves[i]])
    print("Damage: " + str(data[0]))
    print("Guard: ", end=' ')
    printblockname(str(data[1]))
    print()
    print("Startup: " + str(data[2]))
    print("Active: " + str(data[3]))
    print("Recovery: " + str(data[4]))
    print("On Block: " + str(data[5]))
    print("On Hit: " + str(data[6]))
    print()


