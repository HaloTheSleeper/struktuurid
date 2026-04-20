def fiboRecursion(number):
    if number <= 1:
        return number
    
    return fiboRecursion(number - 1) + fiboRecursion(number - 2)

def fiboDynamic(number):
    if number <= 1:
        return number
    
    db = [0, 1]
    
    for i in range (2, number + 1):
        db.append(db[i - 1] + db[i - 2])
        
    return db[i]

print(fiboDynamic(9))
    