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

- Clone this repo:
```
git clone https://github.com/HuascarMC/tictactoe-minimax
```
- Go into the new directory:
```
cd tic-tac-toe-terminal
```
- Run all the tests, ensure they all pass (they should):
```
python3.6 core-test.py
```
- Run the game:
```
python3.6 game.py
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
