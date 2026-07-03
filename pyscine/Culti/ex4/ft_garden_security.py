class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def get_name(self):
        return self.name

    def set_height(self, value):
        if value >= 0:
            self.__height = value
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, value):
        if value >= 0:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {value} day [REJECTED]")
            print("Security: Negative age rejected")

    def status(self):
        print(f"{self.name} : {self.__height}cm, {self.__age} days old")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


""" if __name__ == "__main__":
    rose = Plant("Rose", 12, 20)
    print("Plant created:", rose.name)
    rose.set_height(5)
    rose.set_height(-20)
    rose.set_age(-20)
    rose.set_age(20) """
