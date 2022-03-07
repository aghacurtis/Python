import sys
import time
import random
from random import randint

def typewrite(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.000005)

from colorama import Fore, Back, Style


#make chatbot ask question using typewriting effect
typewrite(Fore.YELLOW + "ChatBot: Hi friend! im chatbot your automated friend! So, how are u... WAIT i dont know ur name , please tell me friend: ")
#where the user can input connected to a variable so the bot remembers the name
name = input(Fore.BLUE + "\n You: ")
#continues conversation refrencing the "name" variable to make it appear as if the computer listened and replied with the name.
typewrite(Fore.YELLOW + "What a great name!I would love to know more about you "+ name)
#adds anoyher question 
typewrite(Fore.YELLOW + "\nHow about the year u were born?" )
#New variable for the user to input their birth year
Birth_Year = input(Fore.BLUE + "\n You:")
#mathmatical question to work out the users age
age = 2021 - int(Birth_Year)
#resets teh colours and style of text
print(Style.RESET_ALL)
#warning to user that system will nuot understand if they type anything but "yes" and "no"
typewrite(Back.RED + "!if asked a question always reply with yes or no or chatbot will not understand!")
#resets colours and styles again
print(Style.RESET_ALL)
#writes down the users details
user = open(name+ "'s_file.py", "w")
user.write("name =")
user.write( name)
user.write('\n')
user.write("Birth_Year =")
user.write(Birth_Year)
user.write('\n')
user.write("age = ")
user.write(str(age))
user.write('\n')
user.close()
#asks a new question
typewrite(Fore.YELLOW + "ChatBot: its so fun being friends with you \nwould u like to play a game?")
#players input
game = input(Fore.BLUE + "\n You:")
#if statement saying that if the player replies yes it will say sometihng then begin the game
if game == "yes":
    typewrite(Fore.YELLOW + " ChatBot: wonderful, i would love to play with u , lets begin")
#elif saying that if the player replies no it will say goodbye and end the program    
elif game == "no":
    typewrite(Fore.YELLOW + "ChatBot:Lets play another time! cya later " + name)
    quit()
#else statement for if the user types anything but yes or no , to end the proccess    
else:
    print(Style.RESET_ALL)
    typewrite(Back.RED +" ChatBot: i dont quite understand \n --------- REBOOTING ---------")
    quit()
#a new variable linking to a mathmatical question 
question_1 = typewrite(Fore.YELLOW + "\n ChatBot: so friend... lets see how ur maths skills are. Whats 4x12 ")
#a new variable for the players input so that we can checck if they got it right
maths_1 = input(Fore.BLUE + "\n You:")
#variables sshowing the players score and the bots score for further things
player_score = 0
bot_score = 0
#if statement saying that if the player replies with the correct answer , 48 , it will congratulate them and add 1 to their score
if maths_1 =="48":
    typewrite(Fore.YELLOW + "Congrats friend! You got it correct! thats one point to you.")
    #adding 1 value to out previous variable which is the players sccore
    player_score += 1
    #reseting style 
    print(Style.RESET_ALL)
    #presenting the score in the game with a green backround
    print(Back.GREEN +" Your score is now ", str(player_score), "and my score is " + str(bot_score))
    #resetting style
    print(Style.RESET_ALL)
#else statement to say that if the user replies anything BUT 48 it will tell them they are incorrect
else:
    typewrite(Fore.YELLOW + "ah thats incorrect meaning i get a point.")
    #adding 1 value to out previous variable which is the bots sccore
    bot_score +=1
    #reseting style
    print(Style.RESET_ALL)
    #presenting the score in the game with a green backround
    print(Back.GREEN +" Your score is ", str(player_score), "and my score is " + str(bot_score))
    #reseting style
    print(Style.RESET_ALL)
 #asking a new question preparing for an if statement
typewrite(Fore.YELLOW  + "so would u like to continue?")
#players input linked to a new variable
continue_1 = input("\n You:")

#using the new variable an if statement to say that if the user says yes it continues 
if continue_1 == "yes":
    typewrite(Fore.YELLOW + "ChatBot: Great im so happy to continue this friend!")
    question_2 = True
#an elif statement to say that if the user says no it says goodbye and ends the program
elif game == "no":
    typewrite(Fore.YELLOW + "\n ChatBot: oh :( thats fine we can play another time! cya later "+name )
    question_2 = False
#else statement to say that if the user says anything but yes or no the procces will end 
else:
    print(Style.RESET_ALL)
    typewrite(Back.RED +" ChatBot: i dont quite understand \n --------- REBOOTING ---------")
    print(Style.RESET_ALL)
    question_2 = False
    quit()

#the start of a new game 
typewrite("\nHow about a guessing game, im thinking of a number between 1 and 5, guess, if u get it right u get a point if u get it wrong i get a point.")
typewrite("\nok i got it \n")
#new variaable using the randint function to choose a number
bots_number = random.randint(1,6)
#new variable for the player to input what they think the number is 
players_guess = input("You: ")

#if statement saying if the player guesses the number correct the bot says congrats
if int(players_guess) != bots_number:
    #resets style
    (Back.GREEN + "Im sorry i chose", bots_number, "and you chose", players_guess, "meaning i get a point")
    
#else statement saying that if the player guesses anything but hte correct answer they are wrong and it gives bot a point
elif int(players_guess) == bots_number:
    print(Back.GREEN + "Congrats i chose", bots_number,  "you chose", players_guess,"meaning u get a point!")

