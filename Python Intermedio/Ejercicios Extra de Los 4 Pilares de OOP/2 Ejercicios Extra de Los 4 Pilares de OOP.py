#Cree una clase abstracta User con los siguientes métodos abstractos:
#get_role()
#has_permission(permission)
#Luego cree dos clases que hereden de ella:
#AdminUser
#RegularUser
#Cada una debe implementar los métodos
#Por ejemplo:
#AdminUser siempre tiene permisos
#RegularUser solo tiene permisos limitados ("read", por ejemplo)

class User:
    def __init__(self, role):
        self._role = role

    def get_role(self):
        return self._role

    def has_permission(self, permission):
        return permission in self._permissions


class AdminUser(User):
    def __init__(self, name):
        super().__init__("admin")
        self._name = name

    def get_role(self):
        return "admin"

    def has_permission(self, permission):
        return True

class RegualarUser(User):
    def __init__(self, name):
        super().__init__("regular")
        self._name = name
        self._permissions = ["read"]

def main():
    user1 = AdminUser("Pepe")
    user2 = RegualarUser("Juan")
    print(user1.has_permission("Delete"))
    print(user2.has_permission("Delete"))    

if __name__ == "__main__":
    main()