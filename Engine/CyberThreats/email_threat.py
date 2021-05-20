from Engine.Email.email import Email
from .cyber_threat import *
from .code_generator import *

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
            end = "by using this link: linki.fy/"+codeGenerator().code
        elif self.elaboration * self.chance_of_success >= 0.6:
            end = "by using the link at the eNd of this massage:\ngo.to/"+codeGenerator().code
        elif self.elaboration * self.chance_of_success >= 0.4:
            end = "by replying to this message with your name and we will call you."
        elif self.elaboration * self.chance_of_success >= 0.1:
            end = "bye replying to this massage with your the code in the message and we will message back with more details.\n\n"+codeGenerator().code
        else:
            end = "bye replying to this email with the rekwired detales (name, phone number, address and email)"
        print(beginning + middle + end)
        return beginning + middle + end

    def get_email(self):
        email = Email(self.sender, self.reciever, self.contents, self.theme, [], ["*"])
        return email