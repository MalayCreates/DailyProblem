#HW3
#Due Date: 07/12/2020, 11:59PM 
########################################
#                                      
# Collaboration Statement:             
#
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self.top = None
        self.count=0
    
    def __str__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE THIS METHOD
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.__len__ == 0:
            return True
        else:
            return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        return self.count

    def push(self,value):
        # YOUR CODE STARTS HERE
        newNode = Node(value)
        if self.top is not None:
            newNode.next = self.top
            self.top = newNode
        else:
            self.top = newNode
        self.count = self.count + 1

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.top is not None:
            temp = self.top.value
            self.top = self.top.next
            self.count = self.count - 1
            return temp
        else:
            return None


    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() == True:
            return None
        else:
            return self.top.value 


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str) and len(new_expr.strip())>0:
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None


    def isNumber(self, txt):
        if not isinstance(txt,str):
            print("Argument error in isNumber")
            return False
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except ValueError:
            return False



    def _getPostfix(self, txt):
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in _getPostfix")
            return None

        postfixStack=Stack()
        # YOUR CODE STARTS HERE
        myOutput = ""
        temp = ""
        postFix = ""
        operators = ['+', '-', '*', '/', '^']
        digits = "0123456789"
        #for i in txt:
            #if self.isNumber(i) == True:
                #txt[i] = float(txt[i]) 
            #else:
                #return None
       
        for i in txt:
            if i == '(':
                postfixStack.push(i)

            elif i == ')':
                #while ((postfixStack.isEmpty() == False) and postfixStack.peek() != '('):
                    #temp2 = postfixStack.pop()
                    #myOutput.push(temp2)
                #if (postfixStack.isEmpty() and postfixStack.peek() != '('):
                    #return None
                #else:
                    #postfixStack.pop()
                 k = postfixStack.pop()
                 while k != '(':
                    if postfixStack.top == None:
                        return None
                    myOutput += i
                    k = postfixStack.pop()
 

            elif self.isNumber(i):
                i = float(i)
                myOutput += str(i)

            elif i in operators:
                if postfixStack.__len__ == 0:
                    postfixStack.push(i)
                elif postfixStack.__len__ != 0:
                    if i == '^':
                        postfixStack.push(i)
                    elif i == '*' or '/' and postfixStack.top == '+' or '-':
                        postfixStack.push(i)
                    elif i == '*' or '/' and postfixStack.top == '^' or '*' or '/':
                        for j in postfixStack.__len__():
                            if j == '^' or '*' or'/':
                                temp.append(postfixStack.pop())
                            else:
                                postfixStack.push(i)
                                temp.reverse()
                                for k in len(temp):
                                    myOutput += str(i)
                    elif i == '+' or '-':
                        for j in postfixStack.__len__():
                            temp.append(postfixStack.pop())
                        postfixStack.push(i)
                        temp.reverse()
                        for k in len(temp):
                            myOutput += str(i)

        return myOutput


    @property
    def calculate(self):
        if not isinstance(self.__expr,str) or len(self.__expr.strip())==0:
            print("Argument error in calculate")
            return None

        calculatorStack=Stack()
        # YOUR CODE STARTS HERE
        
        calculated = self._getPostfix(self.__expr) #creates an example
        
        if calculated != None:
            operators = ['+', '-', '*', '/', '^']
            calculated = calculated.split() #creates a list
            for i in calculated:
                if self.isNumber(i):
                    calculatorStack.push(i)
                elif i in operators: #checks to see if i is an operator
                    x = float(calculatorStack.pop()) #makes string a float
                    y = float(calculatorStack.pop())

                    if i == '^':
                        value = x ** y
                        calculatorStack.push(value) #gets the answer
                    elif i == '-':
                        value = x - y
                        calculatorStack.push(value)
                    elif i == '+':
                        value = x + y
                        calculatorStack.push(value)
                    elif i == '*':
                        value = x * y
                        calculatorStack.push(value)
                    else:
                        value = x / y
                        calculatorStack.push(value)

            final = calculatorStack.pop() #final answer
            return final 

        else:
            return None   

