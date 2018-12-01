class Password():
    def __init__(self, pass_phrase):
        self.pass_phrase = pass_phrase

    def check_for_int(self):
        expected_val = ''
        for value in self.pass_phrase:
            if value.isdigit():
                #password has Expected value
                expected_val = value

        if expected_val == '':
            raise ValueError("Your Password Is Missing A Number")
        else:
            return True

    def check_for_lower(self):
        expected_val = ''
        for value in self.pass_phrase:
            if value.islower():
                #password has Expected value
                expected_val = value

        if expected_val == '':
            raise ValueError("Your Password Is Missing A Lower Case Letter")
        else:
            return True

    def check_for_upper(self):
        expected_val = ''
        for value in self.pass_phrase:
            if value.isupper():
                #password has Expected value
                expected_val = value

        if expected_val == '':
            raise ValueError("Your Password Is Missing An Upper Case Letter")
        else:
            return True

    def check_for_characters(self):
        expected_val = ''
        for value in self.pass_phrase:
            if value in "$#@":
                #password has Expected value
                expected_val = value

        if expected_val == '':
            raise ValueError("Your Password Is Missing either an'@', a'#' or a'$'")
        else:
            return True

    def check_for_pass_lenght(self):
        pass_length = len(self.pass_phrase)
        if pass_length < 6:
            raise ValueError("Your Password Must contain At Least 6 Characters")

        elif pass_length in range(6,13):
            return True

        elif pass_length > 12:
            raise ValueError("Your Password Must contain At Most 12 Characters")
