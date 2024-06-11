from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message, num):
        pass

class Email(Notification):
    def send(self, message, num):
        return num, message

class SMS(Notification):
    def send(self, message, num):
        return num, message

email = Email()
sms = SMS()

print(email.send("Hello via Email", "user@example.com"))
print(sms.send("Hello via SMS", "+1234567890"))





















