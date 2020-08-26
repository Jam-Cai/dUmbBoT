import json

def readHistory():
    try:
        with open("history.json", "r") as read_file:
            print("Converting JSON encoded data into Python dictionary")
            history = json.load(read_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
    return history

def writeHistory(data):
    with open('history.json', 'w') as outfile:
        json.dump(data, outfile)

def addGame(winner, loser):
    hst = readHistory()
    hst.append("{} vs {:<10} {} wins ".format(winner, loser, winner))
    writeHistory(hst)

def tieGame(player1, player2):
    hst = readHistory()
    hst.append("{} vs {:<10} Tie game ".format(player1, player2))
    writeHistory(hst)