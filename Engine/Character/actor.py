from .hacker import Hacker

class Actor(Hacker):


  def __init__(self, Player):
    super().__init__()
    self.player = None
    self.set_player(Player)
    self.applicable_hackers = []
    self.set_applicable_hackers()
    self.chosen_hacker_info = None 
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


  def set_applicable_hacker(self, chosen_hacker):
    self.current_hacker = chosen_hacker
    return


  def set_player(self, Player):
    try:
        self.player = Player
        print("Hello " + self.player.get_full_name() + ",")
    except:
      print("We don't have a player defined! \n Please close and restart the game, there has been an error!")
    return

  def set_chosen_hacker_info(self, info):
    if info != None:
      self.chosen_hacker_info = info
    else:
      print("You tried to set the actor.chosen_hacker_info but it was of a None value!")