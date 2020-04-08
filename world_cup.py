# world_cup.py
from pymodm import connect, MongoModel, fields


class WC_Game(MongoModel):
    year = fields.IntegerField()
    home_team = fields.CharField()
    home_team_score = fields.IntegerField()
    away_team = fields.CharField()
    away_team_score = fields.IntegerField()
    winner = fields.CharField()


def init_db():
    print("Connecting to database...")
    # connect("mongodb+srv://db_access:swim4life@aimeemcv-7rfsl.mongodb.net/"
    #         "wc?retryWrites=true&w=majority")
    connect("mongodb+srv://bme547student:xbzXZ35Y4&lP@bme547-ba348.mongodb.net/"
            "wc?retryWrites=true&w=majority")
    print("Connected to database")


def add_game_to_db():
    new_game = WC_Game(year=1930,
                       home_team="France",
                       home_team_score=4,
                       away_team="Mexico",
                       away_team_score=1,
                       winner="France")
    response = new_game.save()
    print(response)


def get_all_countries():
    teams = []
    all_games = WC_Game.objects.raw({})
    for game in all_games:
        # home_team = game.home_team
        # away_team = game.away_team
        # print("{}-{}".format(home_team, away_team))
        if game.home_team not in teams:
            teams.append(game.home_team)
        if game.away_team not in teams:
            teams.append(game.away_team)
    teams.sort()
    for team in teams:
        print(team)


def get_England_home_games():
    england_home = WC_Game.objects.raw({"home_team": "England"})
    print(england_home.count())
    for game in england_home:
        print("{}: {} {} - {} {}".format(game.year, game.home_team,
                                         game.home_team_score, game.away_team,
                                         game.away_team_score))


def get_England_away_games():
    england_away = WC_Game.objects.raw({"away_team": "England"})
    print(england_away.count())
    for game in england_away:
        print("{}: {} {} - {} {}".format(game.year, game.home_team,
                                         game.home_team_score, game.away_team,
                                         game.away_team_score))


def get_England_all_games():
    england_all = WC_Game.objects.raw({"$and": [{"year": 1958},
                                                {"$or": [{"home_team": "England"},
                                                         {"away_team": "England"}]}]})
    print(england_all.count())
    for game in england_all:
        print("{}: {} {} - {} {}".format(game.year, game.home_team,
                                         game.home_team_score, game.away_team,
                                         game.away_team_score))


if __name__ == '__main__':
    init_db()
    # add_game_to_db()
    # get_all_countries()
    # get_England_home_games()
    # get_England_away_games()
    # get_England_all_games()
