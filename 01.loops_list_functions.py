#default values of arguments for user defined functions

def percent_calculator(mark_obt=0, total=100):
    per = (float(mark_obt) /total) * 100
    return per

students = ['Aman', 'Abhinav', "Ravi", "Vikas", "Mehul", "Deep"]
marks = [298, 267, 264, 237, 278, 194]
i=0

for s in students:

    if marks[i]<90:
        status="fail"
    else:
        status="pass"

    print s, " ", percent_calculator(mark_obt=marks[i],total=300), " ", status
    i=i+1



