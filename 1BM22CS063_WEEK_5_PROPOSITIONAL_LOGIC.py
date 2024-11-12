combinations = [
    (True, True, True), (True, True, False), (True, False, True), (True, False, False),
    (False, True, True), (False, True, False), (False, False, True), (False, False, False)
]
variable = {'p': 0, 'q': 1, 'r': 2}
kb = ''
q = ''
priority = {'~': 3, 'v': 1, '^': 2}

# Function to get the knowledge base and query as input
def input_rules():
    global kb, q
    kb = input("Enter rule: ")
    q = input("Enter the Query: ")

# Function to check entailment using truth table
def entailment():
    global kb, q
    print('*' * 10 + " Truth Table Reference " + '*' * 10)
    print('kb', 'alpha')
    print('*' * 10)
    
    for comb in combinations:
        # Evaluate KB and query in current combination
        s = evaluatePostfix(toPostfix(kb), comb)
        f = evaluatePostfix(toPostfix(q), comb)
        print(s, f)
        print('-' * 10)
        
        # If KB is True and query is False in any combination, return False
        if s and not f:
            return False
    return True

# Check if a character is an operand (variable)
def isOperand(c):
    return c.isalpha() and c != 'v'

# Check if a character is a left parenthesis
def isLeftParanthesis(c):
    return c == '('

# Check if a character is a right parenthesis
def isRightParanthesis(c):
    return c == ')'

# Check if a stack is empty
def isEmpty(stack):
    return len(stack) == 0

# Peek at the top of the stack
def peek(stack):
    return stack[-1]

# Check if c1 has less or equal priority than c2
def hasLessOrEqualPriority(c1, c2):
    try:
        return priority[c1] <= priority[c2]
    except KeyError:
        return False

# Convert an infix expression to postfix
def toPostfix(infix):
    stack = []
    postfix = ''
    
    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if isLeftParanthesis(c):
                stack.append(c)
            elif isRightParanthesis(c):
                operator = stack.pop()
                while not isLeftParanthesis(operator):
                    postfix += operator
                    operator = stack.pop()
            else:
                while (not isEmpty(stack)) and hasLessOrEqualPriority(c, peek(stack)):
                    postfix += stack.pop()
                stack.append(c)
    
    while not isEmpty(stack):
        postfix += stack.pop()
    
    print("Postfix of", infix, "is", postfix)  # Debugging statement
    return postfix


def evaluatePostfix(exp, comb):
    stack = []
    for i in exp:
        if isOperand(i):
            # Push the corresponding value from the combination
            stack.append(comb[variable[i]])
        elif i == '~':
            # Check if there’s at least one operand to apply NOT
            if stack:
                val1 = stack.pop()
                stack.append(not val1)
            else:
                print("Error: Not enough operands for '~'")
        else:
            # Check if there are at least two operands for binary operators
            if len(stack) < 2:
                print("Error: Not enough operands for operator", i)
                return False
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(_eval(i, val2, val1))
    
    # The final result should be the only value in the stack
    return stack.pop() if stack else False


# Evaluate a logical operation for two boolean values
def _eval(i, val1, val2):
    if i == '^':
        return val2 and val1
    return val2 or val1

# Main code to take input and check entailment
input_rules()
ans = entailment()
if ans:
    print("The Knowledge Base entails query")
else:
    print("The Knowledge Base does not entail query")
