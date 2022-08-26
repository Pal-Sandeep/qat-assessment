import re
from telnetlib import SE

class Student:
    def __init__(self,id,name,marks,finalmarks,grade,typ):
        self.name = name
        self.id = id
        self.marks=marks
        self.grade=grade
        self.typ = typ
        self.finalmarks = finalmarks

def mainmenu():
    print('Choose one of the following options:')
    print('1 - Enter student grade information')
    print('2 - Print all student grade information')
    print('3 - Print class performance statistics')
    print('4 - Exit')
    userinp = float(input(''))
    try:
        if userinp not in [1,2,3,4]:
            raise ValueError()
        if userinp == 1:
            menu1()
        elif userinp == 2:
            menu2()
        elif userinp == 3:
            menu3()    
        else:
            exit()
    except ValueError:
        print('Invalid Input❌❌❌')
        print('Please enter a valid input.')
        mainmenu()
def menu1():
    global gradepoint,finalmarks,i,BIT,DIT,grade
    print('Choose one of the following options:')
    print('1.1 - Enter a BIT student information')
    print('1.2 - Enter a DIT student information')
    print('1.3 - Go back to the main menu')
    userinp = float(input())
    try: 
        if userinp not in [1.1,1.2,1.3]:
            raise ValueError()
        
        if userinp == 1.1:
            global F,P,D,HD,C,SA,SE
            id = input('Student ID (A capital letter ‘A’ followed by 8 digits): ')
            regex = r'^[A][0-9]{8}$'
            try:
                if not re.search(regex,id):
                    raise ValueError()
                course.append(input('Student’s name: ').upper())
                marks=input('Student’s assessment marks (separated by comma): ')
                marks = [round(float(mark),2)  for mark in marks.split(',')]
                finalmarks = finalscore(marks)
                BITgrade(marks)                            
                
                typ = "BIT"
                name = course[i]
                course[i]=Student(id,name,marks,finalmarks,grade,typ)
                i=i+1
                BIT += 1
                mainmenu()
            except ValueError :
                print("Entered Student ID is invalid.")
                print("Please enter a valid input.")
                menu1()

        elif userinp == 1.2:
            global CP
            id = input('Student ID (A capital letter ‘A’ followed by 8 digits): ')
            regex = r'^[A][0-9]{8}$'
            try: 
                if not re.search(regex,id):
                    raise ValueError()
                course.append(input('Student’s name: ').upper())
                marks=input('Student’s assessment marks (separated by comma): ')
                marks = [ round(float(mark),2)  for mark in marks.split(',')]
                finalmarks = finalscore(marks)
                typ = "DIT"
                grade = ditgrade(finalmarks)
                if finalmarks > 49 :                
                    CP += 1
                    gradepoint = gradepoint + 4.0
                else:
                    F += 1
                name=course[i]
                if int(finalmarks) < 50:
                    marks = input('What is this student’s resubmission marks (separated by comma): ')
                    marks = [round(float(mark),2)  for mark in marks.split(',')]
                    finalmarks = finalscore(marks)
                    grade = ditgrade(finalmarks)
                    gradepoint += 4 if finalmarks > 50 else 0
                    course[i]=Student(id,name,marks,finalmarks,grade,typ)
                else :
                    course[i]=Student(id,name,marks,finalmarks,grade,typ)
                i=i+1
                DIT += 1
                mainmenu()
            except ValueError :
                print("Entered Student ID is invalid.❌❌❌")
                print("Please enter a valid input.")
                menu1()
        elif userinp == 1.3:
            mainmenu()
    except ValueError:
        print('Invalid Input❌❌❌')
        print('Please enter a valid input.')
        menu1()
def menu2():
    print('Choose one of the following options:')
    print('2.1 - Print all student grade information ascendingly by final mark')
    print('2.2 - Print all student grade information descendingly by final mark')
    print('2.3 - Go back to the main menu')
    userinp = float(input())
    
    try:
        if userinp not in [2.1,2.2,2.3]:
            raise ValueError()
        if userinp ==2.1:
            print('| STUDENT ID | STUDENT NAME | TYPE | FINAL MARKS | GRADE |')
            
            for student in course:
                print(f'| {student.id} | {student.name} | {student.typ} | {student.finalmarks} | {student.grade} |')
            mainmenu()
        elif userinp ==2.2:
            print('| STUDENT ID | STUDENT NAME | TYPE | FINAL MARKS | GRADE |')
            
            for student in course:
                print(f'| {student.id} | {student.name} | {student.typ} | {student.finalmarks} | {student.grade} |')
            mainmenu()
        elif userinp ==2.3:
            mainmenu()
    except ValueError:
        print('Invalid Input❌❌❌')
        print('Please enter a valid input.')
        menu2()
def menu3():
    global sum1,sum2,sum3,sumfinal
    totalstudents = BIT + DIT
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sumfinal = 0
    for students in course:
        sum1 = sum1+ students.marks[0]
        sum2 = sum2 + students.marks[1]
        sum3 = sum3+ students.marks[2]
        sumfinal = sumfinal + students.finalmarks
    try:
        avg1 = round(sum1/totalstudents,2)
        avg2 = round(sum2/totalstudents,2)
        avg3 = round(sum3/totalstudents,2)
        avgtotal = round((sumfinal/totalstudents),2)
        avgGrade = round(gradepoint/totalstudents)
        passrate = round((totalstudents-F)/totalstudents*100,2)
        passratead = round((totalstudents-F-SP)/totalstudents*100,2)
    
        print('Class performance statistics: ')
        print('Number of Total students: ',totalstudents)
        print(f'Number of BIT students: {BIT}')
        print(f'Number of DIT students: {DIT}')
        print('Student pass rate:',passrate)
        print('Student pass rate (adjusted): ',passratead)
        print('Average mark for Assessment 1: ',avg1)
        print('Average mark for Assessment 2:',avg2)
        print('Average mark for Assessment 3:',avg3)
        print('Average final mark:',avgtotal)
        print('Average grade point: ',avgGrade)
        print('Number of HDs: ',HD)
        print('Number of Ds: ',D)
        print('Number of Cs: ',C)
        print('Number of Ps: ',P)
        print('Number of SPs:',SP)
        print('Number of CPs:',CP)
        print('Number of Fs: ',F)
        mainmenu()
    except Exception as e:
        print("Please first Enter the data.😅😅")
        mainmenu()
def finalscore(marks):
    return round((marks[0]*.2)+(marks[1]*.4)+(marks[2]*.4),2)

def BITgrade(marks):
    global F,SA,SP,SE,HD,D,C,P,grade,gradepoint,finalmarks
    if finalmarks < 45:
        if (marks[0] == 0 and marks[1] == 0 ) or (marks[1] == 0 and marks[2] == 0 ) or (marks[2] == 0 and marks[0] == 0 ):
            grade = 'AF'
            F += 1
        else :                        
            grade = 'F'
            F += 1
    if finalmarks < 50 and finalmarks > 44:
        if 0  in marks:
            grade = 'F'                        
            F += 1
        elif marks[0] < 50.0 and not marks[1] < 50.0 and not marks[2] < 50.0:
            grade = 'SA'
            SA += 1
            marks[0] = float(input('What is this student’s resubmission marks of Lab Exercise: '))
            finalmarks = finalscore(marks)
            grade = 'SP' if finalmarks > 49 else 'F'
            gradepoint += 0.5 if finalmarks > 49 else 0
            if finalmarks < 50 and finalmarks >= 0:
                grade = 'F'
                F += 1
            elif finalmarks > 50 and finalmarks <= 100:
                gradepoint += 0.5
                grade = 'SP'
                SP += 1
            
        elif marks[1] < 50.0 and not marks[0] < 50.0 and not marks[2] < 50.0:
            grade = 'SA'
            SA += 1
            marks[1] = float(input('What is this student’s resubmission marks of Report: '))
            finalmarks = finalscore(marks)
            
            if finalmarks < 50 and finalmarks >= 0:
                grade = 'F'
                F += 1
                return finalmarks
            elif finalmarks > 50 and finalmarks <= 100:
                gradepoint += 0.5
                grade = 'SP'
                SP += 1
                return finalmarks
            else :
                print('Invalid Input! Please enter a valid input.')
                menu1()
        else:
            grade = 'SE'
            finalmarks = round(float(input('What is this student’s supplementary exam mark: ')),2)
            if finalmarks < 50 and finalmarks >= 0:
                grade = 'F'
                F += 1
            elif finalmarks > 50 and finalmarks <= 100:
                grade = 'SP'
                SP += 1
            else :
                print('Invalid Input! Please enter a valid input.')
                menu1()

    elif finalmarks <65:
        grade= 'P'                    
        P += 1
        gradepoint = gradepoint + 1.0
    elif finalmarks <75:
        grade= 'C'                    
        C += 1
        gradepoint = gradepoint + 2.0
    elif finalmarks <85:
        grade= 'D'                    
        D +=1
        gradepoint = gradepoint + 3.0
    else :
        grade = 'HD'
        HD += 1
        gradepoint = gradepoint + 4.0

def ditgrade(finalmarks):
    return 'CP' if finalmarks > 49 else 'NC'

if __name__ == '__main__':
    global BIT,DIT,i
    BIT = 0
    DIT = 0
    i = 0
    course = []
    HD = 0
    D = 0
    P = 0
    SP = 0
    CP = 0
    NYC = 0
    F = 0
    C=0
    SA =0 
    NP = 0
    gradepoint = 0
    finalmarks = 0
    mainmenu()