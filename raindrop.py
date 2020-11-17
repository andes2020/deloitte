'''This raindrop python script contains a function that
asks user to input an integer and return a string
'Pling' if it is a factor of 3
'Plang' if it is a fcator of 5
'Plong' if it is a factor of 7
Or return the orginal integer'''


def calculate_rain_drop():
    """The calculate raindrop function"""
    try:
        user_input = int(input("Enter a number: "))
        result_string = ''

        if user_input % 3 == 0:
            result_string += 'Pling'
        if user_input % 5 == 0:
            result_string += 'Plang'
        if user_input % 7 == 0:
            result_string += 'Plong'

        # Final check for output
        if result_string == '':
            return str(user_input)
        return result_string
    except ValueError as value_error:
        print("Input error! Please check again!")
        raise ValueError from value_error

if __name__ == '__main__':
    print(calculate_rain_drop())
