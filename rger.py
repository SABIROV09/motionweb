# words = [True, False, 12, -56, "python", "Java", 3.45]
#
# del words[4]
#
# print(words)
#
#
# words = [True, False, 12, -56, "pyton", "java",3.45]
#
# words[2], words[5] = words[5], words[2]
#
# print(words)
#
#
# words = [True, False, 12, -56, "pyton", "gava", 3.45]
#
# words[3] ="python"
#
# words.insert(1, "34")
#
# print(words)
#
#
# glass = "ауоиэыяюеё"
# a = 0
# b = 0
#
# word = input("Введите слова")
# for i in word:
#         a += 1
#    else:
#        b += 1
# print(f"Количество гласных {a}\n Количество согласных  {b}")



#
#
# object = (True, 6.13, "python", 12)
#
# words = [True, 6.13,  12, ]
#
#
# print = [words]
#
# object = (True, 6.13, "python", 12)
#
# words = [True, 6.13, "Java", 12 ]
#
# print = [words]
#
# student = {
#    "name": "Bektur",
#    "age": 12,
#   "hobbi": ['chess', 'boxing']
# }
#
# print(student["hobbi"])
#
# """добавление"""




#Дан словарь students, где ключами являются имена , а значениями - списки их оценок по трем предметам.


# students = {
#   'Айбек': [5, 4, 3],
#   'Бурул': [4, 5, 5],
# srednie_osenki ={}
# for student, osenki in students.items():
#  srednie_osenki[student] = (sum(osenki) / len(osenki))
#
# otlichniki = [student for student, osenki in srednie_osenki.items() if osenki == 0]
# horoshisty = [student for student, osenki in srednie_osenki.items() if 4 <= osenki < 5]
# print("Средние баллы студентов:")
# for student, osenki in srednie_osenki.items():
#  print(f"{student}: {osenki:2f")
#
#
#    rint("\nОтличники:")
# print(otlichniki)
#
# print("\nХорошисты:")
# print(horoshisty)
#
# my_list = [i for i in range(1, 10, -1)]
# print(my_list)
#
# def reversed1(variable):
#    res=[]
#     for i in range(len(variable)-1,-1,-1):
#        res.append(variable[i])
#     res=''.join(res)
#    return res

#
#
# def int_to_roman(num):
#     val = [
#         1000, 900, 500, 400,
#        100, 90, 50, 40,
#        10, 9, 5, 4,
#        1
#     ]
#    syms = [
#         "M", "CM", "D", "CD",
#        "C", "XC", "L", "XL",
#        "X", "IX", "V", "IV",
#        "I"
#     ]
#     roman_num = ''
#     i = 0
#     while num > 0:
#        for _ in range(num // val[i]):
#            roman_num += syms[i]
#            num -= val[i]
#         i += 1
#    return roman_num
#
#
# number = int(input("Введите число от 1 до 3999: "))
# if 1 <= number <= 3999:
#    print(int_to_roman(number))
# else:


#
#
#
#
# class Human:    # класс - (шаблон нашего объекта)
#
#     brain = True     # аргументы на уровне класса
#     hearth = True
# def students(name, age, mark):
#
#     def __init__(self, name, age):    # конструктор класса
#         self.name = name
#         self.age = age
#
#     def hello_people(self):     # метод
#         return f"{self.name} привет, тебе {self.age} летооо


# class Cat:
#     # Атрибут уровня класса
#     animels = "animels"
#
#     def __init__(self, name, age, level, energy ):
#         self.name = name
#         self.age = age
#         self.level = level
#         self.energy = energy
#
#     def multiply_hp(self):
#         self.level = self.level ** 2
#         self.energy = True
#
#     def display_fly_status(self):
#         if self.energy:
#             print(f"{self.name} can energy: ")
# #           print(f"{self.age}can age: ")
#
# class AirHero(SuperHero):
#     # Атрибут уровня класса
#     people = "air hero"
#
#     def multiply_hp(self):
#         super().multiply_hp()
#
#
# class EarthHero(SuperHero):
#     # Атрибут уровня класса
#     people = "earth hero"
#
#     def multiply_hp(self):
#         super().multiply_hp()
#
#
# class Villain(SuperHero):
#     # Изменение атрибута уровня класса на monster
#     people = "monster"
#
#     def gen_x(self, hero):
#         hero.hp -= self.damage
#
#     def crit(self):
#         return self.damage ** 2
#
#     # Создание объектов для классов героев
#
#
# air_hero = AirHero("Sky Bolt", 100, damage=20)
# earth_hero = EarthHero("Ground Shatter", 150, damage=30)
#
# # Вызов метода для изменения hp и fly
# air_hero.multiply_hp()
# earth_hero.multiply_hp()
#
# # Проверка статуса полета
# air_hero.display_fly_status()  # вывод: Sky Bolt can fly: fly in the True_phrase
# earth_hero.display_fly_status()  # вывод: Ground Shatter can fly: fly in the True_phrase
#
# # Создание объекта для класса злодея
# villain = Villain("Dark Shadow", 200, damage=25)
#
# # Применение метода crit на объекте air_hero
# villain.damage = 10
# critical_damage = villain.crit()
# air_hero.hp -= critical_damage  # наносим критический урон
#
# # Проверка нового значения hp у air_hero
# print(f"{air_hero.name} HP after critical damage: {air_hero.hp}")  # вывод: Sky Bolt HP after critical damage: 99


# import requests
#
#
# def search_anime(query):
#     url = f"https://api.jikan.moe/v4/anime?q={query}&limit=10"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         anime_list = data['data']
#
#         if anime_list:
#             print(f"Результаты поиска для '{query}':\n")
#             for anime in anime_list:
#                 title = anime['title']
#                 synopsis = anime['synopsis']
#                 print(f"Название: {title}\nОписание: {synopsis}\n")
#         else:
#             print("Аниме не найдено.")
#     else:
#         print("Произошла ошибка при запросе данных.")
#
#
# if __name__ == "__main__":
#     query = input("Введите название аниме: ")
#     search_anime(query)
#
#
# class Cat:
    # def __init__(self):
        # self.hunger = 5  # уровень голода (0 - сытый, 10 - голоден)
        # self.energy = 5  # уровень энергии (0 - уставший, 10 - бодрый)
  # def eat(self):class
#         if self.hunger > 0:
#             self.hunger -= 1
#             self.energy += 1
#             self.happiness += 1
#             print("Мяу! Я поел, теперь я чувствую себя лучше!")
#         else:
#             print("Я не голоден!")
# #
# #     def sleep(self):
# #         if self.energy < 10:
# #             self.energy += 2
# #             self.happiness -= 1  # меньше активности, меньше счастья
# #             print("Сплю... Это так приятно!")
# #         else:
# #             print("Я не хочу спать, я уже полностью отдохнувший!")
# #
# #     def play(self):
# #         if self.energy > 0:
# #             self.energy -= 1
# #             self.happiness += 2
# #             print("Играть — это весело! Мяу!")
# #         else:
# #             print("Я слишком уставший, чтобы играть!")
# #
# #     def status(self):
# #         print(f"Уровень голода: {self.hunger}")
# #         print(f"Уровень энергии: {self.energy}")
# #         print(f"Уровень счастья: {self.happiness}")
# #       self.happiness = 5  # уровень счастья (0 - несчастный, 10 - счастливый)
#
#
#
# def main():
#     cat = Cat()
#
#     while True:
#         print("\nЧто ты хочешь сделать? (1 - поесть, 2 - поспать, 3 - поиграть, 4 - статус, 0 - выход)")
#         choice = input("Ваш выбор: ")
#
#         if choice == '1':
#             cat.eat()
#         elif choice == '2':
#             cat.sleep()
#         elif choice == '3':
#             cat.play()
#         elif choice == '4':
#             cat.status()
#         elif choice == '0':
#             print("До свидания!")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
#
# if __name__ == "__main__":
#     main()
#
#


#
#
#
# class TalkingTom:
#     def __init__(self):
#         self.hunger = 5  # Уровень голода (0 - сытый, 10 - голоден)
#         self.happiness = 5  # Уровень счастья (0 - несчастный, 10 - счастливый)
#
#     def speak(self, text):
#         print(f"Том говорит: '{text}'")
#
#     def eat(self):
#         if self.hunger > 0:
#             self.hunger -= 1
#             self.happiness += 1
#             print("Том поел и теперь чувствует себя лучше!")
#         else:
#             print("Том не голоден!")
#
#     def play(self):
#         if self.happiness < 10:
#             self.happiness += 2
#             self.hunger += 1  # Играет — немного голоден
#             print("Том играл и теперь весел!")
#         else:
#             print("Том слишком счастлив, он хочет отдохнуть!")
#
#     def status(self):
#         print(f"Уровень голода: {self.hunger}")
#         print(f"Уровень счастья: {self.happiness}")
#
#
# def main():
#     tom = TalkingTom()
#
#     while True:
#         print("\nЧто ты хочешь сделать?")
#         print("1 - Сказать что-то Тому")
#         print("2 - Поить Тома")
#         print("3 - Играть с Томом")
#         print("4 - Проверить состояние Тома")
#         print("0 - Выход")
#         choice = input("Ваш выбор: ")
#
#         if choice == '1':
#             text = input("Что ты хочешь сказать Тому? ")
#             tom.speak(text)
#         elif choice == '2':
#             tom.eat()
#         elif choice == '3':
#             tom.play()
#         elif choice == '4':
#             tom.status()
#         elif choice == '0':
#             print("До свидания!")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
#
# if __name__ == "__main__":
#     main(
# #
# class Bank:
# def__init__(self, name, balanse=0):
#         self.__name = name
#         self.__balanse = balanse
#
#
#     def moneyX(self):
#         amount = float(int(input("Эсебиңизге кошуу учун суманы киргизиниз:"))
#         if amount >1:
#             self.__balance += amount
#             print(f"Эсебинизге толугу менен кошулду.жаны баланс: {self.__balance}")
#          else:
#             print("Сумма оң болуусу керек. ")
#
#      def kill(self):
#         self.__balance = 0
#          print("Балансыныз ийгиликтуу калыбына келтирилди.")
#
#       def __jecpot(self):
#           self.__balance *= 10
#           print(f"Акчалуу джекпот! жаны баланс:  {self.__balance}")
#     def __bakai_bank(self, other ):
#         if isinstance(other, Bank):
#             self.__balance += other.__balance
#             other.__balance = 0
#             print(f"баланс ийгиликтуу кошулду.жаны баланс: {self.__balance}")
#         else:
#             print("баланс топтоо учун жараксыз обьект.")
#
#          def trigger_jacpot(self):
#              self.__jacpot()
#    if __name__ == "__main__":
#        umar = Bank("умар", 100)
#        ernis = Bank("эрнис",200)
#
#     umar.moneyX()
#     ernis.trigger_jacpot()
#
#     umar._bakai_bank_balance(ernis)
#

#
#
#
#
#
#     def moneyX(self):
#         amount = float(int(input("Эсебиңизге кошуу учун суманы киргизиниз:"))
#         if amount >1:
#             self.__balance += amount
#             print(f"Эсебинизге толугу менен кошулду.жаны баланс: {self.__balance}")
#          else:
#             print("Сумма оң болуусу керек. ")
#
#      def kill(self):
#         self.__balance = 0
#          print("Балансыныз ийгиликтуу калыбына келтирилди.")
#
#       def __jecpot(self):
#           self.__balance *= 10
#           print(f"Акчалуу джекпот! жаны баланс:  {self.__balance}")
#     def __bakai_bank(self, other ):
#         if isinstance(other, Bank):
#             self.__balance += other.__balance
#             other.__balance = 0
#             print(f"баланс ийгиликтуу кошулду.жаны баланс: {self.__balance}")
#         else:
#             print("баланс топтоо учун жараксыз обьект.")
#
#          def trigger_jacpot(self):
#              self.__jacpot()
#    if __name__ == "__main__":
#        umar = Bank("умар", 100)
#        ernis = Bank("эрнис",200)
#
#     umar.moneyX()
#     ernis.trigger_jacpot()
#
#     umar._bakai_bank_balance(ernis)



# #
# class Bank:
#     def __init__(self, name, balance=0):
#         self.__name = name          # Защищенный атрибут имени
#         self.__balance = balance    # Защищенный атрибут баланса
#
#     def moneyX(self):
#         amount = float(input(f"Введите сумму, которую хотите добавить на счет {self.__name}: "))
#         if amount > 0:
#             self.__balance += amount
#             print(f"Ваш баланс теперь: {self.__balance}")
#         else:
#             print("Сумма должна быть положительной.")
#
#     def kill(self):
#         """Обнулить баланс a"""
#         self.__balance = 0
#         print(f"Баланс {self.__name} был обнулен.")
#
#     def __jackpot(self):
#         """Умножает баланс на 10 (скрытый метод)"""
#         self.__balance *= 10
#         print(f"Ваш баланс умножен на 10: {self.__balance}")
#
#     def __combine_balance(self, other):
#         """Объединить баланс с другим объектом"""
#         if isinstance(other, Bank):
#             self.__balance += other.__balance
#             print(f"Баланс {self.__name} теперь: {self.__balance}")
#         else:
#             print("Можно объединять баланс только с другим объектом класса Bank.")
#
#     def show_balance(self):
#         """Метод для показа текущего баланса"""
#         print(f"Текущий баланс {self.__name}: {self.__balance}")
#
# # Пример использования
# bank_account_1 = Bank("Alice", 100)
# bank_account_2 = Bank("Bob", 100)
#
# trusted_input = input("Do you want to add money (y/n)? ")
# if trusted_input.lower() == 'y':
#     bank_account_1.moneyX()
#
# bank_account_1.show_balance()
# bank_account_2.show_balance()
#
# # Объединение баланса
# bank_account_1._Bank__combine_balance(bank_account_2)
# bank_account_1.show_balance()

#абстракция
# class InstallmentPlan:
#     def __init__(self, price):
#         self.price = price
#
#     def calculate_total_cost(self):
#         return self.price
#
#
# class FixedInstallment(InstallmentPlan):
#     def __init__(self, price, months):
#         super().__init__(price)
#         self.months = months
#
#     def calculate_total_cost(self):
#         # Фиксированные платежи - цена умноженная на количество месяцев
#         return self.price * self.months
#
#
# class VariableInstallment(InstallmentPlan):
#     def __init__(self, price, months, interest_rate):
#         super().__init__(price)
#         self.months = months
#         self.interest_rate = interest_rate
#
#     def calculate_total_cost(self):
#         # Переменные платежи с учетом процентов
#         total_with_interest = self.price * (1 + self.interest_rate / 100)  # цена с процентом
#         return total_with_interest * self.months
#
#
# # Создание объектов и вызов метода calculate_total_cost()
# fixed_plan = FixedInstallment(price=1000, months=12)
# variable_plan = VariableInstallment(price=1000, months=12, interest_rate=5)
#
# # Вычисление и вывод общей стоимости
# print(f"Fixed Installment Total Cost: {fixed_plan.calculate_total_cost()}")
# print(f"Variable Installment Total Cost: {variable_plan.calculate_total_cost()}")
#

