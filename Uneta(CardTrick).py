# Deck of cards
deck = [
    'King of Clubs (Black)',
    'King of Hearts (Red)',
    'King of Spades (Black)',
    'King of Diamonds (Red)',  
    'Queen of Clubs (Black)',
    'Queen of Hearts (Red)',
    'Queen of Spades (Black)',
    'Queen of Diamonds (Red)'
]

# Shuffling of cards
def shuffle_cards(cards):
    top_deck = cards[1::2]
    bottom_deck = cards[0::2]
    return top_deck, bottom_deck

# Get user input
def get_user_input():
    while True:
        user_input = input('Yes/No?: ').lower()  # Convert user input to lowercase
        if user_input == 'yes' or user_input == 'no':
            return user_input
        else:
            print("# Please enter 'yes' or 'no' only")


# Display cards
def display_cards(cards):
    for card in cards:
        print(f"- {card}")


print("Select a card from the options below and press 'Enter' to begin:")
display_cards(deck)
input('...')

#3 round shuffle
for round_number in range(3):
    top_deck, bottom_deck = shuffle_cards(deck)
    
    print('\nDoes cards below contain your card?')
    display_cards(top_deck)

    user_input = get_user_input()

    if user_input == 'yes':
        deck = top_deck + bottom_deck
    else:
        deck = bottom_deck + top_deck

#Card revelation
top_deck, bottom_deck = shuffle_cards(deck)
king_or_queen = top_deck[0]

# Color and Suit
new_bottom_deck, new_top_deck = shuffle_cards(bottom_deck[::-1])
color = new_top_deck[0]
suit = new_bottom_deck[0]
the_right_card = new_bottom_deck[1]

print(f'\nYour card is {the_right_card}')