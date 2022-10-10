## Tic-tac-toe

This project started as one tightly-coupled file that allowed the game to be played but made it difficult to add functionality. It also didn't have a competent opponent/computer player because of it's previous 'thinking' algorithm.

It's been improved by refactoring all the code following SOLID principles and implementing MiniMax algorithm to make the computer player intelligent.

The file structure is very clear and it's separated in different components that integrate together in three files to form three different game type classes.

- Human Vs Human
- Human Vs Computer
- Computer Vs Computer -> Fun!

Each component has been unit tested including unittest's mock package to ensure maintainability.

## Requirements

You only need python v3.6 to run the tests and the game. Tests use python's 'unittest', 'unnittest.mock' and some components use python's 'random' and 'copy'.

## How to run

The `game.py` file runs on terminal while the `restful-game.py` runs a RESTful server to run the game from the front-end.

- Clone this repo:

```
  git clone https://github.com/HuascarMC/tictactoe-minimax
```

- Go into the new directory:

```
  cd tic-tac-toe-terminal
```

- (Optional) Install pynput if you would like to run tests

```
  python -m pip install pynput
```

- (Optional) Run all the tests, ensure they all pass (they should):

```
  python core-test.py
```

- Run the game:

```
`python3.6 game.py` OR `python game.py` OR `python -m flask --app restful-game run
```

## Things to be added/improved

- UI, currently runs in terminal.

- Add more tests/test cases.

- On first two moves AI's minimax algorithm runs slow due the depth being high, first computer move takes 3-4 seconds to load.

- GameDisplay class has one method for each 'string' to be displayed in terminal. These methods could be replaced with one method that takes any 'string' as argument but it would make an GUI implementation more difficult.

- ~~Remove commented code.~~

- ~~Extract display functionality into it's own class.~~

- ~~Create parent class for game types.~~

- ~~Remove duplicated code.~~

- ~~Fix stdout coming from tests.~~

- ~Add test coverage for game type classes.~.

```

```
