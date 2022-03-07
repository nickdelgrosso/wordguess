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
        And the hints [fleck,prove,green,steak]
        Then the hint for "<hint>" shows that letters [<correct_indices>] are correct
        And the hint for "<hint>" shows that letters [<unpresent_indices>] are not present

        Examples:
        | hint | correct_indices | unpresent_indices |
        | fleck | 3 | 1,2,4,5 |
        | prove | 2  | 1,3,4 |
        | green | 1,2,3 | 4,5 |
        | steak | 3,4 | 1,5 |


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

    