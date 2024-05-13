import gym
from gym import spaces
import numpy as np


class Snake3DEnv(gym.Env):
    """
    Custom Environment for 3D Snake game that follows gym interface.
    This is a simple version of the Snake game where the snake can move in a 3D grid.
    """
    metadata = {'render.modes': ['console']}

    def __init__(self, grid_size=10):
        super(Snake3DEnv, self).__init__()
        self.grid_size = grid_size
        # Define action and observation space
        # They must be gym.spaces objects
        # We have five actions now: 0 = do nothing, 1 = move left, 2 = move right, 3 = move up, 4 = move down
        self.action_space = spaces.Discrete(5)
        # The observation will be the grid itself, flattened
        self.observation_space = spaces.Box(low=-1, high=2, shape=(grid_size, grid_size, grid_size), dtype=np.float32)

        # Initialize state and direction
        self.state = None
        self.snake = []
        self.apple = None
        self.current_direction = np.array([1, 0, 0])  # Initially moving along x-axis

    def reset(self):
        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """
        # Initialize the snake in the center of the grid
        start = self.grid_size // 2
        self.snake = [np.array([start, start, start])]
        self.spawn_apple()
        self.update_state()
        self.current_direction = np.array([1, 0, 0])  # Reset initial direction to x-axis
        return self.state

    def spawn_apple(self):
        """Spawn an apple in a random position excluding the snake's position."""
        while True:
            pos = np.random.randint(0, self.grid_size, size=3)
            if all(not np.array_equal(pos, part) for part in self.snake):
                self.apple = pos
                break

    def update_state(self):
        """Update the grid state based on snake and apple positions."""
        self.state = np.zeros((self.grid_size, self.grid_size, self.grid_size))
        for part in self.snake:
            self.state[tuple(part)] = 1
        self.state[tuple(self.apple)] = -1
        self.state[tuple(self.snake[0])] = 2  # Head of the snake

    def step(self, action):
        """
        This method is called when your agent decides to take an action.
        :param action: (int)
        :return: (np.array, float, bool, dict)
        """
        # Define moves based on action
        move = np.array([0, 0, 0])  # Do nothing action
        if action == 1:  # Move left
            move = np.array([0, -1, 0])
        elif action == 2:  # Move right
            move = np.array([0, 1, 0])
        elif action == 3:  # Move up
            move = np.array([0, 0, 1])
        elif action == 4:  # Move down
            move = np.array([0, 0, -1])

        if np.any(move):
            self.current_direction = move

        new_head = (self.snake[0] + self.current_direction) % self.grid_size

        # Check for collisions with itself
        if any(np.array_equal(new_head, part) for part in self.snake[1:]):
            reward = -10  # Penalty for hitting itself
            done = True
        else:
            self.snake.insert(0, new_head)
            # Check if apple is eaten
            if np.array_equal(new_head, self.apple):
                reward = 10  # Reward for eating an apple
                self.spawn_apple()
            else:
                self.snake.pop()  # Move the snake by removing the tail
                reward = 0
            done = False

        self.update_state()
        return self.state, reward, done, {}

    def render(self, mode='console'):
        if mode != 'console':
            raise NotImplementedError("Other render modes than 'console' are not implemented.")


# Example of using this environment
if __name__ == "__main__":
    env = Snake3DEnv()
    state = env.reset()
    for _ in range(100):
        action = env.action_space.sample()
        state, reward, done, info = env.step(action)
        env.render()
        if done:
            print("Game Over")
            break
