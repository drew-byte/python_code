class Calculator:
    
    def choiceMethod(self,x,y):
        choice = ["Addition","Substraction","Modulo","Division","Multiplication"]
    
        for i in range (0,5):
             print("[",i+1,"] ", choice[i])
             
        z = int(input())
        
        self.lastInput(x,y,z)
    
    def input(self):
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        
        self.choiceMethod(x,y)
        
    
    def lastInput(self,x,y,z):
        if(z == 1):
            answer = x + y
            print(answer)
        elif(z == 2):
            answer = x - y
            print(answer)
        elif(z == 3):
            answer = x % y
            print(answer)
        elif(z == 4):
            answer = x / y
            if (y == 0):
                print("Can not be divide by 0")
                return 
            print(answer)
        elif(z == 5):
            answer = x * y
            print(answer)
            

            
caller = Calculator()
caller.input()
        
    
            
    
    
    