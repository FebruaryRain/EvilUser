from .act1 import Act1
from .act2 import Act2
from .act3 import Act3


class Scenario:

  def __init__(self, Hacker):
    self.hacker = Hacker
    self.hacker_type = Hacker.chosen_hacker_info["actor_type"]
    self.hacker_objective = Hacker.chosen_hacker_info["objectives"]
    
    # Sanity Checks
    #print(self.act1)
    #print("This is the Scenario!")
    return

  def generate_scenario(self):
    # Recce Act
    self.act1 = Act1(self.hacker)
    self.act1.create_act()
    # Infiltrate Act
    self.act2 = Act2(self.hacker)
    self.act2.create_act()
    # Exploit Act
    self.act3 = Act3(self.hacker)
    self.act3.create_act()
    return