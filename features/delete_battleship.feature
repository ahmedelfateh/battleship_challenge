Feature: Delete Battleship Game
    Tests the delete endpoint for the game.

    Background: Request to the API are sent to emulate game playing.
        Given a request url ${BASE_URL}/battleship


    Scenario: A game can be deleted
        This scenario clears the game

        When the request sends DELETE
        Then the response status is OK