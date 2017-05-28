import sys
import random

lvl = 1

#Класс протагониста##########################################################
class Me:
	def __init__(self, myname):
		self.myname = myname
		hp = 1000
		self.hp = hp

		if lvl == 1:                  #Алгоритм увеличивает урон
			dmg = 15                  #с переходом
		else:                         #на новый 
			dmg = 15 + ((lvl-1) * 10) #уровень
			
		self.dmg = dmg
	

	def myStats(self):
		print("Здоровье: ", self.hp, "Имя: ", self.myname, "Дамаг: ", self.dmg)

me = Me(input('Введи своё имя: '))

#################################имена уебков################################

goblinNames = ["Бульборок", "Киртан", "Горбаг", "Сталлемахс", "Шаграт", "Златотекс", "Веслолихс", "Грязнотукс", "Веслольс", "Сталлемутс"]

dworfNames = ["Бетмар", "Тауридун", "Бордар", "Аррин", "Крораг", "Мурамли", "Брадин", "Казйа", "Сенли", "Гоггераг"]

orkNames = ["Тралдан", "Кургтос", "Рагонок", "Кургрис", "Зумарис", "Гулгака", "Гулгатар", "Кургдан", "Зуманош", "Дабругар"]

trollNames = ["Ленго", "Зумбарала", "Растоджи", "Мунабул", "Джанга", "Торзулак", "Дентеш", "Денка", "Вельджин", "Вельтеш"]

########################классы уебков########################################

class Goblin:
	def __init__(self):
		hp = random.randint(45,60) #Задает гоблину хп в диапазоне
		self.hp = hp
		name = goblinNames[random.randint(0, len(goblinNames) - 1)] #Берет рандомное имя из списка с именами
		self.name = name

	def hit(self):
		chance = random.randint(0, 3) #Коэффицент шанса попадания\промаха

		if (chance == 1) or (chance == 2) or (chance == 3): #С шансом 3 к 4 ты пизданешь ублюдка
			self.hp -= me.dmg 
			if self.hp <= 0:
				print('Ты убил гоблина!') 
			else:
				print('Ты ударил гоблина!') 
		else:
			print('промах!') #С шансом 1 к 4 ты промажешь, лошара

	def stats(self):
		print('Здоровье: ', self.hp, 'Имя: ', self.name) #Показывает статы уебка (пока только здоровье и имя) 

	dmg = 5

	def hitHero(self):
		me.hp -= goblin.dmg
		print('Тебя пизданул гоблин, отняв 5 хп!')

#Построение классов для других уебков аналогично (от слова анал, ха)

class Dworf:
	def __init__(self):
		hp = random.randint(55,75)
		self.hp = hp
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
		print('Здоровье: ', self.hp, 'Имя: ', self.name)

	dmg = 7

	def hitHero(self):
		me.hp -= dworf.dmg
		print('Тебя пизданул дворф, отняв 7 хп!')

class Troll:
	def __init__(self):
		hp = random.randint(90,100)
		self.hp = hp
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
		print('Здоровье: ', self.hp, 'Имя: ', self.name)

	dmg = 10

	def hitHero(self):
		me.hp -= troll.dmg
		print('Тебя пизданул тролль, отняв 10 хп!')

class Ork:
	def __init__(self):
		hp = random.randint(110,160)
		self.hp = hp
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
		print('Здоровье: ', self.hp, 'Имя: ', self.name)

	dmg = 15

	def hitHero(self):
		me.hp -= ork.dmg
		print('Тебя пизданул гоблина, орк 15 хп!')

# LEVEL 1 #######################################################
print()
print("Приветствую тебя, ", me.myname, ', здесь должен быть какой-то сюжетный текст, но его не будет. Просто иди и пизди всех уёбков, которых встретишь далее. Подробнее о всей хуйне можно почитать в readme файле.')
print()
print("Перед тобой гоблин.")
print()
print("1.Пиздануть эту зеленую сраку")
print()
print("2.Показать имя и здоровье зеленого уёбка")
print()
print("3.Показать имя и здоровье великого тебя")
print()
print("4.Чтобы выйти из игры")
print()

#lvl += 1 #Увеличиваем коэффицент на еденицу с переходом на новый уровень, но на первом уровне этого делать не надо

goblin = Goblin() #Создаем экземпляр уебка

while (goblin.hp > 0):       #Хуячим уебка пока не сдохнет
	action = input()

	if action == '1': 
		goblin.hit()

	elif action == '2':
		goblin.stats()

	elif action == '3':
		me.myStats()

	elif action == '4':
		print('Пока')
		sys.exit()

	goblin.hitHero()

#Схема для других левелов аналогична

# LEVEL 2 #######################################################	

lvl += 1
dworf = Dworf()
print()
print("Перед тобой дворф.")
print()
print("1.Пиздануть карлана")
print()
print("2.Показать имя и здоровье низкорослика")
print()
print("3.Показать имя и здоровье великого тебя")
print()
print("4.Чтобы выйти из игры")
print()
while (dworf.hp > 0):
	action = input()

	if action == '1': 
		dworf.hit()

	elif action == '2':
		dworf.stats()

	elif action == '3':
		me.myStats()

	elif action == '4':
		print('Пока')
		sys.exit()

	dworf.hitHero()

# LEVEL 3 #######################################################

lvl += 1
troll = Troll()
print()
print("Перед тобой тролль.")
print()
print("1.Пиздануть этот вонючий хуй")
print()
print("2.Показать имя и здоровье неведомой хуиты")
print()
print("3.Показать имя и здоровье великого тебя")
print()
print("4.Чтобы выйти из игры")
print()
while (troll.hp > 0):
	action = input()

	if action == '1': 
		troll.hit()

	elif action == '2':
		troll.stats()

	elif action == '3':
		me.myStats()

	elif action == '4':
		print('Пока')
		sys.exit()

	troll.hitHero()
# LEVEL 4 ########################################################

lvl += 1
ork = Ork()
print()
print("Перед тобой орк.")
print()
print("1.Пиздануть перекаченного ублюдка")
print()
print("2.Показать имя и здоровье кочки")
print()
print("3.Показать имя и здоровье великого тебя")
print()
print("4.Чтобы выйти из игры")
print()
while (ork.hp > 0):
	action = input()

	if action == '1': 
		ork.hit()

	elif action == '2':
		ork.stats()

	elif action == '3':
		me.myStats()

	elif action == '4':
		print('Пока')
		sys.exit()

	troll.hitHero()
