# To execute use STDIN redirect '>'
# ex: $ python3 inverse-captcha-halfway.py < input.txt > output.txt

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
    
    result = inverse_captcha_halfway(num)
    
    print(result)

if __name__ == "__main__": # execute only if run as a script
    main()
