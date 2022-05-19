from random import choice

available_picks = [1, 2, 'a', 'b']

def get_winner():
    winning_numbers = []
    picks = 0
    while picks < 2:
        addition = choice(available_picks)
        winning_numbers.append(addition)
        picks += 1
    # print(f"Any ticket with {winning_numbers} has won!")
    return winning_numbers


def multiple_picks():
    drawings = 0
    while drawings < 5:
        get_winner()
        drawings += 1
        
def check_for_win(name, ticket, winning_ticket):
    print(f"{name} selected: {ticket}")
    if ticket == winning_ticket:
        print("\tWinner!")
    else:
        print("\tMaybe next time")


    
james_ticket = [1, 'a']
sally_ticket = ['a', 'b']
jimmy_ticket = [1, 2]

winning_ticket = get_winner()
print(f"The winning numbers are {winning_ticket}")

# print(f"The winning numbers are {winning_ticket}")

check_for_win('James', james_ticket, winning_ticket)
check_for_win('Sally', sally_ticket, winning_ticket)
check_for_win('Jimmy', jimmy_ticket, winning_ticket)


# multiple_picks()
