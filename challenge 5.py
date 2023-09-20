#define the base class player
class Player:

  def play(self):
    print("the player is playing cricket:")


#define the derived class  batsmanclass
class Batsman(Player):

  def play(self):
    print("the batsman is batting")


#define the derived class bowler
class Bowler(Player):

  def play(self):
    print("the bowler is bowling")


#create objects of batsman and bowling
batsman = Batsman()
bowler = Bowler()
#call the play ()method for each objects
batsman.play()
bowler.play()