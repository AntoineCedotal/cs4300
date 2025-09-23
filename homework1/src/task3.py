## Create a new file named task3.py. Create an if statement to check if a given number is positive, negative, or zero. 

## Implement a for loop to print the first 10 prime numbers (you may need to research how to calculate prime numbers). 

## Create a while loop to find the sum of all numbers from 1 to 100. Write pytest test cases to verify the correctness 
## of your code for each control structure.

def check_number(num):
    if (num > 0):
        return "Positive!"
    elif (num < 0):
        return "Negative!"
    else:
        return "Zero!"

def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes
                
def sum_to_100():
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total
        
def main():
    number = 1
    test_num_value(number)
    number = -1
    test_num_value(number)
    number = 0
    test_num_value(number)
    
    number = 30
    test_prime_print(number)
    
    test_while_sum()
    
if __name__ == '__main__':
    main()