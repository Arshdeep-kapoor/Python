num = eval(input("enter the number of students:"))
score = 0
max = 0
for i in range(num):
    print("please enter the score of", i+1, "student",end="")
    score = eval(input(":"))
    if score == 0 :
        continue
    elif score >max:
        max, sec = score, max
print("second highest number is", sec)
print("highest number is",max)
        