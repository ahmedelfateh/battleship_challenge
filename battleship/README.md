# Battle Ship

This repo is the start-up point to submit the battleship game exercise for
Profit Tools. It's recommended you read all the instructions before you start
the exercise.

The exercise will be timed to 24 hours starting at the time you gain access to
the repo. The solution should be submitted through a pull request into the repo.

## The Goal

The goal of this exercise is to evaluate your object oriented programming skills.
The solution should have an adequate object oriented design, and demonstrate 
good separation of concerns.

There are tests setup to validate the requirements of the exercise. Below, there
are instructions on how to run them, in case you want to validate your work
before submitting the exercise.

The results from these tests are not the main factor to evaluate the solution. 
Instead, the code implementation and design will be evaluated, but it doesn't
hurt that the tests pass.

Unit tests are an important factor for our projects. Writting unit tests for the
solution is a big plus. The unit tests should be written in the `test` folder, 
and can be executed using the `bolt ut` command. 

You can run the unit tests and have them monitor changes using the `bolt ct` 
command. The tests will be executed every time changes are saved.

## Setup the Development Environment

This exercise should be completed using Python 3.6 or higher. Solutions that 
don't work in that version of Python will not be accepted. Make sure you have
the right Python version.

Start by cloning the repo or creating your own fork. Once you've clone or forked 
the repo and downloaded all the source locally, you can install the necessary 
requirements by running:

```console
$ pip install -r requirements.txt
```

There are some commands that you can run to help you during development:

* `bolt ut` will run the unit test located in the test folder. The project uses
nose to run the tests, but the tests can be implemented with the `unittest`
module in Python.
* `bolt ct` will run the unit tests and wait for file changes. You can use the
command to follow TDD during development. The command can be killed with `<ctrl+c>`.
* `bolt ft` will run the feature tests. The feature tests validate the requirements
of the exercise, so you can use them to verify that your code works against the
specification.

## The Problem

The exercise is to implement the Battleship Game from the perspective of a
single user. The game exposes and endpoint `http://localhost:/5000/battleship`
that supports three HTTP methods:

* `POST` Creates a new game. The payload contains the ships for the game (more
on this below).
* `PUT` Used to specify a shot against the game. The payload contains the 
coordinates for the shot.
* `DELETE` Deletes the current game.

All the functions for the endpoints have already been provided in the
`/battleship/api.py` file. You need to fill the implementation.

You should add your model and business logic classes into a separate module(s).
The architecture will also be evaluated.

### Creating a New Game

A new game will be created by a `POST` request to the endpoint. The payload will
contain the definition of where the ships are located. The payload will look
as follows:

```json
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
```

The game board must have a 10x10 dimension. The indices to the board are 0 based
from 0 to 9. The payload indicates the location of the shipment (its origin), 
its size, and directiion. Ships are located along the horizontal or vertical 
axis, and will never be located diagonally.

The sample payload above shows 4 ships added to the board. The first one starts
at coordinate (2,1) with a size of 4 (meaning 4 squares) and a horizontal
direction. The `direction` parameter will have a value of `H` for horizontal and
`V` for vertical.

The endpoint should create a new game based on the specified payload. The game
can be kept in a global variable, so it becomes available for playing in
subsequent requests.

You don't need to consider multiple threads, games, or players. All the scenarios
will be run as a single player in a single threaded application. And they will
be executed synchronously.

The following scenarios should be considered:

**A correct game definition is sent in the payload**. The endpoint should create
the game and return OK.

**At least one of the ships falls beyond the size of the board**. The endpoint 
should detect the problem and return BAD REQUESTS. As an example, a ship with
an origin `x=8`, `y=1`, `size=4`, and `direction=H` falls out of the board.
Remember that coordinates are 0 based.

**Two shipments overlap. Shipments should not overlap**. If they do, the endpoint
should detect the problem and return BAD REQUEST. The following shipments overlap:

```json
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
        }
    ]
}
```

**NOTE**: Creating a game overwrites any previously created game.

### Playing the Game

The game is played by sending `PUT` requests to the endpoint. The payload will
contain the coordinates of a shot, and it'll look as follows:

```json
{
    "x": 5,
    "y": 4
}
```

The endpoint should return a response payload indicating the result:

```json
{
    "result": "WATER"
}
```

The result value should follow these rules:

* A missing shot should return a result of "WATER".
* A hit shot should return a result of "HIT".
* A hit for the last piece of a ship should return "SINK"
* Hitting an already sinked ship should return "HIT"

All these responses should return a status of OK.

A shot that falls outside of the board should return a status of BAD REQUEST.
As an example `x=10` and `y=7` falls outside of the board.

### Deleting a Game

A game can be deleted by sending a `DELETE` request to the endpoint. Deleting
a game allows to start the game from scratch.

Good luck!
