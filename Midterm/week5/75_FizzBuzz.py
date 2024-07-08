"""Week 5"""
def fizzbuzz(num):
    """FizzBuzz"""
    for number in range(1, num+1):
        if number%3 == 0 and number%5 == 0:
            print("FizzBuzz")
        elif number%3 == 0:
            print("Fizz")
        elif number%5 == 0:
            print("Buzz")
        else:
            print(number)
fizzbuzz(int(input()))
