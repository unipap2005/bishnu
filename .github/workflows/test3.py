import os
import csv
from IPython.utils.io import Tee
from contextlib import closing
import pandas as pd

file = '/Users/avleen/Downloads/03-python/PyPoll/Resources/election_data.csv'
fl = [file]
input = 'input_data'

def vote_count():
    df = pd.read_csv('/Users/avleen/Downloads/03-python/PyPoll/Resources/election_data.csv')
    totcount = df.shape[0]
    return totcount

def candidate():
    candidates = []
    for i in fl:
        path = os.path.join(input, i)
        with open(path, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 'Voter ID':
                    pass
                else:
                    if row[2] not in candidates:
                        candidates.append(row[2])
                    else:
                        pass
    return candidates

def vote_percent():
    candidatedict = {}
    for candidate in candidates:
        candidatedict[candidate] = [0,0]

    for i in fl:
        path = os.path.join(input, i)
        with open(path, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 'Voter ID':
                    pass
                else:
                    for k, v in candidatedict.items():
                        if k == row[2]:
                            v[1] = v[1] + 1
                            v[0] = round(((v[1] / totcount) * 100), 1)
                        else:
                            pass
    return candidatedict

def winner():
    temp = 0
    for k, v in candidatedict.items():
        if v[1] > temp:
            temp = v[1]
            winner = k
        else:
            pass
    return winner

totcount = vote_count()
candidates = candidate()
candidatedict = vote_percent()
winner = winner()

def final_output():
    with closing(Tee("election_results.txt", "w", channel="stdout")) as outputstream:
        print('Election Results')
        print('\n', ('-' * 30))
        print('\n', 'Total Votes:', totcount)
        print('\n', ('-' * 30))
        for k, v in candidatedict.items():
            print('\n' + k + ':', str(v[0]) + '%  (' + str(v[1]) + ')')
        print('\n', ('-' * 30))
        print('\n' + 'Winner: ', winner)
        print('\n', ('-' * 30))


final_output()

