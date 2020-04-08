# world_cup_list.py
from pymodm import connect, MongoModel, fields


class WC_Team(MongoModel):
    team_name = fields.CharField(primary_key=True)
    opponents = fields.ListField()


def init_db():
    print("Connecting to database...")
    connect("mongodb+srv://db_access:swim4life@aimeemcv-7rfsl.mongodb.net/"
            "wc_team?retryWrites=true&w=majority")
    print("Connected to database")


def add_country():
    new_country = WC_Team(team_name="Canada")
    new_country.save()


def add_opponent(input_team_name, input_opponent):
    team = WC_Team.objects.raw({"_id": input_team_name}).first()
    team.opponents.append(input_opponent)
    team.save()


def get_opponents(input_team_name):
    team = WC_Team.objects.raw({"_id": input_team_name}).first()
    for opponent in team.opponents:
        print(opponent)


if __name__ == '__main__':
    init_db()
    # add_opponent("Canada", "Mexico")
    # add_opponent("Canada", "USA")
    get_opponents("Canada")
