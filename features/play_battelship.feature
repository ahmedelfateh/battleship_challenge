Feature: Play Battleship Game
    Tests the behavior of the battleship game.

    Background: Request to the API are sent to emulate game playing.
        Given a request url ${BASE_URL}/battleship

Scenario: Shot misses ship

    Given a shot at 4,8
    Then the response status is OK
        And The response json at $.result is equal to "WATER"


Scenario: Shot hits ship
    Given a shot at 3,5
    Then the response status is OK
        And the response json at $.result is equal to "HIT"


Scenario: Can sink a ship
    Given a shot at 7,4
        And a shot at 7,5
        And a shot at 7,6
    Then the response status is OK
        And the response json at $.result is equal to "SINK"


Scenario: Hitting a sinked ship is just a hit
    Given a shot at 6,8
        And a shot at 6,8
    Then the response status is OK
        And the response json at $.result is equal to "HIT"


Scenario: Out of bounds shot is not allowed
    Given a shot at 10,7
    Then the response status is BAD REQUEST
