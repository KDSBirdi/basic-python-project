import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def chk_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_chk = column[line]
            if symbol != symbol_to_chk:
                break
        else:
            winnings+= values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines 




def get_slot_machine(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print()
                 




def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_lines():
    while 1:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid no. of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while 1:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_lines()

    while 1:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You don't have enough money to bet that amount, your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    
    slots = get_slot_machine(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings, winning_lines = chk_winning(slots, lines, bet, symbol_value)
    print(f"You Won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while 1:
        print(f"Current Balance is: ${balance}")
        ans = input("Press Enter to play! 'q' to quit.")
        if ans == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")
    
    
    # print(balance, lines)


main()