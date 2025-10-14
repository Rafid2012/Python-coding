class system:
    def __init__(self):
        self.user = {}
        self.current_user = None

    def register(self):
        u = input("New usernane: ")
        if u in self.user:
            print("User already exissts")
        else:
            p = input("password: ")
            self.user[u] = p
            print("Registered")

    def login(self):
        if self.current_user:
            print(f"Already logged in as {self.current_user}")
            return
        u = input("Username: ")
        p = input("Password: ")
        if self.user.get(u) == p:
            self.current_user = u
            print(f"welcome, {u}")
        else:
            print("invalid")

    def logout(self):
        if self.current_user:
            print(f"logged out {self.current_user}")
            self.current_user = None
        else:
            print("No user logged in")

    def run(self):
        actions = {
            "1": self.register,
            "2": self.login,
            "3": self.logout,
            "4": exit
        }

        while True:
            print("\n 1.register 2.login 3.logout 4.exit")
            action = input("choose: ")
            actions.get(action,lambda:print("invalid"))()

if __name__ == "__main__":
    system().run()

        
    