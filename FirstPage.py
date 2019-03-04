import turtle
from turtle import *


turtle.bgpic("bg1.gif")



class Person():
    def __init__(self,name,gender,nationality,hub,job,age, image):
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.hub = hub
        self.job = job
        self.age = age
        self.image = image


tracer(0)
turtle.color("")
turtle.register_shape("akinator2.gif") 
akinator1 = turtle.clone()
akinator1.hideturtle()
akinator1.shape("akinator2.gif")
akinator1.goto(-260,-30)
akinator1.showturtle()

headline1 = turtle.Turtle()
headline1.hideturtle()
headline1.penup()
headline1.goto(0,250)
headline1.pendown()
headline1.showturtle()
headline1.write("AkiMEETor",align = 'center', font = ('fantasy', 70, 'normal'))
headline1.hideturtle()


turtle.register_shape("btn.gif") 
button1 = turtle.clone()
button1.hideturtle()
button1.shape("btn.gif")
button1.goto(50,60)
button1.showturtle()
 
button2 = turtle.clone()
button2.hideturtle()
button2.shape("btn.gif")
button2.goto(120,-40)
button2.showturtle()
 
headline2 = turtle.Turtle()
headline2.ht()
headline2.penup()
headline2.color("white")
headline2.goto(45,41)
headline2.pendown()
headline2.write("AKIMEETOR KNOWLEDGE",align='center',font=('Arial',22,'normal'))

headline3 = turtle.Turtle()
headline3.ht()
headline3.penup()
headline3.color("white")
headline3.goto(110,-65)
headline3.write("START",align='center',font=('Arial',32,'normal'))

yara = Person("Yara","F","P","Nazareth","coordinator",25, "yara1.gif")
ahmad = Person("Ahmad","M","P","Jerusalem","coordinator",23,"ahmad.gif")
nada = Person("Nada","F","P","Nazareth","coordinator",18,"nada.gif")
tasneem = Person("Tasneem","F","P","Nazareth","coordinator",23,"tasneem.gif")
boaz = Person("Boaz","M","I","Nazareth","coordinator",30,"boaz.gif")
loai = Person("Loai","M","P","Nazareth","Instructor",18,"loai.gif")
nizar= Person("Nizar","M","P","Nazareth","Instructor",23,"nuzar.gif")
ben = Person("Ben","M","I","Nazareth","TA",18,"ben.gif")
george = Person("George","M","P","Nazareth","TA",17,"george.gif")
sama = Person("Sama","F","P","Nazareth","TA",17,"samah.gif")
amir = Person("Amir","M","P","Nazareth","TA",17,"amir.gif")
mahmoud = Person("Mahmoud","M","P","Nazareth","TA",18,"mahmoud.gif")
abdallah = Person("Abdallah","M","P","Jerusalem","other",30,"abdallah.gif")
mustafa = Person("Mustafa", "M" , "P" , "Jerusalem" , "other" , 35 ,"mustafa.gif")
ted= Person("Ted" , "M", "A", "other", "Instructor", 30,"btn3.gif")
caleb= Person("Caleb", "M","A", "other", "Instructor", 21,"caleb.gif")
arnav= Person( "Arnav","M","A","other","Instructor",21,"arnaf.gif")

def start(x,y):
	global people

	people = [yara,ahmad,nada,tasneem,boaz,loai,nizar,ben,george,sama,amir,mahmoud,abdallah,mustafa,ted,caleb,arnav]

	print("start the game")
	global answer
	answer = ""
	turtle.clearscreen()
	turtle.bgpic("bg1.gif")

	turtle.color("")
	turtle.register_shape("akinator2.gif") 
	akinator1 = turtle.clone()
	akinator1.hideturtle()
	akinator1.shape("akinator2.gif")
	akinator1.goto(-260,-30)
	akinator1.showturtle()

	headline = turtle.Turtle()
	headline.hideturtle()
	headline.penup()
	headline.goto(0,250)
	headline.pendown()
	headline.showturtle()
	headline.write("AkiMEETor",align = 'center', font = ('fantasy', 70, 'normal'))
	headline.hideturtle()

	turtle.register_shape("bubble011.gif") 
	bubble1 = turtle.clone()
	bubble1.hideturtle()
	bubble1.shape("bubble011.gif")
	bubble1.goto(80,80)
	bubble1.showturtle()

	turtle.register_shape("button3.gif") 
	YesButton = turtle.clone()
	YesButton.hideturtle()
	YesButton.shape("button3.gif")
	YesButton.goto(50,-110)
	YesButton.showturtle()
	turtle.register_shape("button4.gif") 
	NoButton = turtle.clone()
	NoButton.hideturtle()
	NoButton.shape("button4.gif")
	NoButton.goto(50,-175)
	NoButton.showturtle()
	turtle.register_shape("button5.gif") 
	# button3 = turtle.clone()
	# button3.hideturtle()
	# button3.shape("button5.gif")
	# button3.goto(50,-240)
	# button3.showturtle()

	headline.penup()
	headline.color("white")
	headline.goto(50,-125)
	headline.pendown()
	headline.write("YES",align='center',font=('Arial',20,'normal'))
	headline.penup()
	headline.goto(50,-190)
	headline.pendown()
	headline.write("NO",align='center',font=('Arial',20,'normal'))


	Question = turtle.Turtle()
	Question.pu()
	Question.ht()
	Question.goto(60,120)
	Question.write("Question goes here...", move=False, align="center", font=("Arial", 24, "normal"))

	YesButton.pu()
	NoButton.pu()


	YesButton.st()
	NoButton.st()

	instructor=False
	TA=False
	coordinator=False
	    

	for i in range(len(basic_questions)):
	    Question.clear()
	    print(basic_questions[i])
	    Question.write(basic_questions[i], move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	    while answer=="":
	        YesButton.onclick(yes)
	        NoButton.onclick(no)
	        #print("waiting")

	    print("Answer is " + answer)
	        
	    if i == 0:
	        if answer=="No":
	            delete_females()
	            if tasneem in people:
	                people.remove(tasneem)
	                print("Removed Tasneem")
	        else:
	            delete_males()
	            if loai in people:
	                people.remove(loai)
	                print("Removed Loai")
	            if ben in people:
	                people.remove(ben)
	                print("Removed Ben")
	            if mahmoud in people:
	                people.remove(mahmoud)
	                print("Removed Mahmoud")
	            if mustafa in people:
	                people.remove(mustafa)
	                print("Removed Mustafa")
	            if caleb in people:
	                people.remove(caleb)
	                print("Removed Caleb")

	           
	            
	            
	            
	    if i == 1:
	        if answer=="No":
	            delete_palestinians()
	            if nada in people:
	                people.remove(nada)
	                print("Removed Nada")

	            if nizar in people:
	                people.remove(nizar)
	                print("Removed Nizar")
	                
	            if sama in people:
	                people.remove(sama)
	                print("Removed Sama")
	                
	            if abdallah in people:
	                people.remove(abdallah)
	                print("Removed Abdallah")
	           
	        else:
	            delete_Israelis()
	            delete_Americans()

	            if caleb in people:
	                people.remove(caleb)
	                print("Removed Caleb")
	    if i== 2:
	        if answer=="No":
	            delete_Israelis()
	        else:
	            delete_palestinians()
	            delete_Americans()
	            if caleb in people:
	                people.remove(caleb)
	                print("Removed Caleb")
	            if abdallah in people:
	                people.remove(abdallah)
	                print("Removed Abdallah")
	                
	            if nada in people:
	                people.remove(nada)
	                print("Removed Nada")

	                
	            if sama in people:
	                people.remove(sama)
	                print("Removed Sama")
	            
	    if i == 3:
	        if answer== "No":
	            delete_Nazareth()
	            if loai in people:
	                people.remove(loai)
	                print("Removed Loai")
	            if nizar in people:
	                people.remove(nizar)
	                print("Removed Nizar")
	            if sama in people:
	                people.remove(sama)
	                print("Removed Sama")
	            if george in people:
	                people.remove(george)
	                print("Removed George")
	            if amir in people:
	                people.remove(amir)
	                print("Removed Amir")
	            if mahmoud in people:
	                people.remove(mahmoud)
	                print("Removed Mahmoud")

	        else:
	            delete_Jerusalem()
	            delete_Other_Hub()
	            if ahmad in people:
	                people.remove(ahmad)
	                print("Removed Ahmad")
	            if caleb in people:
	                people.remove(caleb)
	                print("Removed Caleb")
	            if arnav in people:
	                people.remove(arnav)
	                print("Removed Arnav")
	            if ted in people:
	                people.remove(ted)
	                print("Removed Ted")
	    if i==4:
	        if answer == "No":
	            delete_Jerusalem()
	            if ahmad in people:
	                people.remove(ahmad)
	                print("Removed Ahmad")
	        else:
	            delete_Other_Hub()
	            delete_Nazareth()
	            if caleb in people:
	                people.remove(caleb)
	                print("Removed Caleb")
	            if arnav in people:
	                people.remove(arnav)
	                print("Removed Arnav")
	            if ted in people:
	                people.remove(ted)
	                print("Removed Ted")
	    if i==5:
	        if answer == "No":
	            delete_Instructors()
	            if loai in people:
	                people.remove(loai)
	                print("Removed Loai")
	            if nizar in people:
	                people.remove(nizar)
	                print("Removed Nizar")
	            if caleb in people:
	                people.remove(caleb)
	                print("Removed Caleb")
	            if arnav in people:
	                people.remove(arnav)
	                print("Removed Arnav")
	            if ted in people:
	                people.remove(ted)
	                print("Removed Ted")
	        else:
	            instructor=True
	            delete_coordinators()
	            delete_TAS()
	            delete_Other_Jobs()
	            if mustafa in people:
	                people.remove(mustafa)
	                print("Removed Mustafa")
	            if abdallah in people:
	                people.remove(abdallah)
	                print("Removed Abdallah")
	            if ben in people:
	                people.remove(ben)
	                print("Removed Ben")
	                
	            if boaz in people:
	                people.remove(boaz)
	                print("Removed Boaz")
	                

	            
	            #we should stop the loop 
	    if i==6:
	        if answer == "No":
	            delete_coordinators()
	            if boaz in people:
	                people.remove(boaz)
	                print("Removed Boaz")
	            if ahmad in people:
	                people.remove(ahmad)
	                print("Removed Ahmad")
	        else:
	            coordinator=True
	            delete_TAS()
	            delete_Other_Jobs()
	            delete_Instructors()
	            if mustafa in people:
	                people.remove(mustafa)
	                print("Removed Mustafa")
	            if abdallah in people:
	                people.remove(abdallah)
	                print("Removed Abdallah")
	            if ben in people:
	                people.remove(ben)
	                print("Removed Ben")
	            if caleb in people:
	                people.remove(caleb)
	                print("Removed Caleb")
	            if arnav in people:
	                people.remove(arnav)
	                print("Removed Arnav")
	            if ted in people:
	                people.remove(ted)
	                print("Removed Ted")
	            #we should stop the loop 
	    if i == 7:
	        if answer == "No":
	            delete_TAS()
	            if sama in people:
	                people.remove(sama)
	                print("Removed Sama")
	            if george in people:
	                people.remove(george)
	                print("Removed George")
	            if amir in people:
	                people.remove(amir)
	                print("Removed Amir")
	            if mahmoud in people:
	                people.remove(mahmoud)
	                print("Removed Mahmoud")
	            if ben in people:
	                people.remove(ben)
	                print("Removed Ben")
	            
	        else:
	            TA=True
	            delete_Other_Jobs()
	            delete_Instructors()
	            delete_coordinators()
	            if mustafa in people:
	                people.remove(mustafa)
	                print("Removed Mustafa")
	            if abdallah in people:
	                people.remove(abdallah)
	                print("Removed Abdallah")
	                
	            if tasneem in people:
	                people.remove(tasneem)
	                print("Removed Tasneem")

	            if nada in people:
	                people.remove(nada)
	                print("Removed Nada")
	                
	            if yara in people:
	                people.remove(yara)
	                print("Removed Yara")

	            if ahmad in people:
	                people.remove(ahmad)
	                print("Removed Ahmad")

	            Question.clear()
	            #we should stop the loop

	    answer = ""

	answer = ""

		########################################### Instructors ########################################### 
	if instructor:
	    Question.clear()
	    Question.write("Is he from MIT?", move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	    while answer=="":
	        YesButton.onclick(yes)
	        NoButton.onclick(no)
	    if answer=="Yes":
	        answer=""
	        if loai in people:
	            people.remove(loai)
	            print("Removed Loai")
	        if nizar in people:
	            people.remove(nizar)
	            print("Removed Nizar")

	        Question.clear()
	        Question.write("Does the person usually carries\n tons of Fireballs?", move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	        while answer=="":
	            YesButton.onclick(yes)
	            NoButton.onclick(no)
	        if answer=="Yes":
	            answer=""
	            if caleb in people:
	                people.remove(caleb)
	                print("Removed Caleb")
	            if arnav in people:
	                people.remove(arnav)
	                print("Removed Arnav")
	        
	        else:
	            if ted in people:
	                people.remove(ted)
	                print("Removed Ted")
	            answer=""
	            Question.clear()
	            Question.write("Is the person blonde?", move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	            while answer=="":
	                YesButton.onclick(yes)
	                NoButton.onclick(no)
	            if answer=="Yes":
	                answer=""
	                if arnav in people:
	                    people.remove(arnav)
	                    print("Removed Arnav")

	            else:
	            	answer=""
	                if caleb in people:
	                    people.remove(caleb)
	                    print("Removed Caleb")          
	    else:
	        answer=""
	        if ted in people:
	            people.remove(ted)
	            print("Removed Ted")
	        if caleb in people:
	            people.remove(caleb)
	            print("Removed Caleb")
	        if arnav in people:
	            people.remove(arnav)
	            print("Removed Arnav")

	        answer=""
	        Question.clear()
	        Question.write("Does the person love ducks?", move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	        while answer=="":
	            YesButton.onclick(yes)
	            NoButton.onclick(no)
	            if answer=="Yes":
	                answer=""
	                if loai in people:
	                    people.remove(loai)
	                    print("Removed Loai :(")
	            else:
	            	answer = ""
	                if nizar in people:
	                    people.remove(nizar)
	                    print("Removed Nizar")

	##################################################################################### 

	if TA:
	    Question.clear()
	    Question.write("Does he usually come \n on Mondays?", move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	    while answer=="": 
	        YesButton.onclick(yes)
	        NoButton.onclick(no)
	    if answer=="Yes":
	        answer=""
	        if george in people:
	            people.remove(george)
	            print("Removed George")
	        if mahmoud in people:
	            people.remove(mahmoud)
	            print("Removed Mahmoud")

	    else:
	        answer=""
	        if sama in people:
	            people.remove(sama)
	            print("Removed Sama")

	        if ben in people:
	                people.remove(ben)
	                print("Removed Ben")

	        if amir in people:
	            people.remove(amir)
	            print("Removed Amir")
	            
	        Question.clear()
	        Question.write("Does he wear glasses?", move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	        while answer=="":
	            YesButton.onclick(yes)
	            NoButton.onclick(no)
	        if answer=="Yes":
	            answer=""
	            if mahmoud in people:
	                people.remove(mahmoud)
	                print("Removed Mahmoud")
	              
	        else:
	            answer=""
	            if george in people:
	                people.remove(george)
	                print("Removed George")

	#####################################################################################


	if coordinator:
	    if ahmad in people:
	        if tasneem in people:
	            people.remove(tasneem)
	            print("Removed Tasneem")

	        if yara in people:
	            people.remove(yara)
	            print("Removed Yara")
	        if nada in people:
	            people.remove(nada)
	            print("Removed Nada")
	    elif boaz in people:
	        if tasneem in people:
	            people.remove(tasneem)
	            print("Removed Tasneem")

	        if yara in people:
	            people.remove(yara)
	            print("Removed Yara")
	        if nada in people:
	            people.remove(nada)
	            print("Removed Nada")
	    else:
	        Question.clear()
	        Question.write("Is the person short?", move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	        while answer=="":
	            YesButton.onclick(yes)
	            NoButton.onclick(no)
	        if answer=="Yes":
	            answer=""
	            
	            if tasneem in people:
	                people.remove(tasneem)
	                print("Removed Tasneem")

	            if yara in people:
	                people.remove(yara)
	                print("Removed Yara")

	        else:
	            answer=""
	            if nada in people:
	                people.remove(nada)
	                print("Removed Nada")

	            Question.clear()
	            Question.write("Does the person speak \n korean?", move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	            while answer=="":
	                YesButton.onclick(yes)
	                NoButton.onclick(no)
	            if answer=="Yes":
	                answer=""
	                if yara in people:
	                    people.remove(yara)
	                    print("Removed Yara")
	            else:
	                answer=""
	                if tasneem in people:
	                    people.remove(tasneem)
	                    print("Removed Tasneem")

	other_jobs=False
	if instructor== False and TA== False and coordinator== False:
	    other_jobs= True
	        
	if other_jobs:
	    answer=""
	    Question.clear()
	    Question.write("Is he a father?", move=False, align="center", font=("Arial", 24, "normal")) #show question on screen.
	    while answer=="":
	        YesButton.onclick(yes)
	        NoButton.onclick(no)
	    if answer=="Yes":
	        answer=""
	        if abdallah in people:
	            people.remove(abdallah)
	            print("Removed Abdallah")
	        if ahmad in people:
	            people.remove(ahmad)
	            print("Removed Ahmad")
	    else:
	        answer=""
	        if mustafa in people:
	            people.remove(mustafa)
	            print("Removed Mustafa")


		            
	for i in people:
	    print (i.name)
	    turtle.register_shape(i.image)
	    turtle.shape(i.image)
	


button2.onclick(start)
headline3.onclick(start)


def akimeetor_knowledge(x,y):
	turtle.clearscreen()
	turtle.bgpic("watercolor1.gif")

	turtle.hideturtle()
	turtle.penup()
	turtle.goto(0,150)
	turtle.write("AKIMEETOR'S KNOWLEDGE",align='center',font=("David","50","normal"))
	ppl_list=turtle.clone()
	ppl_list.goto(0,14)
	ppl_list.write("Sama,  "
	               "Amir,  "
	               "Mahmoud,  "
	               "Abdallah,  "
	               "Mustafa,  "
	               "Ted,  "
	               "Caleb,  "
	               "Arnav",align='center',font=("Ariel","18","normal"))
	ppl_list2=turtle.clone()
	ppl_list2.goto(0,-15)
	ppl_list2.write("Yara,  "
	               "Ahmad,  "
	               "Nada,  "
	               "Tasneem,  "
	               "Boaz,  "
	               "Loai,  "
	               "Nizar,  "
	               "Ben,  "
	               "George  ",align='center',font=("Ariel","18","normal"))
	turtle.hideturtle()
	turtle.color('yellow')
	turtle.speed(.1)
	turtle.pensize(7)
	turtle.penup()
	turtle.goto(-450,60)
	turtle.pendown()
	turtle.goto(450,60)
	turtle.goto(450,-30)
	turtle.goto(-450,-30)
	turtle.goto(-450,60)
	turtle.showturtle()


	turtle.Screen().onclick(gotoFirstPage)
	turtle.mainloop()
	return
button1.onclick(akimeetor_knowledge)
headline2.onclick(akimeetor_knowledge)


def gotoFirstPage(x,y):
	turtle.clearscreen()
	turtle.bgpic("bg1.gif")

	turtle.color("")
	turtle.register_shape("akinator2.gif") 
	akinator1 = turtle.clone()
	akinator1.hideturtle()
	akinator1.shape("akinator2.gif")
	akinator1.goto(-260,-30)
	akinator1.showturtle()

	headline1 = turtle.Turtle()
	headline1.hideturtle()
	headline1.penup()
	headline1.goto(0,250)
	headline1.pendown()
	headline1.showturtle()
	headline1.write("AkiMEETor",align = 'center', font = ('fantasy', 70, 'normal'))
	headline1.hideturtle()


	turtle.register_shape("btn.gif") 
	button1 = turtle.clone()
	button1.hideturtle()
	button1.shape("btn.gif")
	button1.goto(50,60)
	button1.showturtle()
	 
	button2 = turtle.clone()
	button2.hideturtle()
	button2.shape("btn.gif")
	button2.goto(120,-40)
	button2.showturtle()
	 
	headline2 = turtle.Turtle()
	headline2.ht()
	headline2.penup()
	headline2.color("white")
	headline2.goto(45,41)
	headline2.pendown()
	headline2.write("AKIMEETOR KNOWLEDGE",align='center',font=('Arial',22,'normal'))

	headline3 = turtle.Turtle()
	headline3.ht()
	headline3.penup()
	headline3.color("white")
	headline3.goto(110,-65)
	headline3.write("START",align='center',font=('Arial',32,'normal'))

	button1.onclick(akimeetor_knowledge)
	headline2.onclick(akimeetor_knowledge)

	button2.onclick(start)
	headline3.onclick(start)



#################################################################################3
# tracer(0)

basic_questions = ["Is the person a female?","Is the person Palestinian?","Is the person Israeli?","Is the person from the \n Nazareth hub?","Is the person from the \n Jerusalem hub?" ,"Is the person an Instructor?","Is the person a Coordinator?","Is the person a TA?"]

def delete_females():
    for person in people:
        if person.gender == "F":
            people.remove(person)
            print ("Removed " + person.name)
            
def delete_males():
    for person in people:
        if person.gender == "M":
            people.remove(person)
            print ("Removed " + person.name)
def delete_palestinians():
    for person in people:
            if person.nationality=="P":
                people.remove(person)
                print("Removed " + person.name)


def delete_Israelis():
    for person in people:
            if person.nationality=="I":
                people.remove(person)
                print("Removed " + person.name)


def delete_Americans():
    for person in people:
            if person.nationality=="A":
                people.remove(person)
                print("Removed " + person.name)


def delete_Nazareth():
    for person in people:
            if person=="Nazareth":
                people.remove(person)
                print("Removed " + person.name)


def delete_Jerusalem():
    for person in people:
            if person.nationality=="Jerusalem":
                people.remove(person)
                print("Removed " + person.name)


def delete_Other_Hub():
    for person in people:
            if person.nationality=="other":
                people.remove(person)
                print("Removed " + person.name)


def delete_coordinators():
    for person in people:
            if person.nationality=="coordinator":
                people.remove(person)
                print("Removed " + person.name)


def delete_Instructors():
    for person in people:
            if person.nationality=="Instructor":
                people.remove(person)
                print("Removed " + person.name)


def delete_TAS():
    for person in people:
            if person.nationality=="TA":
                people.remove(person)
                print("Removed " + person.name)


def delete_Other_Jobs():
    for person in people:
            if person.nationality=="other":
                people.remove(person)
                print("Removed " + person.name)
    


def yes(x,y):
    global answer
    answer = "Yes"
    return

def no(x,y):
    global answer
    answer = "No"
    return

#############################



update()
turtle.mainloop()