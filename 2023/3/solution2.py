
digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def find_dimensions(f):
    sum = 0
    with open (f) as file: 
        y = 0
        for line in file:
            x = 0
            for char in line: 
                x+=1 
            y += 1
    print(x) 
    print(y)
    return (x, y)

# returns the numbers in a string
def seek_numbers(string): 
    left = 0 
    right = 1

    numbers = []
    symbols = []
    is_number = False

    while(left < len(string) and right <= len(string)):
        cur = string[left:right]
        next = string[right:right+1]
        # determine whether we are looking at a number
        for item in digits: 
            if item in cur: 
                is_number = True
                break
        
        # if we are looking at a symbol
        if not(is_number):
            if cur != "." and cur != '\n' and cur not in digits: 
                symbols.append({"symbol": cur, "left": left, "right": right})

        if (next in digits):
            # we were not already looking at a number
            if not(is_number):
                left +=1 # move the cursor
            # we were already looking at a number
            right +=1 # increase the window size to include "next"

        # if this is a number and we are at its end 
        else: 
            if(is_number): 
                numbers.append({"number": cur, "left": left, "right": right})
            # reset
                left = right
                right = left + 1 
                is_number = False
            else: 
                left +=1 
                right +=1
    return (numbers, symbols)      

def scan(f):
    with open (f) as file:

        numbers = []
        symbols = []
        for line in file:
            (line_numbers, line_symbols) = seek_numbers(line)
            numbers.append(line_numbers)
            symbols.append(line_symbols)

        i = 0
        sum = 0
        gearcount = 0
        actual_gears = 0

        for line in symbols:
            #adjacent = false          
            for symbol in line: 
                if symbol["symbol"] == '*':
                    gearcount += 1
                    factors = []  
                    for number in numbers[i]:
                        if(symbol["left"] == number["right"] or symbol["right"] == number["left"]):
                            #adjacent = True
                            factors.append(number["number"])
                    if(i > 0 and len(numbers[i-1])> 0):
                        for number in numbers[i-1]:
                            if(symbol["left"] >= number["left"] -1 and symbol["right"] <= number["right"] + 1):
                                #adjacent = True
                                factors.append(number["number"])
                    if(i < len(symbols) - 1 and len(numbers[i+1])> 0):
                        for number in numbers[i+1]:
                            if(symbol["left"] >= number["left"] - 1 and symbol["right"] <= number["right"] + 1):
                                #adjacent = True
                                factors.append(number["number"])
                    if len(factors) == 2:
                        actual_gears += 1
                        product = int(factors[0])*int(factors[1])
                        sum += product             
            i = i + 1
        return sum  