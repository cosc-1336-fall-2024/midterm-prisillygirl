#write functions here, don't add input('') statements here!

def test_config():
    return True

def get_sum_of_evens(num):
    total_sum = 0

    for i in range(2, num + 1, 2):
        total_sum += i 

    return total_sum