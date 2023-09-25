class Player:
  def play(self):
    print("The player is playing cricket.")

#Define the derived class1 Batman
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

#Define the derived class2 Bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

#Crete a object of each class
batsman = Batsman()
bowler  = Bowler()

batsman.play()
bowler.play()