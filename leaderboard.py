import json


def readLeaderboard():
    try:
        with open("leaderboard.json", "r") as read_file:
            leaderboard = json.load(read_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}
    return leaderboard

def writeLeaderboard(data):
    with open('leaderboard.json', 'w') as outfile:
        json.dump(data, outfile)

def playerWin(player):
    lb = readLeaderboard()
    if player in lb:
        lb[player] += 2
        writeLeaderboard(lb)
    else:
        lb[player] = 2
        writeLeaderboard(lb)

def playerLose(player):
    lb = readLeaderboard()
    if player in lb:
        lb[player] -= 1
        writeLeaderboard(lb)
    else:
        lb[player] = -1
        writeLeaderboard(lb)


