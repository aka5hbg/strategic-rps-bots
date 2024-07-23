# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# RPS.py

# RPS.py

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    
    # Default to "R" if there is no previous play
    if not opponent_history:
        return "R"
    
    # A simple frequency-based strategy
    moves = ["R", "P", "S"]
    move_counts = {"R": 0, "P": 0, "S": 0}
    
    for move in opponent_history:
        move_counts[move] += 1
    
    # Find the most frequently played move by the opponent
    most_common_move = max(move_counts, key=move_counts.get)
    
    # Define a counter-strategy for each possible move
    counter_strategies = {"R": "P", "P": "S", "S": "R"}
    
    # Play the counter to the most frequently played move
    return counter_strategies[most_common_move]

