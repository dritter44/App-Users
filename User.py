# your User class goes here



class User:
    def __init__(self,name,email_address,Dr_Lic_Num):
        self.name = name
        self.email_address = email_address
        self.Dr_Lic_Num = Dr_Lic_Num
    
    def __str__(self):
        return f"{self.name} has email {self.email_address} and license # {self.Dr_Lic_Num}."

alice = User('Alice', 'alice.doe@gmail.com','asdfjkl;')
bob = User('Bob','bob.smith@mail.mil','qwrttty')
carrol = User('Carrol','carrol.johnson@att.com', 'zxcvnm,')

print(alice,'\n',bob,'\n',carrol)
