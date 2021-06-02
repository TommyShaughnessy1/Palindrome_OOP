class Wordclass():
    def __init__(self,name,word):
        self.user_name = name
        self.user_word = word

    def palindrome_check(self):

        # gets user Input,strips white space and converts all letters to lower case
        user_input = f"{self.user_word}".strip().lower()

        #reverses the users input and gets the character at index[0]
        reverse_user_input = user_input[::-1][0]

        # if user_input at index [0] = reverse_user_input [0]

        if user_input[0] == reverse_user_input:
           return "True"
        else:
            return "False"

while True:

    get_name = input("Enter User Name: ")
    get_word = input("Enter your Word: ")

    new_class = Wordclass(get_name,get_word) 
    print(f"Hi {new_class.user_name}! Your word is:{new_class.palindrome_check()}")
    
    


   
    
    






