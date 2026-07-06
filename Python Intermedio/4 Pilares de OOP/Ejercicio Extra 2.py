""""
    Cree una clase abstracta User con los siguientes métodos abstractos:
        get_role()
        has_permission(permission)

Luego cree dos clases que hereden de ella:

    AdminUser
    RegularUser

Cada una debe implementar los métodos
Por ejemplo:

    AdminUser siempre tiene permisos
    RegularUser solo tiene permisos limitados ("read", por ejemplo)
"""
from abc import ABC,  abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass
    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    
    def get_role(self):
        self.role = "Admin"
        return self.role
        
    def has_permission(self, permission):
        self.permission = permission
        return True
    
class RegularUser(User):
    
    def get_role(self):
        self.role = "Regular"
        return self.role
    #valida si es igual a lectura, no acepta nada mas que no sea lectura
    def has_permission(self, permission): 
        return permission.lower() == "read"
    

user1 = AdminUser()
user2 = RegularUser()

print(user1.has_permission("delete"))  # True
print(user2.has_permission("delete"))  # False