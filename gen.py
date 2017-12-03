#
# generates a random dataset to train the ML algorithm
# in order to predict a safe, good value to give as
# credit to the youngling.
#

import sys
import numpy as np

def choose_onehot(v,probs):
    return v[np.random.choice(probs.size, p=probs)]

def choose_indep(v,probs):
    return np.array([np.random.randint(2) for i in range(probs.size)])

def random_client_data():
    data_size = 1

    # years as client, discretized in 0-1, 2-3, 4-5, 6+ years
    size_years = 4
    prob_years = np.array([0.4,0.3,0.2,0.1])
    years = np.identity(size_years)

    # investment products, classified in beginner (CDB, LCA, LCI), medium (fundos) and advanced (acoes) lvls
    size_invs = 3
    prob_invs = np.array([0.5,0.3,0.2])
    invs = np.identity(size_invs)

    # balance analysis, based on whether the final value is positive or not. the past 4 months are analyzed to give more info about a person
    size_analysis = 4
    prob_analysis = np.array([0.1,0.3,0.2,0.4])
    analysis = np.identity(size_analysis)

    # average percentage of invested money, based on total month money
    size_invp = 3
    prob_invp = np.array([0.7,0.2,0.1])
    invp = np.identity(size_invp)

    # saved amount, on all lvls
    max_saved_value = 500
    saved_value = np.random.randint(30,max_saved_value)

    # average credit amount thoughout life
    ave_cred = np.random.randint(50,max_saved_value * 0.5)

    # current credit amount, the value to be predicted
    cred = np.random.randint(50,max_saved_value * 0.5)

    dataset = np.array(np.zeros(16))

    line = np.append([],choose_onehot(years,prob_years))
    line = np.append(line,choose_indep(invs,prob_invs))
    line = np.append(line,choose_indep(analysis,prob_analysis))
    line = np.append(line,choose_onehot(invp,prob_invp))
    line = np.append(line,[np.random.randint(30,max_saved_value)])
    line = np.append(line,[np.random.randint(50,0.5 * max_saved_value)])

    return line.tolist()
