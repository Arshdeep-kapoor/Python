import datetime,time
class time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    
    def getHour(self):
        return self.__hour
    def getMinute(self):
        return self.__minute
    def getSecond(self):
        return self.__second
    
    def setTime(self,elapseTime):
        if elapseTime>=(24*3600):
            elapseTime=elapseTime%(24*3600)
        hour = self.__hour+(elapseTime//3600)
        elapseTime=elapseTime%3600
        minute=self.__minute+(elapseTime//60)
        elapseTime=elapseTime%60
        second=self.__second+elapseTime
        if second>=60:
            second-=60
            minute+=1
        if minute>=60:
            minute-=60
            hour+=1
        if hour>=24:
            hour-=24
        print("The hour:minute:second for the elapsed time is",hour,":",minute,":",second)
        
now=datetime.datetime.now().time()
print("Current time is",now.hour,":",now.minute,":",now.second)
elapseTime = eval(input("Enter the elapsed time:"))
time=time(now.hour,now.minute,now.second)

time.setTime(elapseTime)