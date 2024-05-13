# 3D Snake Game with Reinforcement Learning

## Introduction
This project is a 3D implementation of the classic Snake game, designed to showcase the capabilities of reinforcement learning in a more complex spatial environment.

The game is built using Python and integrates with the OpenAI Gym library to provide a standardized environment for training reinforcement learning agents.

You can play the game, train a RL model (DQN,...) or use a pretrained-model to see how well AI is playing.

## Requirements
tbd (probably GPU necessary)


## Installation
We recommend python >= 3.11 (not tested with earlier versions):
1. Clone the repository:
   ```bash
   git clone https://github.com/straeter/Snake3D.git
   cd Snake3D
2. Create and activate a virtual environment:
    ```python
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required Python packages:
    ```python
    pip install -r requirements.txt

## Snake3D Game Rules

In this 3D version of Snake, the game takes place within a 10x10x10 grid with periodic boundaries (left in, right out etc.). The rules are adapted to suit a three-dimensional gameplay:
- Movement: The snake moves forward automatically every time step t. Players can alter the snake's trajectory left, right, up, or down relative to its current direction, but it cannot reverse.
- Objective: The objective is to eat apples that randomly appear in the grid, each of which makes the snake longer.
- End of game: The game ends if the snake collides with itself or if it fills the whole grid
- Reward (default values): +1 for eating an apple, -10 for colliding (dying)

## How to Run It

To run the game, use the following command after installation:
```bash
python main.py
```
This command starts the game environment and the reinforcement learning agent begins its training. You can view the progress in the terminal or modify the render method to create a visual representation.

## Training

tbd


## License

This project is open-sourced under the MIT License. Feel free to use, modify, and distribute the code as you see fit. See LICENSE file for more details.





