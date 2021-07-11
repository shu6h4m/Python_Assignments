from stack import Stack #Importing Stack Class

def postfix(exp):
    '''
    To Convert infix expression to postfix
    Input : exp-string (Infix Expression)
    Return : result-string (Postfix Expression)
    '''
    precedence = {'+':1,'-':1, '*':2, '/':2}
    operand = '0123456789' #string of valid operands
    result = ''
    stk = Stack()
    for symbol in exp:
        if symbol == '(':
            stk.push(symbol)
        elif symbol == ')':
            val = stk.pop()
            while val != '(':
                result += val
                val = stk.pop()
        elif symbol in operand:
             result += symbol
        elif symbol in precedence:
            if not (stk.isEmpty()):
                stkTop = stk.top()
            while not(stk.isEmpty()) and stkTop != '(' and precedence[ stkTop ] >= precedence [ symbol ]:
                result += stkTop
                stk.pop()
                if not (stk.isEmpty()):
                    stkTop = stk.top()
            stk.push(symbol)
    while not(stk.isEmpty()):
        result += stk.pop()
    return result

def main():
    '''
    To convert infix expression provided by user
    Takes infix expression and return
    Postfix expression
    '''
    exp = input('\nEnter the Expression in infix notation: ')
    exp = postfix(exp)
    print("\nPostfix Notation of given Expression is: ",exp)

if __name__ == '__main__': #Calling Main
    main()