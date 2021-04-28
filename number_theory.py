print("This program is designed to take a natural number and return to the user \
its various properties. It will print out the factors of the number and test to \
see if the number is prime or composite. It will test if the number is perfect, \
abundant, or deficient, and if it is amicable. Enter STOP to quit the program.\n")

def main(): 
    stop = False

    while (not stop): # main loop that controls how long the program will run
        num = input("Please enter a natural number (1, 2, 3, etc...), or enter STOP to terminate the program: ")
        if (num.upper() == 'STOP'):
            print("Quitting...done. Goodbye, user.")
            stop = True
            break # a 'STOP' flag ends the loop, and thus the program
        else:
            try:
                num = int(num) # attempt to convert the num into an int
            except: # if the user's input cannot be turned into an integer (it's neither 'STOP' nor a number)
                print("The value you entered is neither 'STOP' nor a number. Please try again.")
                main() # call the function from within the fuction, effectively restarting it
                break # once the main() function called immediately above ends, the rest of this iteration will try to execute. break prevents this by stopping the loop
                
                     

        sumOfProperFactors = 0
        sumOfFactors = 0 # The sum of all factors up to and including the number itself

        if (num <= 0): # the initial test to see if the entered number does NOT meet the conditions for being a positive number
        # if the entered number is legitimate, then the if-statement's condition does not pass, and the else code executes
            print("Error! Please enter a natural number!")
        else:
            if (num % 2 == 0): # num % 2 returns the remainder of the division by two; if it is 0, then the number is divisible by 2 and is even
                print("The number {} is even.".format(num))
            else:
                print("The number {} is odd.".format(num))
            if (num != 1):
                print("The factors of {} are:".format(num), end=' ')
                for factor in range(1, num+1): # here I loop through all numbers ranging from 1 to the original number 
                    if (num % factor == 0): # if the remainder of the division is 0, then the value in factor is a factor of num
                        if (factor == num):
                            print('and {}.'.format(factor)) # if the factor tested is the number itself (the last possible factor) then print it with an 'and'.
                        else:
                            print(factor, end=', ') # if the factor is legitimate but not the last one
                        sumOfFactors += factor # the variable sumOfFactors increments by the value of factor
                        if (factor != 1 and factor != num): # here I test for proper factors (factors that are not equal to 1 or the number itself)
                            sumOfProperFactors += factor 
            else: # if num is 1
                print("The only factor of 1 is 1.")


            if (num != 1):        
                if (sumOfProperFactors > 0):
                    print("The number {} is composite.".format(num)) # if proper factors were located, then the variale sumOfProperFactors should be > 0 and the number is not prime
                else:
                    print("The number {} is prime.".format(num))

           

                if (sumOfFactors - num == num): # since the sum of factors included the number itself, subtracting num from sumOfFactors yields the sum of all positive factors
                    # if the sum of all positive factors of num, not including num, is equal to num, then it is perfect
                    print("The number {} is perfect.".format(num))
                elif (sumOfFactors - num > num):
                    # if the sum of all positive factors of num, not including num, is greater than num, then it is abundant
                    print("The number {} is abundant.".format(num))
                else:
                    print("The number {} is deficient.".format(num))

                amicableNum = sumOfFactors - num # here I set the sum of all positive factors of num, excluding num itself, to equal the variable 'amicableNum'
                # note that amicableNum is the POTENTIALLY amicable number. It is the sum of the positive factors of num, but it's not confirmed that num is the sum
                # of the positive factors of amicableNum
                
                sumOfFactors = 0 # reset the variable for the tests below

                for factor in range(1, amicableNum+1): # same method of testing for factors, excluding the number itself (because of the definition of amicable numbers)
                    if (factor != amicableNum and amicableNum % factor == 0):
                        sumOfFactors += factor
                if (sumOfFactors == num): # if amicableNum's factors equal the original user-entered number
                    print("The numbers {} and {} are amicable.".format(num, amicableNum))
                else:
                    print("The number {} is not amicable.".format(num))
            else: # again, if the original number was 1
                print("The number 1 is neither prime nor composite.")
                print("The number 1 is deficient.")
            print() # newline
            
main() # start the program
