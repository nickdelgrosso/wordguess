Feature: Unfinished Wordle

    Scenario Outline: Puzzle Has Full-Word Hints
        Given a puzzle where the correct answer is "stark"
        When the player guesses a non-word "<guess>"
        Then the hint does not get registered in the list of guesses.

        Examples: Vertical
        | guess | dadac | liftd | shurt |
        
    Scenario Outline: Hints Say If a Letter is in the Correct Spot
        Given a puzzle where the correct answer is "<solution>" 
        And the hints [<hint>]
        Then the hint for "<hint>" shows that letters [<correct_indices>] are correct
        And the hint for "<hint>" shows that letters [<misplaced_indices>] are in the wrong position
        And the hint for "<hint>" shows that letters [<unpresent_indices>] are not present

        Examples:
        | solution | hint | correct_indices | misplaced_indices | unpresent_indices |
        | great | fleck | 3 | None | 1,2,4,5 |
        | great | prove | 2  | 5 | 1,3,4 |
        | great | green | 1,2,3 | None | 4,5 |
        | great | steak | 3,4 | 2 | 1,5 |
        | great | flock | None | None | 1,2,3,4,5 |
        | loves | joint | 2 | None | 1,3,4,5 |


    Scenario: Win on Correct Guess
        Given a puzzle where the correct answer is "great" 
        And the hints [peach]
        And the game does not say the player has won
        When the player guesses "great"
        Then the player sees a win message.

    