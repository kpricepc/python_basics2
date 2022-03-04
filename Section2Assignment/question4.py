def HowManyFibonacci():
    # Take user input with error handeling
    inputComplete = False
    Times = int
    while inputComplete == False:
        try:
            Times = int(input("Please enter the desired number of fibonacci numbers to display: "))
            if isinstance(Times, int) is False or Times < 1:
                raise Exception
        except Exception:
            print("Please be sure to make your input as a positive integer number!")
        else:
            inputComplete = True
    # recursive function
    def Fibonacci(n):
        # base case
        if n <= 1:
            return n
        # recursive case
        else:
            return (Fibonacci(n-1) + Fibonacci(n-2))
    # calculate nTerms
    result = ''
    for i in range(Times):
        result += (str(Fibonacci(i)) + ', ')
    return print(result[:-2])

# Start the Program
HowManyFibonacci()