import random
import time
cores = ["Ash Wand","Ivy Wand","Ivy Wand","Oak Wand","Willow Wand","Birch Wand","Reed Wand"]
helps =["Hermoine","Ron","Draco","Dudley"]
print("****----WELCOME TO HARRY POTTER'S WIZARD WORLD GAME----***** ")
print("--------------------------------------------------------------")

print("What is your first name?")
name = input(">>> ")

print("What is your last name?")
lastname = input(">>> ")


def welcome():  # intro

    print("To " + name + " " + lastname + ":")
    print("")
    print("-----We are pleased to inform you that you have been ----\n ---"
          "----accepted into Hogwarts School of Witchcraft and Wizardry.------")
    time.sleep(0.5)
    print("-----Please find enclosed a list of all necessary books and equipment.-----")
    time.sleep(0.5)
    print("------We await your acceptance owl no later than July 31.----")
    time.sleep(0.5)
    print("")
    print("-----------Term Begins on September the First.--------------")
    time.sleep(0.5)
    print("-----Take the train from Platform 9 3/4 at King's Cross Station.----")
    time.sleep(0.5)
    print("")
    print("-------Hogwarts School of Witchcraft and Wizardry----")
    time.sleep(0.5)
    print("")
    print("Do you accept? (y/n)")
    accept = input(">>> ").upper()
    if accept == "Y":
        Ollivanders()
    elif accept == "N":
        WowYouJustMissedAGreatChance()


def Ollivanders():  # wand

    print("You travel to Diagon Alley to do your school shopping.")
    print("Where do you get your wand?")
    print("")
    print("1. Delacour's")
    print("2. Gregorovich's Wands")
    print("3. Ollivanders: Makers of Fine Wands since 305 B.C.")
    print("")
    wandshop = input("1, 2, or 3? ")
    if wandshop == "1":
        print("----Delacour's isn't in village-----")
        print("*****choose again*******")
        Ollivanders()
    elif wandshop == "2":
        print("----His shop is closed----")
        print("********choose again********")
        Ollivanders()
    elif wandshop == "3":
        print("You're headed on the right track to be a great witch or wizard.")
        time.sleep(3)
        YourWand()
def YourWand():
    print("Welcome to Ollivander's!")
    print("")
    print("Are you most:")
    print("A. Kind and Generous")  # Ash
    print("B. Tenacious")  # Ivy
    print("C. A good leader")  # Holly
    print("D. Full of life")  # Birch
    print("E. Knowledgeable")  # Reed
    print("F. Strong and Flexible")  # Willow
    print("G. Confident and Optimistic")  # Oak
    print("")
    wood = input(">>> ").upper()
    core= random.choice(cores)
    print("")
    if wood == "A":
        print("You receive an  " + core)
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "B":
        print("You receive an  " + core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "C":
        print("You receive a " + core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "D":
        print("You receive a  " + core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "E":
        print("You receive a  " + core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "F":
        print("You receive a "+core )
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
    elif wood == "G":
        print("You receive an  "  + core)
        print("")
        print("**********Randomly***********")
        time.sleep(5)
        Platform934()
def Platform934():
	print("You need to get onto the platform. How do you get on?")
	print("")
	print("A. Stand between platforms nine and ten")
	print("B. Run at the barrier between platforms nine and ten")
	print("C. Fly a car to Hogwarts.")
	print("")
	platform = input(">>> ").upper()
	if platform == "A":
		print("Do you know anything about Harry Potter?")
		Platform934()
	elif platform == "B":
		print("You make it onto the platform and board the train.")
		time.sleep(5)
		Helping()
	elif platform == "C":
		print("Do you own a flying car?---- chose Again")
		Platform934()

def Helping():
    print("Now Hermoine and Ron are your friends at school")
    help =random.choice(helps)
    w=help
    print("")
    print("^^^"+help+"^^^^"+" Needs your help save your friend from woldmart")
    print("-------------------------------------")
    time.sleep(5)
    print("-----Choose a nor between(1-4) For partner----")
    H=input(">>").upper()
    if H=='1':
        Hermoine()
    elif H=='2':
        Ron()
    elif H=='3':
        Draco()
    else:
        Dudley()


def Hermoine():
    print("-------------------------------------")
    print(" You and hermoine are match for woldmart")
    time.sleep(3)
    print("you both killed woldmart")
    Win()
def Ron():
    print("-------------------------------------")
    time.sleep(3)
    print("You and Ron are match for woldmart")
    print("you both killed woldmart")
    Win()
def Draco():
    print("-------------------------------------")
    time.sleep(3)
    print("you both qurelled together")
    woldmart()
def Dudley():
    print("-------------------------------------")
    time.sleep(3)
    print("Dudley is lazy and careless")
    print("because of him you may loose")
    woldmart()
def Win():
    print("you win")
    time.sleep(3)
    print("-------The end--------")
    S=input("play again yes or no Y/N ?")
    if S==S:
        welcome()
    else:
        exit()
def woldmart():
    print("-------------------------------------")
    print("you are a coward")
    time.sleep(3)
    print("woldmart killed you and your friend")
    print("------The end----------")
def WowYouJustMissedAGreatChance():
	sure = input("Are you sure? y/n ")
	if sure == "n":
		Ollivanders()
	else:
		print("you missed great chance \n ------The end---------- ")
		exit()
welcome()