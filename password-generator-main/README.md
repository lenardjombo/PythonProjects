1.Imports: The random and string modules are imported. 
random is used for random selection and string provides convenient string constants for letters, digits and punctuation.
2.Generate_password Function: This function takes the desired password length and boolean flags indicating whether to include letters, digits and symbols.
It concatenates the chosen character sets and then randomly selects characters from the combined set to form the password.
3.main Function:

    Welcomes the user and asks for the desired password length.
    Asks whether to include letters, digits, and symbols.
    Calls generate_password with the user's choices and prints the generated password.

4.Input Handling: The program includes basic input validation and error handling to ensure the password length is
a positive integer and at least one character set is selected
