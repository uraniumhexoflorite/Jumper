import math

equation = ""
resolution = 0
cvar = 0
upperlimit = 0
varnum = 0
answerx = []
answery = []
startnumber = 0
reslowbound = 0
resupperbound = 0
rescount = 0
initialres = 0
finalres = 0
jumper = 0
y = 0
vlist = []
rescountmax = 0
Check1 = 0
Check2 = 0
supportvar = ""
# if (math.log10(initialres)) > 0:
#    resupperbound = math.log10(initialres)
# rescountmax = (math.log10(finalres)+math.log10(initialres))*-1
leqeqf = "equation[:eval(eqf)]"
# add rest of vars to fix errors
#def helpsection(supportvar):
#    if start == "help":
#        print("insert help text")
def startup():
    # equation,resolution,cvar,upperlimit,varnum,answerx,answery,startnumber,reslowbound,resupperbound,rescount,initialres,finalres,jumper,y,vlist,rescountmax,Check1,Check2
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
    # globals was here
    equation = ""
    #print(equation)
    cvar = 0
    #print(cvar)
    resolution = 1
    #print(resolution)
    upperlimit = float(input("Upper Limit"))
    #print(upperlimit)
    # dev(upperlimit)
    equation = input("Equation")
    #print(equation)
    # dev(equation)
    varnum = int(input("Number of Variables (1 or 2)"))
    #print(varnum)
    # dev(varnum)
    answerx = ["x"]
    #print(answerx)
    answery = ["Y"]
    #print(answery)
    # label .var2return
    startnumber = float(input("Starting Number"))
    # dev(startnumber)
    reslowbound = 0
    resupperbound = 10
    initialres = 0.1
    rescount = 0
    #initialres = float(input("Initial Resolution"))
    # dev(initialres)
    finalres = 0.1
    #finalres = float(input("Final Resolution"))
    # dev(finalres)
    jumper = startnumber
    y = startnumber
    resolution = 0.1
    #resolution = initialres
    if float(math.log10(initialres)) > 0:
        resupperbound = float(math.log10(initialres))
    rescountmax = float((-1 * math.log10(finalres)) + math.log10(initialres))
    vlist = []
    #print(rescount)

    while "x" in equation:
        print(equation)
        equation = (
        "".join([str(equation[:(equation.index("x"))]), "jumper", (equation[(len("x") + equation.index("x")):])]))
        # (len(equation)-int(equation.index("x")))
        print(equation)
    # print("".join([equation[:eqf(equation)], " > ", equation[eqf(equation):]]))
    equation = "".join([equation[:equation.index("=")], " > ", equation[equation.index("=") + 1:]])
    #print(equation)
    y = startnumber
    if eval(equation) == True:
        Check1 = 1
        Check2 = 1
    else:
        Check1 = 0
        Check2 = 0
    #print(Check1)
    #print(Check2)
    #print(equation)
    #print(jumper)
    #print(varnum)
    #print(y)
    # ==============================================================================
    # ==============================================================================
    ##    return(equation)
    ##    return(resolution)
    ##    return(upperlimit)
    ##    return(varnum)
    ##    return(answerx)
    ##    return(answery)
    ##    return(startnumber)
    ##    return(reslowbound)
    ##    return(resupperbound)
    ##    return(rescount)
    ##    return(initialres)
    ##    return(finalres)
    ##    return(jumper)
    ##    return(rescountmax)
    ##    return(vlist)
    ##    return(cvar)
    #print("startup")
    #print(jumper)
    #print(varnum)
    #print(y)


# ==============================================================================
# ==============================================================================

def reschange(jumper, resolution, rescount, rescountmax):
    if (rescount < rescountmax):
        jumper = float(jumper - resolution)
        # jumper = round(jumper,rescount)
        resolution = resolution / 10
        rescount = rescount + 1
        #print(rescount)
        resreturn(jumper, upperlimit, varnum, y, resolution, vlist, equation, Check1, Check2, rescount, rescountmax,reschange, startnumber, initialres, reslowbound, answerx, answery, finalres, question, supportvar,cvar)
        # return rescount
        # return rescountmax
        # return resolution
        # return jumper
        # print("reschange")


def resreturn(jumper,upperlimit,varnum,y,resolution,vlist,equation,Check1,Check2,rescount,rescountmax,reschange,startnumber,initialres,reslowbound,answerx,answery,finalres,question,supportvar,cvar):
    equationsolvermain(jumper,upperlimit,varnum,y,resolution,vlist,equation,Check1,Check2,rescount,rescountmax,reschange,startnumber,initialres,reslowbound,answerx,answery,finalres,question,supportvar,cvar)
def question():
    supportvar = input("Would you like to start the equation solver?")
    if supportvar == "yes":
        #startup(equation,resolution,cvar,upperlimit,varnum,answerx,answery,startnumber,reslowbound,resupperbound,rescount,initialres,finalres,jumper,y,vlist,rescountmax,Check1,Check2)
        start2(jumper, upperlimit, varnum, y, resolution, vlist, equation, Check1, Check2, rescount, rescountmax, reschange, startnumber, initialres, reslowbound, answerx, answery, finalres, question, supportvar, cvar)
        # cvar = 5
    # fix
    #        print("startup")
    else:
        dev(supportvar)
        supportvar = input("Would you like to go to the help section?")
        if supportvar == "yes":
            print("helpsection(supportvar)")
        else:
            dev(supportvar)
            supportvar = input("Exit program?")
            if supportvar == "yes":
                # cvar = 1
                quit()
                # exit()
            else:
                dev(supportvar)
                question()
    #print("question")
#    return cvar,supportvar

def start2(jumper, upperlimit, varnum, y, resolution, vlist, equation, Check1, Check2, rescount, rescountmax, reschange, startnumber, initialres, reslowbound, answerx, answery, finalres, question, supportvar, cvar):
    global start
    answerstr = 0
    supportvar = ""
    start = ""
    equationleft = ""
    equationright = ""
    start = input(
        "Welcome to Jumper! Jumper is an equation solving program capable of solving equations with 1 or 2 variables. Respond start to continue. Respond help to go to the help section.")

    # start = input("")
    dev(start)
    if start == "help":
        print("work in progress")
        #print("helpsection(supportvar)")
    # label .startup
    # startup(equation,resolution,cvar,upperlimit,varnum,answerx,answery,startnumber,reslowbound,resupperbound,rescount,initialres,finalres,jumper,y,vlist,rescountmax,Check1,Check2)
    #
    print(jumper)
    print(y)
    print(varnum)
    print(upperlimit)
    print(equation)
    cvar = 3
    print(cvar)
    equationsolver(jumper, upperlimit, varnum, y, resolution, vlist, equation, Check1, Check2, rescount, rescountmax,reschange, startnumber, initialres, reslowbound, answerx, answery, finalres, question, supportvar,cvar)
    #print("start2")
#    return jumper,upperlimit,varnum,y,resolution,vlist,equation,Check1,Check2,rescount,rescountmax,reschange,startnumber,initialres,reslowbound,answerx,answery,finalres,question,supportvar,cvar



def dev(supportvar):
    # cvar = "cvar"
    if "/" in supportvar:
        print(eval(supportvar[1:]))


# eqf= 'eval(equation.index("=")))'
def eqf(equation):
    if "=" in equation == True:
        return (equation.index("="))


# +1?
# jdc = 'float(equation.index("/jumper"))'
def jdc(equation, jumper):
    if "/jumper" in equation == True:
        return equation.index("/jumper") + 1


# +1?
# jps = 'float(equation.index("jumper"))'
def jps(equation, jumper):
    if "jumper" in equation == True:
        return equation.index("jumper") + 1


def equationsolver(jumper,upperlimit,varnum,y,resolution,vlist,equation,Check1,Check2,rescount,rescountmax,reschange,startnumber,initialres,reslowbound,answerx,answery,finalres,question,supportvar,cvar):
    # ===============================================================================
    equation = ""
    cvar = 0
    resolution = 1
    upperlimit = float(input("Upper Limit"))
    equation = input("Equation")
    varnum = int(input("Number of Variables (1 or 2)"))
    answerx = ["x"]
    answery = ["Y"]
    startnumber = float(input("Starting Number"))
    reslowbound = 0
    resupperbound = 10
    rescount = 0
    # initialres = float(input("Initial Resolution"))
    # finalres = float(input("Final Resolution"))
    initialres = 0.1
    finalres = 0.1
    jumper = (startnumber)
    y = startnumber
    resolution = initialres
    # ======================================================
    if (math.log10(initialres)) >= 0:
        resupperbound = abs(math.log10(initialres))
    rescountmax = float(abs(math.log10(finalres)) + abs(math.log10(initialres)))
    # rescountmax = 1
    # ======================================================

    vlist = []
    while "x" in equation:
        #print(equation)
        equation = (
            "".join([str(equation[:(equation.index("x"))]), "jumper", (equation[(len("x") + equation.index("x")):])]))
        # (len(equation)-int(equation.index("x")))
        #print(equation)
    equation = "".join([equation[:equation.index("=")], " > ", equation[equation.index("=") + 1:]])
    #print(equation)
    y = startnumber
    if eval(equation) == True:
        Check1 = 1
        Check2 = 1
    else:
        Check1 = 0
        Check2 = 0
    # ===============================================================================
    #print("equation solver start")
    # startup()
    #print(jumper)
    #print(varnum)
    #print(y)
    while (((jumper <= upperlimit) and (varnum == 1)) and not ((y <= upperlimit) and (varnum == 2))) == True and (jumper < 2 * upperlimit) == True:
        #equationsolvermain(jumper,upperlimit,varnum,y,resolution,vlist,equation,Check1,Check2,rescount,rescountmax,reschange,startnumber,initialres,reslowbound,answerx,answery,finalres,question,supportvar,cvar)
        # label .resreturn
        #print("while entered")
        jumper = round(jumper, 1)
        jumper += 0.1
        #print(jumper)
        #print(resolution)
        # vlist = vlist + [jumper]
        # print(vlist)
        if eval(equation) == True:
            Check1 = 1
            # jumper = jumper - resolution + resolution
        else:
            Check1 = 0
        # if (Check1 == Check2) == False:
        #            if (Check1 == 1) == True:
        #                print("jumper = (jumper - resolution)")
        #            if (rescount < rescountmax):
        # ============================================================================


        # if rescount < rescountmax:
        ##                jumper = float(jumper - resolution)
        ##                resolution = resolution / 10
        ##                rescount = rescount + 1
        ##                print(rescount)


        # print("reschange")

        # ============================================================================

        if (Check1 != Check2):
            ##            if (Check1 == 1):
            ##                jumper = float(jumper + (2.5*resolution))
            ##            else:
            ##                jumper = float(jumper - (2.5*resolution))
            #if (rescount < rescountmax):
            #    print("reschange")
            # #reschange(jumper, resolution, rescount, rescountmax)
            if varnum == 1:
                # if Check1 == 1:
                #                   jumper = jumper - resolution
                #jumper -= resolution / 10
                #jumper -= 1 * resolution
                #jumper = round(jumper, 1)
                if eval(equation) == False:
                    jumper += resolution
                    jumper = round(jumper, 1)
                # abs(math.log10(int(resolution)))
                #if Check1 == 0:
                    #jumper -= resolution
                    #jumper = round(jumper, 1)
                #print(Check1)
                #print(Check2)
                #print(vlist)
                jumper -= resolution
                print("".join(["The variable is equal to ", str(jumper), "."]))
            if (varnum == 2) and (y <= upperlimit):
                if ((reslowbound % 2) == 0 or (reslowbound == 1)) and ((jumper % 2) == 0 or (jumper == 1)):
                    answerx = answerx + [jumper]
                    answery = answery + [y]
                    print(answerx)
                    print(answery)
                reslowbound = reslowbound + 1
                jumper = float(jumper + finalres)
                # goto .var2return
            question()
            if rescount > rescountmax:
                print("Out of range")
        if (jumper >= upperlimit) and (y < upperlimit) and (varnum == 2):
            jumper = startnumber
            y = finalres + y
            # goto .return2
            if reslowbound != 0:
                reslowbound = 0
                supportvar = "sv"
                # goto .sv
                # cvar = 4
                question()
                # print("solver")
                # return jumper, upperlimit, varnum, y, resolution, vlist, equation, Check1, Check2, rescount, rescountmax, reschange, startnumber, initialres, reslowbound, answerx, answery, finalres, question, supportvar, cvar


def equationsolvermain(jumper,upperlimit,varnum,y,resolution,vlist,equation,Check1,Check2,rescount,rescountmax,reschange,startnumber,initialres,reslowbound,answerx,answery,finalres,question,supportvar,cvar):
        # label .resreturn
        #print("while entered")
        jumper = (jumper + resolution)
        print(jumper)
        # jumper = round(jumper,int(math.log10(resolution))+1)
        #vlist = vlist + [jumper]
        # print(vlist)
        if eval(equation) == True:
            Check1 = 1
            # jumper = jumper - resolution + resolution
        else:
            Check1 = 0
        # if (Check1 == Check2) == False:
        #            if (Check1 == 1) == True:
        #                print("jumper = (jumper - resolution)")
        #            if (rescount < rescountmax):
        # ============================================================================


        # if rescount < rescountmax:
        ##                jumper = float(jumper - resolution)
        ##                resolution = resolution / 10
        ##                rescount = rescount + 1
        ##                print(rescount)


        # print("reschange")

        # ============================================================================

        if (Check1 != Check2):
            ##            if (Check1 == 1):
            ##                jumper = float(jumper + (2.5*resolution))
            ##            else:
            ##                jumper = float(jumper - (2.5*resolution))
            #if (rescount < rescountmax):
                #print("reschange")
            #  #reschange(jumper, resolution, rescount, rescountmax)
            if varnum == 1:
                # if Check1 == 1:
                #                   jumper = jumper - resolution
                jumper = jumper - resolution / 10
                jumper = jumper - (1 * resolution)
                jumper = round(jumper, 1)
                if eval(equation) == False:
                    jumper = jumper + resolution
                    jumper = round(jumper, 1)
                # abs(math.log10(int(resolution)))
                if Check1 == 0:
                    jumper = jumper + resolution
                    jumper = round(jumper, 1)
                #print(Check1)
                #print(Check2)
                #print(vlist)
                print("".join(["The variable is equal to ", str(jumper), "."]))
            if (varnum == 2) and (y <= upperlimit):
                if ((reslowbound % 2) == 0 or (reslowbound == 1)) and ((jumper % 2) == 0 or (jumper == 1)):
                    answerx = answerx + [jumper]
                    answery = answery + [y]
                    print(answerx)
                    print(answery)
                reslowbound = reslowbound + 1
                jumper = float(jumper + finalres)
                # goto .var2return
            question()
            if rescount > rescountmax:
                print("Out of range")
        if (jumper >= upperlimit) and (y < upperlimit) and (varnum == 2):
            jumper = startnumber
            y = finalres + y
            # goto .return2
            if reslowbound != 0:
                reslowbound = 0
                supportvar = "sv"
                # goto .sv
                # cvar = 4
                question()
    #print("solver")
    #return jumper, upperlimit, varnum, y, resolution, vlist, equation, Check1, Check2, rescount, rescountmax, reschange, startnumber, initialres, reslowbound, answerx, answery, finalres, question, supportvar, cvar

if __name__ == '__main__':

    start2(jumper, upperlimit, varnum, y, resolution, vlist, equation, Check1, Check2, rescount, rescountmax, reschange, startnumber, initialres, reslowbound, answerx, answery, finalres, question, supportvar, cvar)
#print("end")
