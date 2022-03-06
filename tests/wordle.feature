Feature: Unfinished Wordle

    Scenario: Puzzle Has Full-Word Hints
        Given a puzzle where the correct answer is "great" 
        And the hints [peach]
        Then all of the hints will be words in the dictionary
        
    Scenario: Hints Say If a Letter is in the Correct Spot
        Given a puzzle where the correct answer is "great" 
        And the hints [fleck]
        Then the hint for "fleck" shows that letters [3] are correct
        And the hint for "fleck" shows that letters [1, 2, 4, 5] are not present

    Scenario: Win on Correct Guess
        Given a puzzle where the correct answer is "great" 
        And the hints [peach]
        When the player guesses "great"
        Then the player sees a win message.

    Scenario: Lose on Incorrect Guess
        Given a puzzle where the correct answer is "great" 
        And the hints [peach]
        When the player guesses "great"
        Then the player sees a lose message.

    