


# the basic check if there is no letters in the input and if the input contian 9 digits
def basic_validation(tz):
    index=0
    digits=[]
    for i in tz:
        if i.isalpha():
            return False
        i = int(i)
        index += 1
        digits.append(i)
    if index != 9:
        return False
    return digits


# the algorithm check 
def check_rule(list):    
    total=[]
    check_digit= list[8]
    key= [1,2,1,2,1,2,1,2]
    for number in range(8):
        res = list[number] * key[number]
        if res > 9:
            res = res / 2
            total.append(res)
        total.append(res)
    check_the_total = sum(total) + check_digit
    if check_the_total % 10 == 0:
        return True
    else:
        return False




while True:
    try:
        user_input= input("Enter ID to check, for quit press [q]: ")
        if user_input == 'q':
            break
        tz = basic_validation(user_input)
        if tz == False:
            print('ID is not valid!')
        chek = check_rule(tz)
        if chek == True:
            print('ID is valid!')
        else:
            print('ID is not valid!')
    except Exception as e:
        continue
        

            

        
        




