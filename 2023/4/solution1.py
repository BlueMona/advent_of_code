def scan(f):
    with open (f) as file:
        total_points = 0
        for line in file: 
            string = line.rstrip()
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
            if winning == 0: 
                points = 0
            else: 
                points = 2**(winning - 1)
            total_points += points
        return total_points

                


            

