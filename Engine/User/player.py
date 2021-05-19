

class Player:
  """
  Class to hold the defining characteristics of the player - the LBG employee using the program. 
  """

  def __init__(self, 
              forename = "",
              surname = "",
              email = "", 
              role = "", 
              id = "", 
              is_customer_facing = False
              ):
    self._forename = forename
    self._surname = surname
    self.email = email
    self._role = role
    self._id = id
    self._is_customer_facing = is_customer_facing
    self.score = 0.0


  def set_role(self, role = ""):
    self._role = role
    return


  def get_role(self):
    return self._role


  def get_full_name(self):
    full_name = self._forename + " " + self._surname 
    return full_name


  def get_id(self):
    return self._id


  def set_id(self, id = ""):
    self._id = id
    return


  def get_is_customer_facing(self):
    return self._is_customer_facing


  def set_is_customer_facing(self, is_customer_facing = False):
    self._is_customer_facing = is_customer_facing
    return
