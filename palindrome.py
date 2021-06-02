def palindrome_check():

    # gets user Input,strips white space and converts all letters to lower case
    user_input = input("Enter a Word: ").strip().lower()

    #reverses the users input and gets the character at index[0]
    reverse_user_input = user_input[::-1][0]

    # if user_input at index [0] = reverse_user_input [0]
    if user_input[0] == reverse_user_input:
        print(True)
    else:
        print(False)

        
palindrome_check()


