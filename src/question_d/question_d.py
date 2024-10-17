#write functions here, don't add input('') statements here!

def get_bonus_pay_amount(sales):

    if sales < 0 or sales > 1999:
        return 'Invalid arguments'
 
    if 0 <= sales < 500:
        percentage = 0.05
    elif 500 <= sales < 1000:
        percentage = 0.06
    elif 1000 <= sales < 1500:
        percentage = 0.07
    elif 1500 <= sales < 2000:
        percentage = 0.08
    
    bonus = sales * percentage

    return bonus

