import numpy as np

def pct_trans():
    return (float) (np.random.randint(40,60)) / 100

def pct_games():
    return (float) (np.random.randint(40,70)) / 100

def pct_idle():
    return (float) (np.random.randint(60,100)) / 100

def get_pcts():
    choice = np.random.randint(0,6)
    l = [0,0,0,0]

    if choice == 0:
        l[0] = pct_trans()
        l[1] = l[2] = l[3] = (1 - l[0])/3
    elif choice == 1:
        l[1] = pct_games()
        l[0] = l[2] = l[3] = (1 - l[1])/3
    elif choice == 2:
        l[2] = pct_idle()
        l[0] = l[1] = l[3] = (1 - l[2])/3
    else:
        l[0] = l[1] = l[2] = l[3] = 0.25
    return l, choice

# 'pcts' is a list of percentages used by each thing money was spent on
# in this example, it has 4 values, regarding costs in transportation (0),
# games (1), idle (2) money and others (3, unranked), in the past weeks
def get_dataset():
    data_size = 10000

    for i in range(data_size):
        pcts,choice = get_pcts()
        for el in pcts:
            print("%.3f" % (el),end=',')
        if choice <= 2: # there is one separate category for each type of expense
            print(choice)
        else: # and one for all other
            print(3)

