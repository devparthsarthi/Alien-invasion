# Alien Invasion

A Pygame-based arcade shooter built with Python. Control a spaceship, destroy incoming alien fleets, survive as long as possible, and beat your high score.

## Features

- Keyboard-controlled player ship
- Bullet shooting system
- Alien fleet movement and edge detection
- Collision detection between bullets, aliens, and the player
- Lives system
- Level progression
- Increasing difficulty
- Persistent high score saved locally
- Game Over and Play Again states
- Modular project structure with separate game classes

## Controls

| Key | Action |
|---|---|
| `A` / `Left Arrow` | Move left |
| `D` / `Right Arrow` | Move right |
| `Space` | Fire |
| `P` | Start a new game when inactive |
| `Esc` / `Q` | Quit |

## Requirements

- Python 3.9+
- Pygame 2.5+

## Installation

Clone the repository and install the dependency:

```bash
pip install -r requirements.txt
```

## Run the Game

From the project directory:

```bash
python alien_invasion.py
```

## Project Structure

```text
Alien-invasion/
├── alien_invasion.py
├── alien.py
├── bullet.py
├── button.py
├── game_stats.py
├── high_score.txt
├── requirements.txt
├── scoreboard.py
├── settings.py
├── ship.py
└── images/
    ├── alien.bmp
    └── ship.bmp
```

## Gameplay

Destroy all aliens in a fleet to advance to the next level. Each level increases the game speed and alien point value. Losing all ships ends the game, while the highest score is stored in `high_score.txt`.

## Built With

- Python
- Pygame

## Author

Parthsarthi Sharma
