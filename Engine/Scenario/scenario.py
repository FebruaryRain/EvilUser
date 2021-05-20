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
    self.points_total = 0
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
    self.calculate_total_points()
    #print(self.points_total)
    return


  def create_full_narrative(self):
    self.options_selected.append(self.act1.get_chosen_option())
    self.options_selected.append(self.act2.get_chosen_option())
    self.options_selected.append(self.act3.get_chosen_option())


  def calculate_total_points(self):
    total_points = 0
    for option_selected in self.options_selected:
      total_points += option_selected.get_points_for_action()
    self.points_total = total_points
    return


  def get_options_selected(self):
    return self.options_selected


  def get_points_total(self):
    return self.points_total