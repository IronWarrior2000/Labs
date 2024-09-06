#Bill Nguyen | 9/5/2024 | Calculator

class Calculator: #Created the Calculator Class to hold all of the important function needed for this lab
    def __init__(self, num1, num2): 
        self.num1 = num1 
        self.num2 = num2
        self.operator = ""
        #Created each variable needed for this lab. Num 1, Num 2, and the Operator
        
    def setNum1(self, num1): #Set Num 1
        self.num1 = num1
    
    def setNum2(self, num2): #Set Num 2
        self.num2 = num2

    def setNum3(self, num3): #Set Num 3
        self.num3 = num3

    def setOperator(self, operator): #Set Operator
        self.operator = operator

    def getNum1(self): #Get Num 1
        return self.num1
    
    def getNum2(self): #Get Num 2
        return self.num2

    def getNum3(self): #Get Num 3
        return self.num3

    def getOperator(self): #Get Operator
        return self.operator
    
    def operation(self, operator): #Created the problem solving function
        if operator == "+": #If the operator is a "+"
            self.num3 = self.num1 + self.num2 #Num 1 + Num 2 = Num 3
            return self.num3 #It will also returns.
        elif operator == "-": #else If the operator is a "-"
            self.num3 = self.num1 - self.num2 #Num 1 + Num 2 = Num 3
            return self.num3 #It will also returns.
        elif operator == "x": #else If the operator is a "x"
            self.num3 = self.num1 * self.num2 #Num 1 + Num 2 = Num 3
            return self.num3 #It will also returns.
        elif operator == "/": #else If the operator is a "/"
            if self.num2 != 0: #If num2 is NOT 0 then...
                self.num3 = self.num1 / self.num2 #Num 1 + Num 2 = Num 3
                return self.num3 #It will also returns.
            else: #ELSE...
                return "ERROR CANNOT DIVIDE BY 0" #It will return an Error message


def userinput(): #created a quick and simple way to get the user input as an integer and returns it
    user = int(input(f"Enter in the number here\n")) 
    return user

def operationUser():
    print(f"1. Addition \n2. Subtraction \n3. Multiplication \n4. Division") 
    operator = userinput() #Get the userinput
    if operator == 1: #If the Operator is any number from 1-4 it will reassign Operator as it respective Order of Operation (from above) then return it
        operator = "+"
        return operator
    elif operator == 2:
        operator = "-"
        return operator
    elif operator == 3:
        operator = "x"
        return operator
    elif operator == 4:
        operator = "/"
        return operator
    

def main():
    while True: #While True
        try:
            print(f"Welcome to simple Calculator")
            newCalc = Calculator #new Calculator instance has been created
            
            #Setting up num1 and num2 then using those number to be set in the calculator methods so it can be used in newCalc.Operations.
            #Operations will use the returned operator into it in order to solve the problem that was given.
            num1 = userinput()  
            num2 = userinput()
            newCalc.setNum1(newCalc, num1)
            newCalc.setNum2(newCalc, num2)            
            operator = operationUser()
            num3 = newCalc.operation(newCalc, operator)
            
            #It will print out num1, OPERATOR, num2 = the integer of num3
            print(f"{num1} {operator} {num2} = {int(num3)}")
            
            #User will have the opporunity to end or start another calculation
            repeat = input("Would you like to try another calculation? Yes or No?").upper()
            if repeat == "NO": #IF user does not want to do another calculation it will break the loop
                break
            
        except ValueError: #Gives a ValueError
            print("ValueError")
        except IOError: #Gives an IOError
            print("IOError")


main()