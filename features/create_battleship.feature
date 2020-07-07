Feature: Create Battleship Game
    Test the creation of the battleship game.

    Background: Request to the API are sent to emulate game playing.
        Given a request url ${BASE_URL}/battleship

    Scenario: Battleship game can be created
        This scenario tests that a battleship game can be created with a 
        correct representation of ships.

        Given a request json payload
            """
            {
                "ships": [
                    {
                        "x": 2,
                        "y": 1,
                        "size": 4,
                        "direction": "H"
                    },
                    {
                        "x": 7,
                        "y": 4,
                        "size": 3,
                        "direction": "V"
                    },
                    {
                        "x": 3,
                        "y": 5,
                        "size": 2,
                        "direction": "V"
                    },
                    {
                        "x": 6,
                        "y": 8,
                        "size": 1,
                        "direction": "H"
                    }
                ]
            }
            """
        When the request sends POST
        Then the response status is OK


    Scenario: Specified ships fall outside of game board
        This scenario tests that the game cannot be created because at least
        one of the specified ships is outside of the game board.

        Given a request json payload
            """
            {
                "ships": [
                    {
                        "x": 8,
                        "y": 1,
                        "size": 4,
                        "direction": "H"
                    },
                    {
                        "x": 7,
                        "y": 4,
                        "size": 3,
                        "direction": "V"
                    },
                    {
                        "x": 3,
                        "y": 5,
                        "size": 2,
                        "direction": "V"
                    },
                    {
                        "x": 6,
                        "y": 8,
                        "size": 1,
                        "direction": "H"
                    }
                ]
            }
            """
        When the request sends POST
        Then the response status is BAD REQUEST


    Scenario: Specified ships overlap
        This scenaro test that the game cannot be created because at least two
        ships overlap

        Given a request json payload
            """
            {
                "ships": [
                    {
                        "x": 5,
                        "y": 5,
                        "size": 4,
                        "direction": "H"
                    },
                    {
                        "x": 7,
                        "y": 4,
                        "size": 3,
                        "direction": "V"
                    },
                    {
                        "x": 3,
                        "y": 5,
                        "size": 2,
                        "direction": "V"
                    },
                    {
                        "x": 6,
                        "y": 8,
                        "size": 1,
                        "direction": "H"
                    }
                ]
            }
            """
        When the request sends POST
        Then the response status is BAD REQUEST


