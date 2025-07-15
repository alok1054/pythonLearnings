# Student Grading
''' Program to take input of 5 subjects,
calculate the percentage and
decide the grades of the student'''

marks1 = float(input("Enter the marks of the Subject 1: "))
marks2 = float(input("Enter the marks of the Subject 2: "))
marks3 = float(input("Enter the marks of the Subject 3: "))
marks4 = float(input("Enter the marks of the Subject 4: "))
marks5 = float(input("Enter the marks of the Subject 5: "))

percentScored = ((marks1+marks2+marks3+marks4+marks5)/5)

# How i did it
# if percentScored>=75:
#    print(f"Student has obtained {percentScored} % and graded A")
# elif percentScored>=50 and percentScored<75:
#    print(f"Student has obtained {percentScored} % and graded B")
# elif percentScored>=30 and percentScored<50:
#    print(f"Student has obtained {percentScored} % and graded C")
# else:
#    print(f"What a useless guy Fail")

# Simpler way
if percentScored>=75:
    print(f"Student has obtained {percentScored} % and graded A")
elif percentScored>=50:
    print(f"Student has obtained {percentScored} % and graded B")
elif percentScored>=30:
    print(f"Student has obtained {percentScored} % and graded C")
else:
    print(f"What a useless guy Fail")

