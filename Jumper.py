#print ("Welcome to Jumper! Jumper is an equation solver capable of solving 1 and 2 variable equations. The 2 variable solver is a bit slow.")
#from goto import goto, comefrom, label
import math
Check1 = 1
Check2 = 1
Check4 = 1
equation = ""
cvar = ""
resolution = 1
upperlimit = 0
equation = 0
varnum = 0
answerx = []
answery = []
#label .var2return
startnumber = 0
reslowbound = 0
resupperbound = 10
rescount = 0
initialres = 0
finalres = 0
jumper = startnumber
y = startnumber



#if (math.log10(initialres)) > 0:
#    resupperbound = math.log10(initialres)
#rescountmax = (math.log10(finalres)+math.log10(initialres))*-1
vlist = []
leqeqf = "equation[:eval(eqf)]"
#add rest of vars to fix errors
def helpsection(supportvar):
    if start == "help":
            print("insert help text")
def startup():
    global equation
    global resolution
    global cvar
    global upperlimit
    global equation
    global varnum
    global answerx
    global answery
    global startnumber
    global reslowbound
    global resupperbound
    global rescount
    global initialres
    global finalres
    global jumper
    global y
    global vlist
    global rescountmax
    global Check1
    global Check2
    equation = ""
    cvar = 0
    resolution = 1
    upperlimit = float(input("Upper Limit"))
    #dev(upperlimit)
    equation = input("Equation")
    #dev(equation)
    varnum = int(input("Number of Variables (1 or 2)"))
    #dev(varnum)
    answerx = ["x"]
    answery = ["Y"]
    #label .var2return
    startnumber = float(input("Starting Number"))
    #dev(startnumber)
    reslowbound = 0
    resupperbound = 10
    rescount = 0
    initialres = float(input("Initial Resolution"))
    #dev(initialres)
    finalres = float(input("Final Resolution"))
    #dev(finalres)
    jumper = startnumber
    y = startnumber
    resolution = initialres
    if (math.log10(initialres)) > 0:
        resupperbound = math.log10(initialres)
    rescountmax = (math.log10(finalres)+math.log10(initialres))*-1
    vlist = []
    print(rescount)
    
    
    while "x" in equation:
        print(equation)
        equation = ("".join([str(equation[:(equation.index("x"))]),"jumper",(equation[(len("x") + equation.index("x")):])]))
        #(len(equation)-int(equation.index("x")))
        print(equation)
    #print("".join([equation[:eqf(equation)], " > ", equation[eqf(equation):]]))
    equation = "".join([equation[:equation.index("=")], " > ", equation[equation.index("=") + 1:]])
    print(equation)
    y = startnumber
    if eval(equation) == True:
        Check1 = 1
        Check2 = 1
    else:
        Check1 = 0
        Check2 = 0
    print(Check1)
    print(Check2)
    print(equation)

    return(equation)
    return(resolution)
    return(upperlimit)
    return(varnum)
    return(answerx)
    return(answery)
    return(startnumber)
    return(reslowbound)
    return(resupperbound)
    return(rescount)
    return(initialres)
    return(finalres)
    return(jumper)
    return(rescountmax)
    return(vlist)
    return(cvar)

def reschange(jumper, resolution, rescount, rescountmax):
    if rescount < rescountmax:
            jumper = jumper - resolution
            resolution = resolution / 10
            rescount = rescount + 1
            print(rescount)
    return rescount
    return rescountmax
    return resolution
    return jumper
def question():
    supportvar = input("Would you like to start the equation solver?")
    if supportvar == "yes":
        print("startup")
    else:
        dev(supportvar)
        supportvar = input("Would you like to go to the help section?")
        if supportvar == "yes":
            helpsection
        else:
            dev(supportvar)
            supportvar = input("Exit program?")
            if supportvar == "yes":
                quit()
                exit()
            else:
                dev(supportvar)
                question(supportvar)
    return(supportvar)
def dev(supportvar):
    #cvar = "cvar"
    if "/" in supportvar:
        print(eval(supportvar[1:]))
#eqf= 'eval(equation.index("=")))'
def eqf(equation):
    if "=" in equation == True:
        return (equation.index("="))
#+1?
#jdc = 'float(equation.index("/jumper"))'
def jdc(equation,jumper):
    if "/jumper" in equation == True:
        return equation.index("/jumper")+1
#+1?
#jps = 'float(equation.index("jumper"))'
def jps(equation,jumper):
    if "jumper" in equation == True:
        return equation.index("jumper")+1
#+1?
answerstr = 0
supportvar = ""
start = ""
equationleft = ""
equationright = ""
start = input("Welcome to Jumper! Jumper is an equation solving program capable of solving equations with 1 or 2 variables. Respond start to continue. Respond help to go to the help section.")
#start = input("")
dev(start)
if start == "help":
    helpsection
#label .startup
startup()
print(jumper)
print(y)
print(varnum)
print(upperlimit)
print(equation)
#68
#      if ("math.sqrt(") in equation:
#          print(equation")
#74
    #label .return2
while (((jumper <= upperlimit) and (varnum == 1)) and not ((y <= upperlimit) and (varnum == 2))) == True and (jumper < 2 * upperlimit) == True:
    #label .resreturn
    print("while entered")
    jumper = (jumper + resolution)
    vlist = vlist + [jumper]
    if eval(equation) == True:
        Check1 = 1
    else:
        Check1 = 0
    if (Check1 == Check2) == False:
        if (Check1 == 1) == True:
            jumper = (jumper - resolution)
        if (rescount < rescountmax):
            reschange(jumper, resolution, rescount, rescountmax)
        if (rescount < rescountmax) and (Check1 != Check2):
            if varnum == 1:
                jumper = jumper - startnumber
                jumper = jumper + initialres
                print("".join(["The variable is equal to ", str(jumper), "."]))
            if (varnum == 2) and (y <= upperlimit):
                if ((reslowbound % 2) == 0 or (reslowbound == 1)) and ((jumper % 2) == 0 or (jumper == 1)):
                    answerx = answerx + [jumper]
                    answery = answery + [y]
                    print(answerx)
                    print(answery)
                reslowbound = reslowbound + 1
                jumper = jumper + finalres
                #goto .var2return
            question()
##            supportvar = input("Solve another equation?")
            ##dev(supportvar)
##            if supportvar == "no":
##                exit()
##            if supportvar == "yes":
##                startup()
            if rescount > rescountmax:
                print("Out of range")
    if (jumper >= upperlimit) and (y < upperlimit) and (varnum == 2):
        jumper = startnumber
        y = finalres + y
        #goto .return2
    if reslowbound != 0:
        reslowbound = 0
        supportvar = "sv"
            #goto .sv
        question()
      #label .sv
##      if supportvar == "sv":
##            supportvar = input("Go to the help section")
##            dev(supportvar)
##            if supportvar == "yes":
##                helpsection
##            else:
##                supportvar = input("Start Jumper?")
##                dev(supportvar)
##                if supportvar == "yes":
                    #goto .startup
      #label .reschange
      
            #goto .resreturn
print("end")
            
       
           
       
           
       
      
          

