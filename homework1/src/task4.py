## Duck typing is the functionality of a language where "if it looks like a duck and quacks like a duck,
## you might as well treat it like a duck." This is quite common in interpreted languages. Create a
## new file named task4.py that calculates the final price of a product after applying a given discount
## percentage inside of a function named calculate_discount. The function should accept any numeric
## type for price and discount. Write pytest test cases to test the calculate_discount function with
## various types (integers, floats) for price and discount.

def calculate_discount(price, discount):
    if (discount < 0 or discount > 100):
        raise ValueError("Discount must be between 0 and 100.")
    final_price = price - (price * (discount / 100))
    return final_price

def main():
    ##print(f"Formatted to two decimal places: {number:.2f}")
    print("Final price (int inputs):", calculate_discount(100, 20))
    print("Final price (float inputs):", calculate_discount(150.5, 15.75))

if __name__ == '__main__':
    main()