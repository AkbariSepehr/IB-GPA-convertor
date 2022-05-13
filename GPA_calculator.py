import time

print('''
██╗██████╗░  ████████╗░█████╗░  ░██████╗░██████╗░░█████╗░
██║██╔══██╗  ╚══██╔══╝██╔══██╗  ██╔════╝░██╔══██╗██╔══██╗
██║██████╦╝  ░░░██║░░░██║░░██║  ██║░░██╗░██████╔╝███████║
██║██╔══██╗  ░░░██║░░░██║░░██║  ██║░░╚██╗██╔═══╝░██╔══██║
██║██████╦╝  ░░░██║░░░╚█████╔╝  ╚██████╔╝██║░░░░░██║░░██║
╚═╝╚═════╝░  ░░░╚═╝░░░░╚════╝░  ░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝''')

print("program by Sepehr")

time.sleep(0.5)

def gpa(weight):
    gpa_sum = 0.0
    subjects = ["Language & Literature (G1)", "Language Acquisition (G2)", "Individuals and Societies (G3)",
                "Experimental Sciences (G4)", "Mathematics (G5)", "The Arts (G6)"]

    flag = True
    while flag:
        q = str(input("\nWould you like to add your own subjects? \n respond with [Y/N]")).upper()

        if q == "N":
            pass

        if q == "Y":
                time.sleep(0.5)
                for i in range(0, 6):
                    subjects[i] = str(input("\nWhat subject do you take in " + subjects[i] + "? ")).upper()
                flag = False


    for i in range(0,6):
        ib_grade = int(input("\n what is your score in " + subjects[i]+"? "))
        if ib_grade == 7: gpa_sum += weight
        if ib_grade == 6: gpa_sum += 4.0
        if ib_grade == 5: gpa_sum += 3.0
        if ib_grade == 4: gpa_sum += 2.0
        if ib_grade == 3: gpa_sum += 1.0

    return gpa_sum/6


flag = True
weight = 0

while flag:
    x = str(input("\n Do you want to get a weighted GPA? "
                    +"\n respond with [Y/N]")).upper()
    if x == "Y":
        weight += 4.3
        x = "WEIGHTED"
        flag = False

    if x == "N":
        weight += 4.0
        x = "UNWEIGHTED"
        flag = False

print("\nyour GPAis "+ str(gpa(weight)))
