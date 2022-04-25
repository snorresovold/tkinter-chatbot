class Server:
    # Hvis nokon sender X respons så får de Y svar
    relations = {
        "python": "Python er et programmerings språk utviklet i 1989 av Guido van Rossum",
        "string": "String is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation. Python has a built-in string class named str . Python strings are 'immutable' which means they cannot be changed after they are created",
        "strings": "String is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation. Python has a built-in string class named str . Python strings are 'immutable' which means they cannot be changed after they are created",
        "int":"In Python, integers are zero, positive or negative whole numbers without a fractional part and having unlimited precision, e.g. 0, 100, -10. The followings are valid integer literals in Python.",
        "integer":"In Python, integers are zero, positive or negative whole numbers without a fractional part and having unlimited precision, e.g. 0, 100, -10. The followings are valid integer literals in Python.",
        "bool": "In programming you often need to know if an expression is True or False. You can evaluate any expression in Python, and get one of two answers, True or False. When you compare two values, the expression is evaluated and Python returns the Boolean answer",
        "boolean": "In programming you often need to know if an expression is True or False. You can evaluate any expression in Python, and get one of two answers, True or False. When you compare two values, the expression is evaluated and Python returns the Boolean answer",
        "function": "A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result",
    }

    """
    def request(self, input):
        input.lower() # makes the responses none case sensitive

        for k, v in self.relations.items(): # we get an input from the dict, then return the opposite
            if input in self.relations:
                return v
            else:
                print("not", k, v)
                return "This response was invalid"
    """