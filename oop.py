"""
def create_player(name, xp, team):
  return {
    'name' : name,
    'xp' : xp,
    'team' : team
  }

def introduce_player(player):
  name = player['name']
  team = player['team']
  print(f"hello my name is {name} and my team is {team}")

yubin = create_player('yubin', 100, 'spurs')
introduce_player(yubin)
"""

#class가 메소드를 가지고 있을 경우 안의 모든 메소드는 자동으로 메소드의 첫번째 argument는 self 
class Puppy:
  def __init__(self):
    self.name = "Ruffus"
    self.age = 10
    self.breed = "canine"

ruffus = Puppy()
bogsil = Puppy()
print(ruffus.name)
print(bogsil.name)