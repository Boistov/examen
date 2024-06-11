from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self, content):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        with open("user.txt", 'r') as file:
            return file.read()
    
    def write(self, content):
        with open("user.txt", 'w') as file:
            file.write(content + '\n')

text= TextFileHandler()
text.write('Hello, World!')
text.write('Salom Jahon!')
print(text.read())














