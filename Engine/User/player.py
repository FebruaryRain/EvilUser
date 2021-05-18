class player():
    _email = "" #Real life email of the player, to be grabbed via api
    _forename = ""
    _surname = ""
    _id = ""
    _is_customer_facing = False
    _role = ""
    _score = 0.0

    
    def __init__(self, email = "", role = "", id = "", is_customer_facing = False):
        self.email = email
        self._role = role
        self._id = id
        self._is_customer_facing = is_customer_facing
        self.score = 0.0
    
    def setRole(self, role = ""):
        self._role = role

    def getRole(self):
        return self._role

    def getFullName(self):
        return self._forname + " " + self._surname 
    
    def getId(self):
        return self._id
    
    def setId(self, id = ""):
        self._id = id

    def getIsCustomerFacing(self):
        return self._is_customer_facing

    def setIsCustomerFacing(self, is_customer_facing = False):
        self._is_customer_facing = is_customer_facing

    
