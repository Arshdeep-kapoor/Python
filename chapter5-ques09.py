tution = 10000
rate = 5
total = 0
tution1 = 0
for i in range(1,11):
    tution1 = tution * .05
    tution = tution + tution1
print(tution,"tution after 10 years")
for i in range(1,3):
    total += tution
    tution1 = tution * .05
    tution = tution + tution1
total+=tution
print(total,"amount for 4 years after 10 years")