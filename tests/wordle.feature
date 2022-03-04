Feature: Unfinished Wordle

    Scenario: Puzzle Description
        Given a puzzle where the correct answer is "great"
        Then all of the hints will be words in the dictionary

    Scenario: Win on Correct Guess
        Given a puzzle where the correct answer is "python"
        When the player guesses "python"
        Then the player sees a win message.

    Scenario: Lose on Incorrect Guess
        Given a puzzle where the correct answer is "mango"
        When the player guesses "python"
        Then the player sees a lose message.

    