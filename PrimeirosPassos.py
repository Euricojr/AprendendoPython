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