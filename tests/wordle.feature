Feature: Unfinished Wordle

    Scenario Outline: Puzzle Has Full-Word Hints
        Given a puzzle where the correct answer is "<solution>" 
        And the hints [<hints>]
        Then all of the hints will be words in the dictionary

        Examples:
        | solution | hints |
        | stark    | jokes,grade |
        | jokes    | found |
        | marks | there,bombs,plumb | 
        
    Scenario Outline: Hints Say If a Letter is in the Correct Spot
        Given a puzzle where the correct answer is "great" 
        # And the hints [fleck]
        Then the hint for "fleck" shows that letters [3] are correct
        And the hint for "fleck" shows that letters [1, 2, 4, 5] are not present

        # Examples:
        # | solution | hints | hint | correct_indices | unpresent_indices |


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

    