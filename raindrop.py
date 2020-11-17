import argparse

def calculate_rain_drop():
    try:
        user_input = int(input("Enter a number"))
        return user_input
    except ValueError:
        raise ValueError

if __name__ == '__main__':
    calculate_rain_drop()