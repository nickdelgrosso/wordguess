Feature: Unfinished Wordle

    Scenario: Win on Correct Guess
        Given a puzzle where the correct answer is "python"
        When the player guesses "python"
        Then the player sees a win message.