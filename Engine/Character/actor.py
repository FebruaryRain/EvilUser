from .hacker import Hacker

class Actor(Hacker):


  def __init__(self, Player):
    super().__init__()
    self.player = None
    self.set_player(Player)
    self.applicable_hackers = []
    self.set_applicable_hackers()

    # Sanity Checks
    #print(self.first_name)
    #print(self.surname)
    #print(self.applicable_hackers)
    return


  def set_applicable_hackers(self):
    for h in self.hackers_list:
      if self.player.get_is_customer_facing():
        #print("This player faces the front of house!")
        if h["for_FOH"]:
          self.applicable_hackers.append(h)
      else: 
        #print("This player does NOT face front of house!")
        if h["for_BOH"]:
          self.applicable_hackers.append(h)
    return

  def get_applicable_hackers(self):
    return self.applicable_hackers


  def set_player(self, Player):
    try:
      #if type(Player) != None:
        self.player = Player
        #
        print("Hello " + self.player.get_full_name() + ",")
    except:
      print("We don't have a player defined! \n Please close and restart the game, there has been an error!")
    return