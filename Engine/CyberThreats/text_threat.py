from .cyber_threat import *

class Text_Threat(Cyber_Threat):
    location = Location.PHONE
    theme = random.choice(list(Theme))

    def __init__(self, sender, receiver):
        self.sender = sender
        self.reciever = receiver
        self.theme = random.choice(list(Theme))
        self.contents = self.build_contents()

    def build_contents(self):
        message = self.theme.build()
        beginning = random.choice(message['BEGINNING'])
        middle = random.choice(message['MIDDLE'])
        if self.elaboration * self.chance_of_success >= 0.8:
            end = "by using this link: linki.fy/"+codeGenerator()
        elif self.elaboration * self.chance_of_success >= 0.6:
            end = "by using the link at the eNd of this massage:\ngo.to/"+codeGenerator()
        elif self.elaboration * self.chance_of_success >= 0.4:
            end = "by replying to this message with your name and we will call you."
        elif self.elaboration * self.chance_of_success >= 0.1:
            end = "bye replying to this massage with your the code in the message and we will message back with more details.\n\n"+codeGenerator().code
        else:
            end = "bye replying to this email with the rekwired detales (name, phone number, address and email)"
        print(beginning + middle + end)
        return beginning + middle + end

class codeGenerator():

    alphaNum = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(self):
        self.code = ""
        for i in range(random.randint(1,10)):
            self.code += random.choice(self.alphaNum)*random.randint(1,2)

        
