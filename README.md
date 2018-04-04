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
cd tictactoe-minimax
```
- Run all the tests, ensure they all pass (they should):
```
python3.6 core-test.py
```
- Run the game:
```
python3.6 game.py
```

## Things to be added

- UI, currently runs in terminal.

- More tests/test cases.

- On first two moves AI's minimax algorithm runs slow due the depth being high, first computer moves take around 3-4 seconds to load.
