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





#class가 메소드를 가지고 있을 경우 안의 모든 메소드는 자동으로 메소드의 첫번째 argument는 self
# instance method는 instance의 변수에 접근 가능하다 ! 그래서 self를 매개변수로 받는다
# 상속은 클래스 이름 옆에 소괄호를 쓰고 그 안에 부모 클래스의 이름을 쓰면됨
class Dog:

  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def sleep(self):
    print("sleep")


class GuardDog(Dog):

  def __init__(self, name, breed):
    #부모클래스의의 인스턴스메소드를 불러올 때
    super().__init__(name, breed, 5)  #age를 원하는 값으로 고정

  def rrr(self):
    print("stay away")


class Puppy(Dog):

  def __init__(self, name, breed):
    #부모클래스의의 인스턴스메소드를 불러올 때
    super().__init__(name, breed, 0.1)  #age를 원하는 값으로 고정

  def __woof_woof__(self):
    print("woof woof")


ruffus = GuardDog(name="Ruffus", breed="beagle")
bogsil = Puppy(name="bogsil", breed="poodle")

bogsil.__woof_woof__()
ruffus.rrr()
bogsil.sleep()
ruffus.sleep()
