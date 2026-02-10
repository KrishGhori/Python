print("walcome to my game , have fun")
print("\n The gun beats the snake, the water beats the gun, and the snake beats the water")
print("for gun : 1 \n for snek : 2 \n for water : 3 ")
player1 = input("enter your choies between(1 to 3) :- ")
player2 = input("enter your choies between(1 to 3) :- ")


if player1 == '1' or player2 == '1' :
    print(f"player 1 choies is {player1} and player 2 choies is {player2} , so this round will be drow")

elif player1 == '1' and player2 == '2' :
    print(f"player 1 choies is {player1} and player 2 choies is {player2} , so this win by player1")

elif player1 == '1' or player2 == '3' :
    print(f"player 1 choies is {player1} and player 2 choies is {player2} , so this round win by player2")

elif player1 == '2' or player2 == '1' :
    print(f"player 1 choies is {player1} and player 2 choies is {player2} , so this round win by player2")

elif player1 == '2' or player2 == '2' :
    print(f"player 1 choies is {player1} and player 2 choies is {player2} , so this round will be drow")

elif player1 == '2' or player2 == '3' :
    print(f"player 1 choies is {player1} and player 2 choies is {player2} , so this round win by player1")

elif player1 == '3' or player2 == '1' :
    print(f"player 1 choies is {player1} and player 2 choies is {player2} , so this round win by player1")

elif player1 == '3' or player2 == '2' :
    print(f"player 1 choies is {player1} and player 2 choies is {player2} , so this round win by player1")

elif player1 == '3' or player2 == '3' :
    print(f"player 1 choies is {player1} and player 2 choies is {player2} , so this round will be drow")

else :
    print("sorry players, see the rules ")