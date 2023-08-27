"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""


def valid_parentheses(string: str):
    counter = 0
    for i in string:
        if counter < 0:
            return False
        if i == "(":
            counter += 1
        if i == ")":
            counter -= 1
    return counter == 0




print(valid_parentheses("hi(hi)(())"))

"""
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
hi(hi)()"),True
"""