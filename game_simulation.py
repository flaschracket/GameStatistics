
from random import randrange
from GameObjects.Player import *
from GameObjects.Game import *
from copy import deepcopy
import mssql


tempply = Player('')
GS = GameSettings()
sampleCounter = 0
previousStep = Step(0)

#initial

print("Hello From Game Simulation! Data Generation is begining:")

while sampleCounter <= GS.sampleDataNumber:
    mygame = Game(sampleCounter,previousStep)
    mssql.insertGame(mygame)
    #play
    print("Game"+str(sampleCounter)+" begins")
    condition = True
    while condition:
        
        mygame.currentRound = mygame.currentRound + 1
        print("b")
        print(str(mygame.currentStep))
        mygame = copy.deepcopy(mygame.playOneRound()) 
        #mygame.playOneRound()
        print("c")
        print(str(mygame.currentStep))
        if (mygame.winer != '') or (mygame.currentRound >= GS.StoponThisRound): 
            condition = False       
        print("con:"+str(condition))

    print("after while")
       
    mssql.updateGame(mygame)
    print(mygame.winer +' is the winer!')
    sampleCounter = sampleCounter +1


    #-------------------------------
    # make a jason deepcopy
    #-------------------------------
def update_dict(data_copy, data):
    for k, v in data_copy.iteritems():
        if v != data[k]:
            if isinstance(v, dict):
                update_dict(v, data[k])
            elif isinstance(v, list):
                update_list(v, data[k])
            elif isinstance(v, float):
                data_copy[k] = data[k]

def update_list(data_copy, data):
    for i, value in enumerate(data_copy):
        if value != data[i]:
            if isinstance(value, dict):
                update_dict(value, data[i])
            elif isinstance(value, list):
                update_list(value, data[i])
            elif isinstance(value, float):
                data_copy[i] = data[i]

def json_deep_copy(data):
    if data is None:
        return data

    #  precise_float is slower, but we get more reports of diffs
    #  without it (floats being floats)
    try:
        data_copy = ujson.loads(
            ujson.dumps(data, double_precision=15),
            precise_float=True)
        if isinstance(data_copy, list):
            update_list(data_copy, data)
        else:
            update_dict(data_copy, data)
    except OverflowError:
        data_copy = json.loads(json.dumps(data))
    except Exception:
        print ("non-json safe object passed. falling back to deepcopy")
        data_copy = copy.deepcopy(data)
    return data_copy
