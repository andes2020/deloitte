import argparse

def calculate_rain_drop():
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
        else:
            return result_string
    except ValueError:
        raise ValueError

if __name__ == '__main__':
    print(calculate_rain_drop())