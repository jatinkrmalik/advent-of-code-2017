import sys
import math

def get_square(ip):
    '''
    To calculate the size of square required
    '''
    square = 1
    
    while square * square < ip:
        square = square + 2
    
    return square

def distance_to_one(num, base, offset, side):
    '''
    To find the number of step after each step recursively
    '''
    
    first = base + 1
    
    if num < first + side:
        return int(math.fabs(num - first - offset))
    
    elif num < first + side * 2:
        return int(math.fabs(num - first - offset - side))
    
    elif num < first + side * 3:
        return int(math.fabs(num - first - offset - side * 2))
    
    else:
        return int(math.fabs(num - first - offset - side * 3))

def main():
    ip = int(input()) # getting input from STDIN
    square = get_square(ip)
    side_len = square - 1
    path_to_one = math.floor(square/2)
    side_offset_to_middle = path_to_one - 1
    prev_square = square - 2
    print(path_to_one + distance_to_one(ip, prev_square * prev_square, side_offset_to_middle, side_len))

if __name__ == "__main__":
    main()

