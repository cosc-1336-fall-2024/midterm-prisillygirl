#add import

from question_b import get_fahrenheit


def main():
 
 return (9/5) * celsius + 32

print(f"{'Celsius':<10} {'Fahrenheit':<10}") 

print("_" * 21)

for celsius in range(21):
        
        fahrenheit = get_fahrenheit(celsius)

        print(f"{celsius:<10} {fahrenheit:<10.2f}")

main()