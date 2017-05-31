import sys
import random

lvl = 0

# Имена врагов ########################################################

goblinNames = ["Бульборок", "Киртан", "Горбаг", "Сталлемахс", "Шаграт",
	           "Златотекс", "Веслолихс", "Грязнотукс", "Веслольс",
	           "Сталлемутс"]

dworfNames = ["Бетмар", "Тауридун", "Бордар", "Аррин", "Крораг", "Мурамли",
              "Брадин", "Казйа", "Сенли", "Гоггераг"]

orkNames = ["Тралдан", "Кургтос", "Рагонок", "Кургрис", "Зумарис", "Гулгака",
            "Гулгатар", "Кургдан", "Зуманош", "Дабругар"]

trollNames = ["Ленго", "Зумбарала", "Растоджи", "Мунабул", "Джанга",
              "Торзулак", "Дентеш", "Денка", "Вельджин", "Вельтеш"]

dragonNames = ["Портурнакс", "Алдуин"]

# Создание классов ####################################################

class Creature:
	'''Суперкласс для всех существ'''
	#Выводит статы существа
	def stats(self):
		print("HP: ", self.hp)
		print("DMG: ", self.dmg)
		print("Race: ", self.race)
		print("Name: ", self.name)
	#Используется для нанесения урона протагонисту другими существами
	def hitHero(self):
		me.hp -= self.dmg
		if me.hp > 0:
			print("Вас ударил", self.race, ", отняв ", self.dmg, "урона")
		else:
			print("Вас убил", self.race, ", отняв ", self.dmg, "урона")
			print("Ты проиграл, лошара!")
			sys.exit()
	#Функия, обратная предыдущей
	def hitEnemy(self):
		self.hp -= me.dmg
		if self.hp > 0:
			print("Вы ударили", self.race, ", отняв", me.dmg, "урона")
		else:
			print("Вы убили", self.race, ", отняв", me.dmg, "урона")

class Protagonist(Creature):
	'''Класс протагониста'''
	def __init__(self, name):
		self.name = name

		hp = 100
		self.hp = hp

		race = "Человек"
		self.race = race

		if lvl == 1:                  
			dmg = 15                  
		else:                         
			dmg = 15 + ((lvl-1) * 13) 
		self.dmg = dmg

class Goblin(Creature):
	'''Класс гоблинов'''
	def __init__(self):
		hp = random.randint(45, 60)
		self.hp = hp
		race = "Гоблин"
		self.race = race
		dmg = 5
		self.dmg = dmg
		name = goblinNames[random.randint(0, len(goblinNames) - 1)] 
		self.name = name
 
class Dworf(Creature):
	'''Класс дворфов'''
	def __init__(self):
		hp = random.randint(55,75)
		self.hp = hp
		race = "Дворф"
		self.race = race
		dmg = 7
		self.dmg = dmg
		name = dworfNames[random.randint(0, len(dworfNames) - 1)]
		self.name = name

class Troll(Creature):
	'''Класс троллей'''
	def __init__(self):
		hp = random.randint(90,100)
		self.hp = hp
		race = "Тролль"
		self.race = race
		dmg = 10
		self.dmg = dmg
		name = trollNames[random.randint(0, len(trollNames) - 1)]
		self.name = name

class Ork(Creature):
	'''Класс орков'''
	def __init__(self):
		hp = random.randint(110,160)
		self.hp = hp
		race = "Орк"
		self.race = race
		dmg = 20
		self.dmg = dmg
		name = orkNames[random.randint(0, len(orkNames) - 1)]
		self.name = name

class Dragon(Creature):
	'''Класс драконов'''
	def __init__(self):
		hp = random.randint(150, 300)
		self.hp = hp
		race = "Дракон"
		self.race = race
		dmg = 30
		self.dmg = dmg
		name = dragonNames[random.randint(0, len(dragonNames) - 1)]
		self.name = name

name = input('Введи своё имя: ')

# LEVEL 1 #############################################################

lvl += 1
me = Protagonist(name)

print()
print("Приветствую тебя,", me.name)
print('Здесь должен быть какой-то сюжетный текст, но его не будет. ')
print('Просто иди и пизди всех уёбков, которых встретишь далее.')
print('Подробнее о всей хуйне можно почитать в readme файле.')
print()

goblin = Goblin()

print("Перед тобой гоблин.")
def cycleLVL1():
	print()
	print("1.Пиздануть эту зеленую сраку")
	print("2.Показать имя и здоровье зеленого уёбка")
	print("3.Показать имя и здоровье великого тебя")
	print("4.Чтобы выйти из игры")
	print()
cycleLVL1()
#Цикл выполняет действия, выбранные персонажем, пока не умрет сам
#персонаж или враг
#Для других уровней цикл аналогичный
while (goblin.hp > 0) and (me.hp > 0):       
	action = input()
	print()

	if action == '1':
		goblin.hitEnemy()
		if goblin.hp > 0:
			goblin.hitHero()

	elif action == '2':
		goblin.stats()

	elif action == '3':
		me.stats()

	elif action == '4':
		print('Пока')
		sys.exit()
	if goblin.hp > 0:
		cycleLVL1()

# LEVEL 2 #############################################################

lvl += 1
me = Protagonist(name)
dworf = Dworf()

print()
print("Перед тобой дворф.")
def cycleLVL2():
	print()
	print("1.Пиздануть карлана")
	print("2.Показать имя и здоровье низкорослика")
	print("3.Показать имя и здоровье великого тебя")
	print("4.Чтобы выйти из игры")
	print()
cycleLVL2()

while (dworf.hp > 0) and (me.hp > 0):
	action = input()
	print()

	if action == '1':
		dworf.hitEnemy()
		if dworf.hp > 0:
			dworf.hitHero()

	elif action == '2':
		dworf.stats()

	elif action == '3':
		me.stats()

	elif action == '4':
		print('Пока')
		sys.exit()
	if dworf.hp > 0:
		cycleLVL2()

# LEVEL 3 #############################################################

lvl += 1
me = Protagonist(name)
troll = Troll()

print()
print("Перед тобой тролль.")
def cycleLVL3():
	print()
	print("1.Пиздануть этот вонючий хуй")
	print("2.Показать имя и здоровье неведомой хуиты")
	print("3.Показать имя и здоровье великого тебя")
	print("4.Чтобы выйти из игры")
	print()
cycleLVL3()

while (troll.hp > 0) and (me.hp > 0):
	action = input()
	print()

	if action == '1':
		troll.hitEnemy()
		if troll.hp > 0:
			troll.hitHero()

	elif action == '2':
		troll.stats()

	elif action == '3':
		me.stats()

	elif action == '4':
		print('Пока')
		sys.exit()
	if troll.hp > 0:
		cycleLVL3()

# LEVEL 4 #############################################################

lvl += 1
me = Protagonist(name)
ork = Ork()

print()
print("Перед тобой орк.")
def cycleLVL4():
	print()
	print("1.Пиздануть перекаченного ублюдка")
	print("2.Показать имя и здоровье кочки")
	print("3.Показать имя и здоровье великого тебя")
	print("4.Чтобы выйти из игры")
	print()
cycleLVL4()

while (ork.hp > 0) and (me.hp > 0):
	action = input()
	print()

	if action == '1':
		ork.hitEnemy()
		if ork.hp > 0:
			ork.hitHero()

	elif action == '2':
		ork.stats()

	elif action == '3':
		me.stats()

	elif action == '4':
		print('Пока')
		sys.exit()
	if ork.hp > 0:
		cycleLVL4()

# LEVEL 5 #############################################################

lvl += 1
me = Protagonist(name)
dragon = Dragon()

print()
print("Смотри ка. Это, мать его, босс!")
print("Быстро дай ему банана, иначе он сам тебя пизданет!")
print()
print("Перед тобой дракон.")
def cycleLVL5():
	print()
	print("1.Пиздануть огнежопого")
	print("2.Показать имя и здоровье рептилоида")
	print("3.Показать имя и здоровье великого тебя")
	print("4.Чтобы выйти из игры")
	print()
cycleLVL5()

while (dragon.hp > 0) and (me.hp > 0):
	action = input()
	print()

	if action == '1':
		dragon.hitEnemy()
		if dragon.hp > 0:
			dragon.hitHero()

	elif action == '2':
		dragon.stats()

	elif action == '3':
		me.stats()

	elif action == '4':
		print('Пока')
		sys.exit()
	if dragon.hp > 0:
		cycleLVL5()
print()
print("Конгратулейшонс! Ты прошел эту ебучую игру.")