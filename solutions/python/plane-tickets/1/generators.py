"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    seats = {0: "A", 1: "B", 2: "C", 3:"D"}
    for num in range(number):
        yield seats[num % 4]

# print(list(generate_seat_letters(6)))


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    for num, letter in enumerate(generate_seat_letters(number)):
        row = num // 4 + 1
        if row >= 13:
            row += 1

        yield f"{row}{letter}"

# print(list(generate_seats(15)))




    

def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    res = {}
    num_seats = len(passengers)
    seats = generate_seats(num_seats)
    for name in passengers:
        res[name] = next(seats)

    return res
    


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat_num in seat_numbers:
        code = f"{seat_num}{flight_id}"
        zeros = "0" * (12 - len(code))
        yield code + zeros

# print(list(generate_codes(['1A', '17D'], 'C01234')))