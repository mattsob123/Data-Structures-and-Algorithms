def evalRPN(tokens):
        
        operators = ["+", "-", "*", "/"]
        stack = []
        
        res = 0
        
        for char in tokens:
            print(char)
            if char not in operators:
                stack.append(char)
                print("appended", char)
            else:
                num1 = int(stack.pop(-1))
                if stack != []:
                    num2 = int(stack.pop(-1))
                else:
                    num2 = res
                calc = 0
                if char == "+":
                    print('1')
                    calc = num1 + num2
                elif char == "-":
                    print('2')
                    calc = num1 - num2
                elif char == "*":
                    print('3')
                    calc = num1 * num2
                    print('calc')
                elif char == "/":
                    print('4')
                    calc = num1 // num2
                    print(calc, 'calc')
                res = calc
                print("res", res)
                
        return res

evalRPN(["4","13","5","/","+"])