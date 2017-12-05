
def sheetMaker(ip):
    '''
    This method returns a 2d array (list of lists) sorted and parsed as integers
    '''
    sheets = []

    for line in ip.readlines():
        sheets.append(line.split())

    new_sheet = []

    for sheet in sheets:
        new_sheet.append(sorted(list(map(int, sheet))))
    
    return new_sheet

def corChecksum(new_sheet):
    '''
    This method returns the checksum where, the difference between the largest value and the smallest value;
    the checksum is the sum of all of these differences.
    '''
    checksum = 0
    
    # Finding difference between smallest and largest number in each row, and adding it to the checksum.
    for row in new_sheet:
        checksum += row[-1] - row[0]

    return checksum

def corChecksumNew(new_sheet):
    '''
    This method retuns the checksum where, the only two numbers in each row where one evenly divides the other;
    the checksum is the sum of the result of division of two numbers above.
    '''
    checksum = 0

    # Implementing bruteforce search for evenly divisible pair, and adding the quotient to the checksum.
    for row in new_sheet:
        for i, num1 in enumerate(row):
            for j, num2 in enumerate(row[i+1:]):
                if num2 % num1 == 0:
                    checksum += num2//num1
                    break
                else:
                    pass
    
    return checksum


def main():
    ip = open('input.txt', 'r+')
    new_sheet = sheetMaker(ip)
    answer1 = corChecksum(new_sheet)
    answer2 = corChecksumNew(new_sheet)
    print("Answer for the part 1 is", answer1, "\nAnswer for the part 2 is", answer2)

if __name__ == "__main__":
    main()
