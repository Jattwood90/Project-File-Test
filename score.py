def score(): 
    if x >= 75:
        return(list.append(str("Top")))
    elif x >= 50:
        return(list.append(str("pass")))
    else:
        return(list.append(str("fail")))number = 0
x = []
list = []

while number < 10:
    x = int(input())
    number = number + 1
    score()
    
print("There are:", list.count("Top"), "top marks", list.count("pass"),"pass marks and", list.count("fail"), "failures out of", number)