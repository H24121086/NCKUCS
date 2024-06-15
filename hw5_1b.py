import random

# Constants
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Function to deal a card
def deal_card():
    suit = random.choice(suits)
    rank = random.choice(ranks)
    return (rank, suit)

# Function to calculate the score of a hand
def calculate_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        rank = card[0]
        score += values[rank]
        if rank == 'Ace':
            ace_count += 1
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score

# Function to play Blackjack
def play_blackjack():
    # Initialize hands
    hands = {'Player': [], 'Dealer': []}
    
    # Deal initial cards
    for _ in range(2):
        hands['Player'].append(deal_card())
        hands['Dealer'].append(deal_card())
    
    # Player's turn
    while True:
        player_score = calculate_score(hands['Player'])
        print(f"Player's hand: {hands['Player']} (score: {player_score})")
        
        if player_score > 21:
            print("Player busts! Dealer wins.")
            return
        
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            hands['Player'].append(deal_card())
        elif action == 'stand':
            break
    
    # Dealer's turn
    while True:
        dealer_score = calculate_score(hands['Dealer'])
        print(f"Dealer's hand: {hands['Dealer']} (score: {dealer_score})")
        
        if dealer_score > 21:
            print("Dealer busts! Player wins.")
            return
        elif dealer_score >= 17:
            break
        else:
            hands['Dealer'].append(deal_card())
    
    # Final scores and winner
    print(f"Final Player's hand: {hands['Player']} (score: {calculate_score(hands['Player'])})")
    print(f"Final Dealer's hand: {hands['Dealer']} (score: {calculate_score(hands['Dealer'])})")
    
    if calculate_score(hands['Player']) > calculate_score(hands['Dealer']):
        print("Player wins!")
    elif calculate_score(hands['Player']) < calculate_score(hands['Dealer']):
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game
play_blackjack()
