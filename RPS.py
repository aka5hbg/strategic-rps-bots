# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order={}):
    # If it's the first move, initialize prev_play to 'R'
    if not prev_play:
        prev_play = 'R'

    # Update the opponent's history with the current move
    opponent_history.append(prev_play)
    
    # Default prediction to 'P'
    prediction = 'P'

    # If there are more than 4 moves in history, analyze patterns
    if len(opponent_history) > 4:
        # Create a string of the last 5 moves
        last_five = "".join(opponent_history[-5:])
        # Update the count for this pattern in the play_order dictionary
        play_order[last_five] = play_order.get(last_five, 0) + 1
        
        # Generate potential future patterns based on the last 4 moves
        potential_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]

        # Filter the play_order to include only potential future patterns
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        # If there are valid sub_orders, choose the most frequent pattern's last move
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    # Define the ideal response to counter the predicted move
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # Return the move that beats the predicted move
    return ideal_response[prediction]







