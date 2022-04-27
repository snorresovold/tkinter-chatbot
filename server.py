class Server:
    # Hvis nokon sender X respons så får de Y svar
    relations = [
        {"key":"python", "value":"Python is a programming language developed in 1998 by Guido Van Rossum"},
        {"key":"string", "value":"String is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation. Python has a built-in string class named str . Python strings are 'immutable' which means they cannot be changed after they are created"},
        {"key":"strings", "value":"String is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation. Python has a built-in string class named str . Python strings are 'immutable' which means they cannot be changed after they are created"},
        {"key":"int","value": "In Python, integers are zero, positive or negative whole numbers without a fractional part and having unlimited precision, e.g. 0, 100, -10. The followings are valid integer literals in Python."},
        {"key":"integer","value":"In Python, integers are zero, positive or negative whole numbers without a fractional part and having unlimited precision, e.g. 0, 100, -10. The followings are valid integer literals in Python."},
        {"key":"bool", "value":"In programming you often need to know if an expression is True or False. You can evaluate any expression in Python, and get one of two answers, True or False. When you compare two values, the expression is evaluated and Python returns the Boolean answer"},
        {"key":"boolean", "value":"In programming you often need to know if an expression is True or False. You can evaluate any expression in Python, and get one of two answers, True or False. When you compare two values, the expression is evaluated and Python returns the Boolean answer"},
        {"key":"function", "value" : "A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result"},
    ]
    def request(self, input):
        input.lower()  # makes the responses non-case sensitive
        for x in self.relations: # loops through the different items
            if x["key"] in input:  # checks the key
                return(x["value"]) # returns the value



""" # Old request function
    def request(self, input):
        input.lower() # makes the responses none case sensitive

        for k, v in self.relations.items(): # we get an input from the dict, then return the opposite
            print(k, v)
            if input == k:
                return v
            else:
                print("not", k, v)
                return "This response was invalid"
"""