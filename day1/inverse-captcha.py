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


def inverse_captcha_halfway(num):
    numList = [int(x) for x in str(num)] # to easily iterate over digits by splitting into a list
    inv_captcha = 0
    ln = len(numList)
    half_len = ln//2
    for i in range(ln):
        num_half_ahead = i + half_len
        if num_half_ahead >= ln: 
            num_half_ahead = num_half_ahead % ln # to normalise the rotation ahead the length of the list
        
        if numList[i] == numList[num_half_ahead]:
            inv_captcha += numList[i]
        
        else:
            pass

    return inv_captcha    

def main():
    num = int(input())
    
    result1 = inverse_captcha(num)
    result2 = inverse_captcha_halfway(num)
    print('Answer of part 1 is', result1, '\nAnswer of part 2 is', result2)

if __name__ == "__main__": # execute only if run as a script
    main()
