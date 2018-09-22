#check if the size of the given parenthesis is 'ODD' then return false
#Scan the Parenthesis from left --> right and for every added Open bracket in the stack check if the current parenthesis is a right close one
#also check if the stack size of Open parenthesis is '0'
def balanced_parenthesis(parenthesis):
    print(parenthesis)

    #check if the lenght is odd if so then exit
    if len(parenthesis)%2 != 0:
        return False
    #set to hold all the Open parenthesis
    openParenthesis = set('({[')
    print(openParenthesis)
    #declare a tuple to hold the open and close combinations
    matchingParenthesis = set([ ('(',')'), ('[',']'), ('{','}') ])
    print(matchingParenthesis)
    #defina s stack
    stack = []
    for paren in parenthesis:
        if paren in openParenthesis:
            stack.append(paren)
        else:
            if len(stack) == 0:
                print('HERE---')
                return False
            #now pop the last open parenthesis and check if the current paren is the matching close
            last_open = stack.pop()
            print(last_open)
            if(last_open,paren) not in matchingParenthesis:
                return False
    return len(stack) == 0

isBalanced = balanced_parenthesis('{([)}')
print(isBalanced)
