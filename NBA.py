#python program to get the scores of current NBA games and stats of players in each game.

from requests import get
from pprint import PrettyPrinter

mainurl = "https://nba-prod-us-east-1-mediaops-stats.s3.amazonaws.com"
json = "/NBA/liveData/scoreboard/todaysScoreboard_00.json"

printer = PrettyPrinter()

response = get(mainurl + json).json()
sboard = response['scoreboard']
printer.pprint(sboard.keys())

def info_games():
    games = get(mainurl + json).json()['scoreboard']['games']
    
    for game in games:
        home = game['homeTeam']
        away = game['awayTeam']
        quarter = game['period']
        clock = game["gameClock"]
        Hscore = game['homeTeam']['score']
        Ascore = game['awayTeam']['score']
        topPlayerHome = game['gameLeaders']['homeLeaders']
        topPlayerAway = game['gameLeaders']['awayLeaders']
        print(f"--------------")


        #-----score and game info
        print(f"{home['teamTricode']} vs {away['teamTricode']}")
        print(f"{Hscore} to {Ascore}")
        print(f"{clock}" ,"|", "Q:", f"{quarter}")


        #------top players P/R/A
        print("*","Game Leaders:")
        print(f"{topPlayerHome['name']}:","Points:",f"{topPlayerHome['points']}"",",
        "Rebounds:",f"{topPlayerHome['rebounds']}"",","Assists:",f"{topPlayerHome['assists']}"  )
        print(f"{topPlayerAway['name']}:","Points:",f"{topPlayerAway['points']}"",",
        "Rebounds:",f"{topPlayerAway['rebounds']}"",","Assists:",f"{topPlayerAway['assists']}"  )
        
info_games()
