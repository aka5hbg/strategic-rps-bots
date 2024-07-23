# Rock Paper Scissors

This is the boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

# Explanation(winning strategy)

## Initialization:

- **First Move:** If `prev_play` is empty (i.e., it's the first move), it defaults to 'R'. This ensures that the function has a valid starting move.

## History Tracking:

- **Update History:** Appends the current move (`prev_play`) to `opponent_history`.

## Pattern Tracking:

- **Update Play Order:** If there are more than 4 moves in history, it creates a string `last_five` from the last 5 moves. It updates the count of this pattern in `play_order`.

## Predicting Next Move:

- **Generate Potential Plays:** It constructs potential future patterns by adding each possible move ('R', 'P', 'S') to the last 4 moves in `opponent_history`.
- **Filter and Count Patterns:** Filters the `play_order` to include only patterns from `potential_plays`, then selects the most frequent pattern.

## Decision Making:

- **Prediction:** Determines the most common next move based on the highest count in `sub_order`.
- **Response:** Uses `ideal_response` to counter the predicted move:
  - If the prediction is 'P', the function returns 'S'.
  - If the prediction is 'R', the function returns 'P'.
  - If the prediction is 'S', the function returns 'R'.

## How It Beats the Opponents

- **Against Quincy:**
  - **Pattern:** Quincy follows a fixed pattern (["R", "R", "P", "P", "S"]).
  - **Strategy Advantage:** The player strategy adapts to Quincy’s fixed sequence by learning and predicting patterns over time. Although Quincy’s pattern is simple, the player strategy can eventually adapt and counter the known sequence.

- **Against Mrugesh:**
  - **Pattern:** Mrugesh predicts the next move based on the most frequent move in the last 10 moves.
  - **Strategy Advantage:** The player strategy tracks the last 5 moves and predicts the next move based on recent patterns. If Mrugesh’s frequent move shifts, the player strategy’s prediction mechanism can adapt and counter Mrugesh’s tendencies more effectively.

- **Against Kris:**
  - **Pattern:** Kris always responds with the move that beats the opponent’s last move.
  - **Strategy Advantage:** Since Kris’s strategy is predictable and relies on only the last move, the player strategy, by predicting future moves based on a pattern of the last 5 moves, can effectively counter Kris’s direct response.

- **Against Abbey:**
  - **Pattern:** Abbey uses a pattern-based approach to predict the next move based on the last two moves.
  - **Strategy Advantage:** The player strategy tracks the last 5 moves and generates potential future patterns, allowing it to adapt to Abbey’s pattern-based strategy and respond with a counter move.

## Summary

The player strategy is effective because it combines:

- **Historical Analysis:** It tracks patterns over the last 5 moves to predict future moves.
- **Adaptive Prediction:** It generates potential future patterns and responds based on observed patterns.
- **Ideal Response:** It uses a fixed response strategy to counter predicted moves.

