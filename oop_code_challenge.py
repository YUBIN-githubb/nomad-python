class Player:

  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team
    self.removed = False

  def introduce(self):
    print(f"Hello. I'm {self.name}. and I play for {self.team}.")


class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []

  def add_player(self, name):
    new_player = Player(name, self.team_name)
    self.players.append(new_player)
    new_player.introduce()

  def remove_player(self, name):
    for player in self.players:
      if player.name == name:
        player.removed = True
        print(f"removed {player.name}")

  def show_players(self):
    for player in self.players:
      if player.removed == False:
        print(player.name)

  def show_xp(self):
    total_xp = 0
    for player in self.players:
      total_xp = total_xp + player.xp
    print(f"the {self.team_name}'s total xp is {total_xp}")

korea = Team(
  team_name="Korea"
)
korea.add_player("kim")
korea.add_player("son")
korea.show_xp()
korea.remove_player("son")
korea.show_players()