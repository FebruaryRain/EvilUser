

class Option:

  def __init__(self, act_number, option_descriptor, actions_descriptor):
    self.act = act_number
    self.option_descriptor = option_descriptor
    self.actions_descriptor = actions_descriptor
    self.action_taken = False
    return


  def get_option_descriptor(self):
    return self.option_descriptor


  def get_actions_descriptor(self):
    return self.actions_descriptor