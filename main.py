import sys
import random

#Ставим первый уровень по умолчанию
lvl = 1

class Me:
	'''Класс протагониста'''
	def __init__(self, name):
		self.name = name
		hp = 1000
		self.hp = hp

		if lvl == 1:                  #Алгоритм увеличивает урон
			dmg = 15                  #с переходом
		else:                         #на новый
			dmg = 15 + ((lvl-1) * 13) #уровень

		self.dmg = dmg

	#Выведет статы протагониста
	def myStats(self):
		print("Здоровье: ", self.hp)
		print("Дамаг: ", self.dmg)
		print("Имя: ", self.name)

#Создаем единственный экземпляр протагониста
print()
me = Me(input('Введи своё имя: '))

#Имена врагов##########################################################

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

#Классы врагов#########################################################

class Goblin:
	'''Класс гоблинов'''
	def __init__(self):
		#Задает гоблину хп в диапазоне
		hp = random.randint(45,60) 
		self.hp = hp

		#Урон
		dmg = 5
		self.dmg = dmg

		#Берет рандомное имя из списка с именами
		name = goblinNames[random.randint(0, len(goblinNames) - 1)] 
		self.name = name

	def hit(self):
		#Коэффицент шанса попадания\промаха
		chance = random.randint(0, 3)

		#С шансом 3 к 4 ты пизданешь ублюдка
		if (chance == 1) or (chance == 2) or (chance == 3): 
			self.hp -= me.dmg
			if self.hp <= 0:
				print('Ты убил гоблина!')
			else:
				print('Ты ударил гоблина!')
		else:
			#С шансом 1 к 4 ты промажешь
			print('промах!') 

	def stats(self):
		#Показывает статы уебка (пока только здоровье и имя)
		print('Здоровье: ', self.hp) 
		print('Имя: ', self.name)

	

	def hitHero(self):
		me.hp -= self.dmg
		print()
		print('Тебя пизданул гоблин, отняв 5 хп!')

#Построение классов для других врагов аналогично

class Dworf:
	'''Класс дворфов'''
	def __init__(self):
		hp = random.randint(55,75)
		self.hp = hp

		dmg = 7
		self.dmg = dmg

		name = dworfNames[random.randint(0, len(dworfNames) - 1)]
		self.name = name

	def hit(self):
		chance = random.randint(0, 3)

		if (chance == 1) or (chance == 2) or (chance == 3):
			self.hp -= me.dmg
			if self.hp <= 0:
				print('Ты убил дворфа!')
			else:
				print('Ты ударил дворфа!')
		else:
			print('промах!')

	def stats(self):
		print('Здоровье: ', self.hp) 
		print('Имя: ', self.name)

	def hitHero(self):
		me.hp -= self.dmg
		print()
		print('Тебя пизданул дворф, отняв 7 хп!')

class Troll:
	'''Класс троллей'''
	def __init__(self):
		hp = random.randint(90,100)
		self.hp = hp

		dmg = 10
		self.dmg = dmg

		name = trollNames[random.randint(0, len(trollNames) - 1)]
		self.name = name

	def hit(self):
		chance = random.randint(0, 3)

		if (chance == 1) or (chance == 2) or (chance == 3):
			self.hp -= me.dmg
			if self.hp <= 0:
				print('Ты убил тролля!')
			else:
				print('Ты ударил тролля!')
		else:
			print('промах!')

	def stats(self):
		print('Здоровье: ', self.hp) 
		print('Имя: ', self.name)

	def hitHero(self):
		me.hp -= self.dmg
		print()
		print('Тебя пизданул тролль, отняв 10 хп!')

class Ork:
	'''Класс орков'''
	def __init__(self):
		hp = random.randint(110,160)
		self.hp = hp

		dmg = 15
		self.dmg = dmg

		name = orkNames[random.randint(0, len(orkNames) - 1)]
		self.name = name

	def hit(self):
		chance = random.randint(0, 3)

		if (chance == 1) or (chance == 2) or (chance == 3):
			self.hp -= me.dmg
			if self.hp <= 0:
				print('Ты убил орка!')
			else:
				print('Ты ударил орка!')
		else:
			print('промах!')

	def stats(self):
		print('Здоровье: ', self.hp) 
		print('Имя: ', self.name)

	

	def hitHero(self):
		me.hp -= self.dmg
		print()
		print('Тебя пизданул орк, отняв 15 хп!')

class Dragon:
	'''Класс драконов'''
	def __init__(self):
		hp = random.randint(150, 230)
		self.hp = hp

		dmg = 30
		self.dmg = dmg

		name = dragonNames[random.randint(0, len(dragonNames) - 1)]
		self.name = name

	def hit(self):
		chance = random.randint(0, 3)

		if (chance == 1) or (chance == 2) or (chance == 3):
			self.hp -= me.dmg
			if self.hp <= 0:
				print('Ты убил дракона!')
			else:
				print('Ты ударил дракона!')
		else:
			print('Ты промахнулся, еблан!')

	def stats(self):
		print('Здоровье: ', self.hp) 
		print('Имя: ', self.name)

	

	def hitHero(self):
		me.hp -= self.dmg
		print()
		print('Дракон поджарил тебе жопу, отняв 50 хп!')

# LEVEL 1 #############################################################
print()
print("Приветствую тебя,", me.name)
print('Здесь должен быть какой-то сюжетный текст, но его не будет. ')
print('Просто иди и пизди всех уёбков, которых встретишь далее.')
print('Подробнее о всей хуйне можно почитать в readme файле.')
print()
print("Перед тобой гоблин.")
print()
print("1.Пиздануть эту зеленую сраку")
print("2.Показать имя и здоровье зеленого уёбка")
print("3.Показать имя и здоровье великого тебя")
print("4.Чтобы выйти из игры")
print()

#Создаем экземпляр врага
goblin = Goblin() 

#Цикл позволяет выполять какие-либо действия пока не умрет враг
while (goblin.hp > 0):       
	action = input()
	print()

	if action == '1':
		goblin.hit()
		goblin.hitHero()

	elif action == '2':
		goblin.stats()

	elif action == '3':
		me.myStats()

	elif action == '4':
		print('Пока')
		sys.exit()
	print()

#Схема для других левелов аналогична

# LEVEL 2 #############################################################

lvl += 1
dworf = Dworf()
print()
print("Перед тобой дворф.")
print()
print("1.Пиздануть карлана")
print("2.Показать имя и здоровье низкорослика")
print("3.Показать имя и здоровье великого тебя")
print("4.Чтобы выйти из игры")
print()
while (dworf.hp > 0):
	action = input()
	print()

	if action == '1':
		dworf.hit()
		dworf.hitHero()

	elif action == '2':
		dworf.stats()

	elif action == '3':
		me.myStats()

	elif action == '4':
		print('Пока')
		sys.exit()
	print()

# LEVEL 3 #############################################################

lvl += 1
troll = Troll()
print()
print("Перед тобой тролль.")
print()
print("1.Пиздануть этот вонючий хуй")
print("2.Показать имя и здоровье неведомой хуиты")
print("3.Показать имя и здоровье великого тебя")
print("4.Чтобы выйти из игры")
print()
while (troll.hp > 0):
	action = input()
	print()

	if action == '1':
		troll.hit()
		troll.hitHero()

	elif action == '2':
		troll.stats()

	elif action == '3':
		me.myStats()

	elif action == '4':
		print('Пока')
		sys.exit()	
	print()

# LEVEL 4 #############################################################

lvl += 1
ork = Ork()
print()
print("Перед тобой орк.")
print()
print("1.Пиздануть перекаченного ублюдка")
print("2.Показать имя и здоровье кочки")
print("3.Показать имя и здоровье великого тебя")
print("4.Чтобы выйти из игры")
print()
while (ork.hp > 0):
	action = input()
	print()

	if action == '1':
		ork.hit()
		troll.hitHero()

	elif action == '2':
		ork.stats()

	elif action == '3':
		me.myStats()

	elif action == '4':
		print('Пока')
		sys.exit()
	print()

# LEVEL 5 #############################################################

lvl += 1
dragon = Dragon()

print("Смотри ка. Это, мать его, босс!")
print("Быстро дай ему банана, иначе он сам тебя пизданет!")
print()
print("Перед тобой дракон")
print()
print("1.Пиздануть огнежопого")
print("2.Показать имя и здоровье рептилоида")
print("3.Показать имя и здоровье великого тебя")
print("4.Чтобы выйти из игры")
print()

while (dragon.hp > 0):
	action = input()
	print()

	if action == '1':
		dragon.hit()
		dragon.hitHero()

	elif action == '2':
		dragon.stats()

	elif action == '3':
		me.myStats()

	elif action == '4':
		print('Пока')
		sys.exit()
	print()


 