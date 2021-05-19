from .act1 import Act1
from .act2 import Act2
from .act3 import Act3


class Scenario:

  def __init__(self, Hacker):
    self.hacker = Hacker
    self.hacker_type = Hacker.chosen_hacker_info["actor_type"]
    self.hacker_objective = Hacker.chosen_hacker_info["objectives"]
    self.act1 = None
    self.act2 = None
    self.act3 = None
    self.options_selected = []
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

    self.create_full_narrative()
    return


  def create_full_narrative(self):
    # Sanity Checks
    print(self.act1.get_chosen_option().actions_descriptor)
    print(self.act2.get_chosen_option().actions_descriptor)
    print(self.act3.get_chosen_option().actions_descriptor)
    self.options_selected.append(self.act1.get_chosen_option())
    self.options_selected.append(self.act2.get_chosen_option())
    self.options_selected.append(self.act3.get_chosen_option())

    return