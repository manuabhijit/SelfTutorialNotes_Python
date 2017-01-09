import module_used_1
import random

students = ['Aman', 'Abhinav', "Ravi", "Vikas", "Mehul", "Deep"]
marks = [298,267,264,237,278,194]
i=0

for s in students:
    if marks[i]<90:
        status="fail"
    else:
        status="pass"

    print s," ",module_used_1.percent_calculator(mark_obt=marks[i],total=300)," ",status
    i=i+1

print "a random number = " + str(random.randrange(2,10))