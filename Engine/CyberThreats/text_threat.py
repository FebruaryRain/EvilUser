from .cyber_threat import *

class Text_Threat(Cyber_Threat):
    location = Location.Phone
    theme = random.choice(Theme)

    def __init__(self, sender, receiver):
        self.sender = sender
        self.reciever = receiver
        self.contents = self.build_contents()

    def build_contents(self):
        return