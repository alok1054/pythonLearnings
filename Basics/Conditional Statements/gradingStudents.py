''' Write a program to design a student grading system wth marks validity check
- the marks can only be entered in between 0 to 100, then only the grade will be checked
- otherwise negative marks or marks greater than 100 are invalid'''

marks1 = float(input("Enter the marks of the Subject 1: "))
if 0<=marks1<=100 :
    marks2 = float(input("Enter the marks of the Subject 2: "))
    if 0<=marks2<=100:
        marks3 = float(input("Enter the marks of the Subject 3: "))
        if 0<=marks3<=100:
            marks4 = float(input("Enter the marks of the Subject 4: "))
            if 0<marks4<=100:
                marks5 = float(input("Enter the marks of the Subject 5: "))
                if 0<=marks5<=100:
                    if marks1>=40 and marks2>=40 and marks3>=40 and marks4>=40 and marks5>=40 :
                        percentScored = ((marks1+marks2+marks3+marks4+marks5)/5)
                        if percentScored >= 75:
                            print(f"Student has obtained {percentScored} % and graded A")
                        elif percentScored >= 50:
                            print(f"Student has obtained {percentScored} % and graded B")
                        elif percentScored >= 40:
                            print(f"Student has obtained {percentScored} % and graded C")
                    else:
                         print("Fail, No Grades")
                else :
                    print("Error : Please enter the marks 5 of the students between 0 to 100, negative or marks greater than 100 not allowed")
            else:
                print("Error : Please enter the marks 4 of the students between 0 to 100, negative or marks greater than 100 not allowed")
        else :
            print("Error : Please enter the marks 3 of the students between 0 to 100, negative or marks greater than 100 not allowed")
    else:
        print("Error : Please enter the marks 2 of the students between 0 to 100, negative or marks greater than 100 not allowed")
else:
    print("Error : Please enter the marks 1 of the students between 0 to 100, negative or marks greater than 100 not allowed")
