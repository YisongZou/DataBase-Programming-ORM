import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ORM.settings")

import django
if django.VERSION >= (1, 7):
    django.setup()

def loadState():
    from ncaa_db.models import State
    f = open('state.txt')
    States = []
    for line in f:
        state_id, name= line.split(' ')
        state = State(name = name)
        States.append(state)
    f.close()
    State.objects.bulk_create(States)
    return

def loadColor():
    from ncaa_db.models import Color
    f = open('color.txt')
    Colors = []
    for line in f:
       color_id, name= line.split(' ')
       color = Color(name = name)
       Colors.append(color)
    f.close()
    Color.objects.bulk_create(Colors)
    return

def loadTeam():
    from ncaa_db.models import Team, State, Color
    f = open('team.txt')
    Teams = []
    for line in f:
        team_id, name, state_id, color_id, wins, losses= line.split(' ')
        team = Team(name = name, state_id = State.objects.get(state_id = state_id), color_id = Color.objects.get(color_id = color_id), wins = wins, losses = losses)
        Teams.append(team)
    f.close()
    Team.objects.bulk_create(Teams)
    return

def loadPlayer():
    from ncaa_db.models import Player, Team
    f = open('player.txt')
    Players = []
    for line in f:
        player_id, team_id, uniform_num, first_name, last_name, mpg, ppg, rpg, apg, spg, bpg= line.split(' ')
        player = Player(team_id=Team.objects.get(team_id = team_id), uniform_num=uniform_num, first_name=first_name, last_name=last_name, mpg=mpg, ppg=ppg, rpg=rpg, apg=apg, spg=spg, bpg=bpg)
        Players.append(player)
    f.close()
    Player.objects.bulk_create(Players)
    return

def action():
    loadState()
    loadColor()
    loadTeam()
    loadPlayer()
