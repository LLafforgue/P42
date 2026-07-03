# from ex2 import EliteCard

# try:
#     elite = EliteCard('rrrh', 2, 'common', 10, 5, 'melee')
#     elite.get_name()
#     elite.play({'mana_used': 5})
# except (Exception) as e:
#     print(e)

# test: list[dict | str] = [
#     {'ele': 11, 'test': 10},
#     {'ele': 10, 'test': 100},
#     ]
# test.remove({'ele': 10, 'test': 100})
# print(test)
# if any(not isinstance(e, dict) for e in test):
#     print('ok')
# else:
#     print('pas ok')
# test += ['test']
# print(test)

# class Mere:

#     def __init__(self, name: str) -> None:
#         self.name = name

#     def get_info(self) -> dict:
#         return {f'{k}': vars(self)[k] for k in vars(self)}


# class Pere:

#     def __init__(self, rate: int) -> None:
#         self.rate = rate

#     def add_rate(self) -> None:
#         self.rate += 1


# class Fille(Mere, Pere):

#     def __init__(self, name: str, rate: int, bonus: str):
#         super().__init__(name)
#         self.rate = rate
#         self.bonus = bonus

#     def get_rate(self) -> int:
#         return self.rate


# if __name__ == "__main__":
#     test = Fille('test', 10, 'lala')
#     print(test.get_info())
#     print(test.__class__.__mro__[0].__name__)
#     test.add_rate()
#     test.add_rate()
#     test.add_rate()
#     test.add_rate()
#     test.add_rate()
#     print(test.get_rate())

test: list = []
print(sorted(test))
