#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_fahrenheit(celsius):
    return (9/5) * celsius + 32


def display_temperature_table():

    for celsius in range(21):
        fahrenheit = get_fahrenheit(celsius)
        
