Feature: Unfinished Wordle

    Scenario: Win on Correct Guess
        Given a puzzle where the correct answer is "python"
        When the player guesses "python"
        Then the player sees a win message.

    Scenario: Lose on Incorrect Guess
        Given a puzzle where the correct answer is "mango"
        When the player guesses "python"
        Then the player sees a lose message.
