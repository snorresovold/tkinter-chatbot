class Server:
    # Hvis nokon sender X respons så får de Y svar
    relations = {
        "python": "Python er et programmerings språk utviklet i 1989 av Guido van Rossum"
    }

    def request(self, input):
        input.lower() # makes the responses none case sensitive

        for k, v in self.relations.items():
            if k == input:
                print(v)