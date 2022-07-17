############### Blackjack Project #####################
import random
from art import logo
from replit import clear
 
def play_blackjack():
    print(logo)
    def deal_card():
        """Returns a random card from the list of cards"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    user_cards = []
    computer_cards = []
    is_game_over = False
    
    def calculate_score(card_list):
        """Returns the sum of cards """
        if sum(card_list) == 21 and len(card_list) == 2:
            return 0
        if 11 in card_list and sum(card_list) > 21:
            card_list.remove(11)
            card_list.append(1)
        return sum(card_list)
    def compare(computer_score,user_score):
        if computer_score == user_score:
            return 'It is a draw 😐'
        elif computer_score == 0:
            return "Opponent got a blackjack 🥲"
        elif user_score == 0:
            return "You got a blackjack 🤗"
        elif user_score > 21:
            return 'You went over, You lose 😭'
        elif computer_score > 21:
            return "Opponent went over, You win 😊"
        elif user_score > computer_score :
            return "You win 😉"
        else:
            return "You lose 😥"
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
 
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score is {user_score}")
        print(f"computer card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to continue or 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand is : {user_cards} , current score is {user_score}")
    print(f"Opponent final hand is : {computer_cards} , current score is {computer_score}")
    print(compare(computer_score,user_score))

while input("Do you want to play blackjack Type 'y' for yes or 'n' for no: ") == 'y':
    clear()
    play_blackjack()
    


