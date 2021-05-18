from .email import email
class EmailClient():
    emails = {
        "inbox":[],
        "outbox":[],
        "sent":[]        
        }
    email = email()


    def __init__(self):
        self.emails = []
        
    def ReceiveEmail(self, email):
        self.emails["inbox"].append(email)

    def SendEmail(self, email):
        self.emails["outbox"].append(email)
        if email.is_valid():
            pass
