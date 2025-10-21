# Mindsight: Educational Game

Mindsight is a simple educational game built with Pygame to help users (especially children) learn to identify colors, shapes, and letters. The game is interactive, visually engaging, and designed for quick learning and fun.

## Features
- Select between three categories: Colors, Shapes, or Letters
- Choose two items from the selected category to play with
- Assign keyboard keys (F and J) to each item
- Fullscreen gameplay for immersive experience
- Tracks correct, wrong, and skipped answers, plus response times
- Score summary at the end of each session

## Installation
1. **Install Python 3.7 or higher**
2. **Install Pygame**:
   ```sh
   pip install pygame
   ```
3. **Clone or download this repository**

## Running the Game
Run the game from the command line:
```sh
python mindsight.py
```

## How to Play
1. **Select a Category**: Choose Colors, Shapes, or Letters.
2. **Select Items**: Pick two items from the category (e.g., two colors, two shapes, or two letters).
3. **Assign Keys**: Assign F and J keys to each item.
4. **Gameplay**: Items will appear on the screen. Press the assigned key to identify the item, or Space to skip.
5. **Score Summary**: At the end, view your performance stats.

## Controls
- **Arrow Keys**: Navigate menus
- **Enter/Return**: Select or toggle items
- **Space**: Confirm selections, skip during gameplay, or return to menu
- **F / J**: Identify the displayed item
- **Esc**: Exit gameplay

## Customization
- You can adjust the size of shapes and letters by changing `SHAPE_SIZE` and `LETTER_FONT_SIZE` in `mindsight.py`.
- The game is easy to extend with new shapes, colors, or letters.

## Requirements
- Python 3.7+
- Pygame

## License
MIT License

## Credits
Created by Adam Ferras. Powered by Pygame.
