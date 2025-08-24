#print("hello world")


#Drawing a Shape (Desenhar um triângulo) * A Ordem dos comandos influenciam

#print("   /|")
#print("  / |")
#print(" /  |")
#print("/___|")

#Variables and Datas Types


#Character_name = "Jhon" #String = text
#Character_age = "35" #Number
#isMale = False  #boolean value ( represent true or false data)
#print("There once was a man named " + Character_name + ".")
#print("he was "+ Character_age + " years old.")

#Character_name = "Mike"
#print("He really like the name " + Character_name + ",")
#print("but didn`t like being "+ Character_age + ".")

#Working with Strings (textos)
#phrase = "Giraffe Academy"
#print(phrase + "is cool")
#print("Giraffe\nAcademy")

#phrase = "Giraffe Academy"
         #0123
#print(phrase.upper().isupper()) #isupper()..........
#print(len(phrase))  #Função de comprimento
#print(phrase[0])
#print(phrase.index("a"))
#print(phrase.replace("Giraffe","Elephant"))

#Working with numbers
#print(3+4) # +,*,/, todas as operações
#my_num=5
#print(str(my_num) + " is my favorite number")
#print(abs(my_num)) #abs da o valor absoluto que esta ali ,
#print(pow(3,2)) #pow  vai permitir passar 2 tipos de informações, primeiro é o numero e segundo é o poder do numero, como se fosse elevar a algo
#print(max(4,6))
#print(round(3.9)) # serve para arredondar o número

#from math import *  #usa para usar outras funções
#print(floor(4.1)) #arredonda para baixo
#print(ceil(3.7))
#print(sqrt(3.1))

#Get input From Users  (permite que um usuário insira informações no programa)

#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " +name+ "! You are " + age  )

#Building a basic calculator

#num1 =  input("enter a number: ")
#num2 = input("enter another number: ")
#result=num1+num2
#print(result)    # torna uma string, dai a soma fica errada, só testar esse código

#num1 =  input("enter a number: ")
#num2 = input("enter another number: ")
#result= int(num1)+int(num2) #transforma em número, apenas numeros
#print(result)    #com número decimal, a função int da problema pois ela só considera número inteiro, para isso é preciso trocar para float

#num1 =  input("enter a number: ")
#num2 = input("enter another number: ")
#result= float(num1)+float(num2) #transforma em número, apenas numeros
#print(result)


#Mad libs Game (jogo de palavras)

#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")

#print("Roses are "+ color)
#print(plural_noun +" are blue")
#print("I love "+ celebrity)

#Lists (datas you need to organize)
#friends =["Kevin", "Karen", "Jim"] #usa os colchetes para mostrar que é uma lista
#friends[1] = "Mike"
#print(friends[1])

#List Functions
#lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends = ["Kevin", "Karen", "Jim","Jim", "Oscar", "Tim"]
#friends2 = friends.copy()
#print(lucky_numbers)

#friends.extend(lucky_numbers) # Junta tudo
#friends.append("Creed")
#friends.insert(1,"Kelly") #muda o objeto da lista na posição determinanda pelo index
#friends.remove("Jim")
#friends.pop() #tira o último da lista
#print(friends.index("Oscar")) #retorna seu numero

#print(friends.count("Jim",)) #retorna quantas vezes aquele objeto aparece
#friends.sort() #sort ele meio que serve para colocar em ordem *Tem o .reverse que vai colocar isso na ordem ao contrário
#print(friends)
#lucky_numbers.sort()
#print(lucky_numbers)

#Tuples (type of data structure) (can not change) só para dados que não mudarão com o tempo
#coordinates = (4, 5)
#print(coordinates[0])

#Functions
#def say_hi(name,age):
   # print("Hello " + name+  " you are " + str(age) + " years old.")
#say_hi("Mike",35)
#say_hi("Steve",70)

#Return Statement
#def cube(num):
    #return num * num * num

#num = input("numero:")   # essas duas linhas foram um improviso que fiz para tentar fazer uma calculadora ao cubo e deu certo
#print(cube(int(num)))

#result = cube(5)
#print(result)


#If Statements (uso do IF)
#is_male = False
#is_tall = False
#if is_male and is_tall:
    #print("You are a tall male")
#elif is_male and not(is_tall):
    #print("you are a short male")
#elif not is_male and is_tall:
    #print("you are not a male but are tall")
#else:
    #print("You are not a male nor tall")

#If statements and comparisons

#def max_num(num1,num2,num3):
    #if num1 >= num2 and num1 >= num3:
        #return num1
    #elif num2 >= num1 and num2 >= num3:
        #return num2
    #else:
        #return num3
#print(max_num(1000,20,3))


#Building a better calculator

#num1 = float(input("Enter first number: "))
#op = input("Enter operator: ")
#num2 = float(input("Enter second number: "))

#if op == "+":
    #print(num1 + num2)
#elif op == "-":
    #print(num1 - num2)
#elif op == "*":
    #print(num1 * num2)
#elif op == "/":
    #print(num1 / num2)
#else:
    #print("Invalid operator")


#dictionaries

#montConversions = {
    #"Jan": "January",
    #"Feb": "February",
    #"Mar": "March",
    #"Apr": "April",
    #"May": "May",
    #"Jun": "June",
    #"Jul": "July",
    #"Aug": "August",
    #"Sep": "September",
    #"Oct": "October",
    #"Nov": "November",
   #"Dec": "December"
#}

#print(montConversions.get("Nov", "not a value key")) #Se não tiver a kay correspondente vai retornar not a value key

#While loop (estrutura que permite percorrer e fazer e achar algo)

#i = 1
#while i <= 10:
    #print(i)
   #i += 1
#print("Done with loop")

#Building a Guessing game (jogo de adivinhar)

#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guess = False
#while guess != secret_word and not out_of_guess:
   # if guess_count < guess_limit:
        #guess = input("Enter guess: ")
        #guess_count += 1
    #else:
       # out_of_guess = True
#if out_of_guess:
    #print("You lose")
#else:
    #print("You win")

#For loop

#for letter in "Giraffe Academy":
   # print(letter)
# "Kevin"]
#for index in range(len(friends)):
    #print(friends[index])
#for index in range(5):
    #if index == 0:
        #print("First Iteraction")
    #else:
        #print("Second Iteraction")



#exponent function
#def raise_to_power(base_num, pow_num):
    #result =1
    #for index in range(pow_num):
        #result = result * base_num
    #return  result
#print(raise_to_power(2, 3))

#2d lists and nested loops

#number_grid = [
    #[1, 2, 3],
    #[4, 5, 6],
    #[7, 8, 9],
    #[0]
#]
#print (number_grid[2][1])

#for row in number_grid:
   #for col in row:
        #print(col)

#Build a Translator

#def translate(phrase):
    #translation = ""
    #for letter in phrase:
       # if letter.lower() in "aeiou":
            #if letter.isupper:
                #translation = translation + "G"
            #else:
                #translation = translation + "g"
        #else:
            #translation = translation + letter
    #return translation

#print(translate(input("Enter a phrase: ")))

#Try Except
#try:
    #value: 10 / 0
    #number = int(input("Enter a number :"))
    #print(number)
#except ZeroDivisionError:
    #print("Division by zero")
#except ValueError:
    #print("invalid input")


#Reading files

#employes_file = open("employes.txt", "r")
#print(employes_file.readable())
#print(employes_file.read())

#employes_file.close()

#Writing to files

#employes_file = open("employes.txt", "a")
#employes_file.write("\nKelly - Customer Service")
#employes_file.close()

#employes_file = open("employes1.txt", "w")
#employes_file.write("\nKelly - Customer Service")
#employes_file.close()

#Modules and Pip  // python model index buscar no site outros modules
#usa se o pip para instalar os modelos de python /// verificar se o pip esta no pc, so usar o terminarl do pycharm pip --version

#import useful_tools

#print(useful_tools.roll_dice(10))

#Classes and Objects

#from student import Student

#student1 = Student("Jim","business",3.2, False)
#print(student1.name)

#Building a Multiple Choice Quiz
#from Question import Question
#question_prompts = [
    #"What color are apples?\n (a)red/green\n (b) purple\n (c) orange\n\n",
    #"What color are Bananas?\n (a)teal\n (b) magenta\n (c) yellow\n\n ",
    #"What color are strawberries?\n (a)yellow\n (b) red\n (c) blue\n\n "
#]

#questions = [
    #Question(question_prompts[0], "a"),
    #Question(question_prompts[1], "c"),
    #Question(question_prompts[2], "b")
#]

#def run_test(questions):
    #score = 0
    #for question in questions:
        #answer = input(question.prompt)
        #if answer == question.answer:
            #score += 1
    #print("You got" + str(score) + "/" + str(len(questions)) + "correct")

#run_test(questions)


#Object Functions
#from student import Student
#student1 =Student("Jim","business",3.2)
#student2 = Student("Clara","business",3.8)

#print(student2.on_honor_roll())

#Inheritance (herdar)
#from Chef import Chef
#from ChineseChef import ChineaseChef

#myChef = Chef()
#myChef.make_speccial_dish()

#myChineseChef = ChineaseChef()
#myChineseChef.make_fried_rice()

#Python interpreter

