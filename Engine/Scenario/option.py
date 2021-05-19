

class Option:

  def __init__(self, act_number, option_descriptor, actions_descriptor):
    self.act = act_number
    self.option_descriptor = option_descriptor
    self.actions_descriptor = actions_descriptor
    self.action_taken = False
    print("here")
    print(self.option_descriptor)
    return