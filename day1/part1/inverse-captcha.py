# To execute use STDIN redirect '>'
# ex: $ python3 inverse-captcha.py < input.txt > output.txt

def inverse_captcha(num):
    numList = [int(x) for x in str(num)] # to easily iterate over digits by splitting into a list
    inv_captcha = 0
    i = 0
    
    while i < len(numList):
        if i == len(numList) - 1 and numList[i] == numList[0]: # for edge case of list rotation when last digit == first digit
            inv_captcha += numList[i]
        
        elif numList[i] == numList[i+1]:
            inv_captcha += numList[i]
        
        else:
            pass
       
        i += 1
    
    return inv_captcha

def main():
    num = int(input())
    
    result = inverse_captcha(num)
    
    print(result)

if __name__ == "__main__": # execute only if run as a script
    main()
