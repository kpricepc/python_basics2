# Get user input
data = int(input("What number would you like test to see if it is prime? "))

# FUnction to determine if number is prime or not
def prime(a):
    if a == 1:
        return False
    elif a ==2:
        return True
    else:
        for x in range(2,a):
            if(a % x==0):
                return False
        return True   

# Function to return printed output based off true/false determination
def output(b):
    if b == True:
        print("The number provided is Prime.")
        exit()
    else:
        print("The number provided is not Prime.") 
        exit()  

# Print final output using functions               
print(output(prime(data)))