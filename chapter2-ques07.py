time = eval(input("number of minutes in billions"))
days = time//(60*24)
years = days//365
days = days%365
print(time,"minutes is approximately",years,"years and ",days, " days")        