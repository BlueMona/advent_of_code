from functools import cache

def copyfile(f):
    with open (f) as file: 
        fcopy = open("./newfile.txt", "w")
        for line in file: 
            fcopy.write(line)
        return fcopy
    
def makeFileArray(f): 
    with open (f) as file:
        bigArray = [] 
        for line in file: 
            bigArray.append(line)
        return bigArray

def copyArray(array):
    newArray = [] 
    for item in array: 
        newArray.append(item)
    return newArray

def copyArrayBackwards(array):
    return array[::-1] 
    
def processCard(line):
    string = line.rstrip()
    # index from the end because of additional spacing in large file
    card = int(string.split(":")[0].rstrip().split(" ")[-1])
    print(card)
    numbers = string.split(":")[1]
    winning_numbers = numbers.split("|")[0].rstrip().split(" ")
    your_numbers = numbers.split("|")[1].rstrip().split(" ")

    while('') in winning_numbers: 
        winning_numbers.remove('')

    while('') in your_numbers: 
        your_numbers.remove('')
    
    winning = 0
    for number in your_numbers: 
        if number in winning_numbers:
            winning += 1

    return (card, winning)


# globally accessible to simplify function headers. 
FILE_ARRAY = makeFileArray("input.txt")

# this is a correct solution and works on the example. 
# However, with the full problem, it reaches 
# `RecursionError: maximum recursion depth exceeded while calling a Python object`
def recursiveCardCounting(cardArray, cardCount):
    for line in cardArray:
        cardCount += 1 
        
        (card, winning) = processCard(line)
        print("for card " + str(card) + " the winning number is " + str(winning))

        # the card wins the next few cards
        for i in range(card, card + winning):
            print(i)
            cardArray.append(FILE_ARRAY[i])
        
        #we are done processing the current card
        cardArray.remove(line)

        if cardArray != []:
            return recursiveCardCounting(cardArray, cardCount)
        
        return cardCount

def cardCounting(reversedArray):
    cardTotalValues = {} 
    cardCount = 0 

    for line in reversedArray:
         
        (card, winning) = processCard(line)
        print("for card " + str(card) + " the winning number is " + str(winning))

        cardTotalValues[card] = 1

        for i in range(card, card + winning):
            cardTotalValues[card] += cardTotalValues[i + 1] 
        print("total value for card " + str(card) + " " + str(cardTotalValues[card]))
        cardCount += cardTotalValues[card]

    return cardCount

def scan():
    #cardArray = copyArray(FILE_ARRAY)
    #return recursiveCardCounting(cardArray, 0)
    
    cardArray = copyArrayBackwards(FILE_ARRAY)
    return cardCounting(cardArray)