############################################################
# OBSERVAÇÃO IMPORTANTE:
# Para testar cada tópico, basta tirar o símbolo "#" da frente
# da linha de código que você quiser executar.
############################################################



############################################################
# PRINT BÁSICO
############################################################

#print("hello world")



############################################################
# DESENHANDO FORMAS
# A ordem dos comandos no print influencia o desenho.
############################################################

#print("   /|")
#print("  / |")
#print(" /  |")
#print("/___|")



############################################################
# VARIÁVEIS E TIPOS DE DADOS
# Exemplos de string (texto), número e booleano (verdadeiro/falso).
############################################################

#Character_name = "Jhon" #String = text
#Character_age = "35" #Number
#isMale = False  #boolean value ( represent true or false data)

#print("There once was a man named " + Character_name + ".")
#print("he was "+ Character_age + " years old.")

#Character_name = "Mike"
#print("He really like the name " + Character_name + ",")
#print("but didn`t like being "+ Character_age + ".")



############################################################
# STRINGS (trabalhando com textos)
############################################################

#phrase = "Giraffe Academy"
#print(phrase + "is cool")
#print("Giraffe\nAcademy")

#phrase = "Giraffe Academy"
         #0123
#print(phrase.upper().isupper())
#print(len(phrase))
#print(phrase[0])
#print(phrase.index("a"))
#print(phrase.replace("Giraffe","Elephant"))



############################################################
# NÚMEROS E OPERAÇÕES
############################################################

#print(3+4)
#my_num=5
#print(str(my_num) + " is my favorite number")
#print(abs(my_num))
#print(pow(3,2))
#print(max(4,6))
#print(round(3.9))

#from math import *
#print(floor(4.1))
#print(ceil(3.7))
#print(sqrt(3.1))



############################################################
# INPUT DO USUÁRIO
# Permite que o usuário digite informações.
############################################################

#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " +name+ "! You are " + age  )



############################################################
# CALCULADORA SIMPLES
############################################################

#num1 =  input("enter a number: ")
#num2 = input("enter another number: ")
#result=num1+num2
#print(result)

#num1 =  input("enter a number: ")
#num2 = input("enter another number: ")
#result= int(num1)+int(num2)
#print(result)

#num1 =  input("enter a number: ")
#num2 = input("enter another number: ")
#result= float(num1)+float(num2)
#print(result)



############################################################
# JOGO DE PALAVRAS (Mad Libs)
############################################################

#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")

#print("Roses are "+ color)
#print(plural_noun +" are blue")
#print("I love "+ celebrity)



############################################################
# LISTAS
############################################################

#friends =["Kevin", "Karen", "Jim"]
#friends[1] = "Mike"
#print(friends[1])



############################################################
# FUNÇÕES DE LISTAS
############################################################

#lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends = ["Kevin", "Karen", "Jim","Jim", "Oscar", "Tim"]
#friends2 = friends.copy()
#print(lucky_numbers)

#friends.extend(lucky_numbers)
#friends.append("Creed")
#friends.insert(1,"Kelly")
#friends.remove("Jim")
#friends.pop()
#print(friends.index("Oscar"))
#print(friends.count("Jim",))
#friends.sort()
#print(friends)
#lucky_numbers.sort()
#print(lucky_numbers)



############################################################
# TUPLAS (DADOS FIXOS)
############################################################

#coordinates = (4, 5)
#print(coordinates[0])



############################################################
# FUNÇÕES
############################################################

#def say_hi(name,age):
   # print("Hello " + name+  " you are " + str(age) + " years old.")

#say_hi("Mike",35)
#say_hi("Steve",70)



############################################################
# RETURN STATEMENT
############################################################

#def cube(num):
    #return num * num * num

#num = input("numero:")
#print(cube(int(num)))

#result = cube(5)
#print(result)



############################################################
# IF STATEMENTS
############################################################

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



############################################################
# IF + COMPARAÇÕES
############################################################

#def max_num(num1,num2,num3):
    #if num1 >= num2 and num1 >= num3:
        #return num1
    #elif num2 >= num1 and num2 >= num3:
        #return num2
    #else:
        #return num3
#print(max_num(1000,20,3))



############################################################
# CALCULADORA MELHORADA
############################################################

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



############################################################
# DICIONÁRIOS
############################################################

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

#print(montConversions.get("Nov", "not a value key"))



############################################################
# WHILE LOOP
############################################################

#i = 1
#while i <= 10:
    #print(i)
   #i += 1
#print("Done with loop")



############################################################
# JOGO DA ADIVINHAÇÃO
############################################################

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



############################################################
# FOR LOOP
############################################################

#for letter in "Giraffe Academy":
    #print(letter)

#for index in range(len(letter)):
    #print(letter[index])

#for index in range(5):
    #if index == 0:
        #print("First Interaction")
    #else:
        #print("Second Interaction")



############################################################
# FUNÇÃO DE EXPONENCIAÇÃO
############################################################

#def raise_to_power(base_num, pow_num):
    #result =1
    #for index in range(pow_num):
        #result = result * base_num
    #return  result
#print(raise_to_power(2, 3))



############################################################
# LISTAS 2D E LOOPS ANINHADOS
############################################################

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



############################################################
# TRADUTOR SIMPLES
############################################################

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



############################################################
# TRY / EXCEPT
############################################################

#try:
    #value: 10 / 0
    #number = int(input("Enter a number :"))
    #print(number)
#except ZeroDivisionError:
    #print("Division by zero")
#except ValueError:
    #print("invalid input")



############################################################
# ARQUIVOS: LENDO E ESCREVENDO
############################################################

#employes_file = open("employes.txt", "r")
#print(employes_file.readable())
#print(employes_file.read())
#employes_file.close()

#employes_file = open("employes.txt", "a")
#employes_file.write("\nKelly - Customer Service")
#employes_file.close()

#employes_file = open("employes1.txt", "w")
#employes_file.write("\nKelly - Customer Service")
#employes_file.close()



############################################################
# MÓDULOS E PIP
############################################################

#import useful_tools
#print(useful_tools.roll_dice(10))



############################################################
# CLASSES E OBJETOS
############################################################

#from student import Student
#student1 = Student("Jim","business",3.2, False)
#print(student1.name)



############################################################
# QUIZ DE MÚLTIPLA ESCOLHA
############################################################

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



############################################################
# FUNÇÕES EM OBJETOS
############################################################

#from student import Student
#student1 =Student("Jim","business",3.2)
#student2 = Student("Clara","business",3.8)
#print(student2.on_honor_roll())



############################################################
# HERANÇA (INHERITANCE)
############################################################

#from Chef import Chef
#from ChineseChef import ChineaseChef

#myChef = Chef()
#myChef.make_special_dish()

#myChineseChef = ChineaseChef()
#myChineseChef.make_fried_rice()



#############################################################
# PYTHON INTERPRETER
#############################################################
