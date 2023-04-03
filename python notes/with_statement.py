# without with statement
file = open("test.txt", "w")
try:
    file.write("test")
finally:
    file.close()


# with statement, nothing to do with handling the exception    
with open("test.txt", "a") as file:
    file.write("test1")


# Define user class support With statement, implement the following methods: __enter__, __exit__
class MessageWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "a")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
    
    def write(self, message):
        self.file.write(message)

with MessageWriter("test2.txt") as file:
    file.write("test2")

