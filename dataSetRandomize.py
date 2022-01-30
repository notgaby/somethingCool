import random as r
import pandas as pd
import os

def createNewTweet(spaceFacts):

    col = pd.read_csv(spaceFacts)
    colSize = len(col.columns)

    info = []

    if spaceFacts == 'datasets/astronauts.csv':
        luckyGuy = r.randint(0,colSize-1)
        colForAst = [0,1,12,14]

        for i in range(len(colForAst)):
            if i > 0:
                info.append(int(col.iat[luckyGuy,colForAst[i]]))
            else:
                info.append(col.iat[luckyGuy, colForAst[i]])

        if (info[2] > 1 or info[2] == 0) and (info[3] > 1 or info[3] == 0):
            infoStr = info[0] + " was an astronaut who was first selected by NASA in " + str(info[1]) +\
            ". During this time they took part in " + str(info[2]) + " space flights and " + str(info[3]) +\
            " space walks!"
        elif (info[2] > 1 or info[0] == 0) and info[3] < 2:
            infoStr = info[0] + " was an astronaut who was first selected by NASA in " + str(info[1]) + \
            ". During this time they took part in " + str(info[2]) + " space flights and " + str(info[3]) + \
            " space walk!"
        elif info[2] < 2 and (info[3] > 1 or info[3] == 0):
            infoStr = info[0] + " was an astronaut who was first selected by NASA in " + str(info[1]) + \
            ". During this time they took part in " + str(info[2]) + " space flight and " + str(info[3]) + \
            " space walks!"
        else:
            infoStr = info[0] + " was an astronaut who was first selected by NASA in " + str(info[1]) + \
            ". During this time they took part in " + str(info[2]) + " space flight and " + str(info[3]) + \
            " space walk!"

        return infoStr

    else:
        ranFact = r.randint(0,colSize)
        fact = col.iat[ranFact,0]

        return fact
    
def chooseDataSet():
    count = 0
    filePaths = []

    for path in os.listdir('datasets'):
        if os.path.isfile(os.path.join('datasets',path)):
            filePaths.append('datasets/' + path)
            count += 1

    randSet = r.randint(0,count-1)
    luckyDataset = filePaths[randSet]

    createNewTweet(luckyDataset)

print(chooseDataSet())

