age = 18

if age>=18:
    print("You can vote")
else:
    print("You can not vote")


temperatura=28

if temperatura>30:
    print("Its a hot day, stay hydrated.")
elif temperatura>=20 or temperatura <=30:
    print("The weather is pleasent.")
else:
    print("Its a cold day.")

student_gpa = 4.5
student_score=75

if student_gpa >= 3.5:
     if student_score>=50 | student_score<=65:
        print("Student with these score are eligible for a partial scholarship")
     elif student_score>65:
         print("Student with these score are eligible for a full scholarship")
     else:
         print("Student with these score are not eligible for a scholarship")
else:
    print("Student gpa and test score are not eligible for a scholarship")