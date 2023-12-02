numbers = {
    'zero': 0, 
    'one': 1, 
    'two': 2, 
    'three': 3, 
    'four': 4, 
    'five': 5, 
    'six': 6, 
    'seven': 7, 
    'eight': 8, 
    'nine': 9
}

def is_int(char):
    if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return True
    return False

#
def contains_int(string): 
    for char in string: 
        if is_int(char): 
            return (int)(char)
    return None

def is_number(string): 
    if string in numbers.keys():
        return True
    return False

def contains_number(string): 
    for n in numbers.keys(): 
        if n in string: 
            return numbers[n]
    return None

def seek_number(string, reverse=False): 
    if reverse: 
        start = len(string)
        end = 0 
        step = -1
    else: 
        start = 0
        end = len(string)
        step = 1
    for i in range(start, end, step): 
        if reverse:
            cur = string[i - 1:len(string)]
        else: 
            cur = string[0:i + 1]  
        # print(cur)
        firstInt = contains_int(cur)
        if firstInt != None:    
            return firstInt 
        firstNumber = contains_number(cur)
        if firstNumber != None: 
            return firstNumber
    print("Error, no numbers found, input was " + string)

def concatenate(string): 
    first = str(seek_number(string))
    last = str(seek_number(string, True))
    return first + last 

def sum_all(list):
    sum = 0;
    for item in list:
        sum = sum + (int)(concatenate(item))
    return sum

def sum_all(f):
    with open (f) as file: 
        sum = 0;
        for line in file: 
            string = line.rstrip()
            sum = sum + (int(concatenate(string)))
    return sum