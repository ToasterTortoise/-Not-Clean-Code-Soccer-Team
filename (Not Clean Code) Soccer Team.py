# Make a roster and stuff

roster = {}

player1_jersey = int(input('Enter player 1\'s jersey number:'))
player1_rating = int(input('\nEnter player 1\'s rating:\n'))
roster[player1_jersey] = player1_rating
player2_jersey = int(input('\nEnter player 2\'s jersey number:'))
player2_rating = int(input('\nEnter player 2\'s rating:\n'))
roster[player2_jersey] = player2_rating
player3_jersey = int(input('\nEnter player 3\'s jersey number:'))
player3_rating = int(input('\nEnter player 3\'s rating:\n'))
roster[player3_jersey] = player3_rating
player4_jersey = int(input('\nEnter player 4\'s jersey number:'))
player4_rating = int(input('\nEnter player 4\'s rating:\n'))
roster[player4_jersey] =  player4_rating
player5_jersey = int(input('\nEnter player 5\'s jersey number:'))
player5_rating = int(input('\nEnter player 5\'s rating:\n'))
roster[player5_jersey] = player5_rating

sorted_roster = sorted(roster.items())
print('\nROSTER')
for jersey, rating in sorted_roster:
    print('Jersey number: %d, Rating: %d' % (jersey, rating))

menu_selection = 0
while menu_selection != 'q':
    
    menu_selection = input()
    
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print('\nChoose an option:')
    
    if menu_selection == 'o':
        sorted_roster = sorted(roster.items())
        print('\nROSTER')
        for jersey, rating in sorted_roster:
            print('Jersey number: %d, Rating: %d' % (jersey, rating))
    
    elif menu_selection == 'a':
        add_new_player = int(input('Enter a new player\'s jersey number:'))
        roster[add_new_player] = int(input('Enter the player\'s rating:'))
    
    elif menu_selection == 'd':
        delete_player = int(input('Enter a jersey number:'))
        if delete_player in roster:
            del roster[delete_player]
    
    elif menu_selection == 'u':
        find_existing_player = int(input('Enter a jersey number:'))
        edit_player_rating = int(input('Enter a new rating:'))
        roster[find_existing_player] = edit_player_rating
        
    elif menu_selection == 'r':
        prefered_rating = int(input('Enter a rating:'))
        print('ABOVE %d' % prefered_rating)
        for jersey, rating in sorted_roster:
            if rating > prefered_rating:
                print('Jersey number: %d, Rating: %d' % (jersey, rating))
