In this game, the player plays against a computer to collect dots to get bigger before the
computer does. If the player is bigger than the computer, they can eat them, and then win
the game. They can select to play again or quit in the menu screens.

### Play the game at the link by running it at the top: https://repl.it/@Aetrix/Get-Big#main.py

---

## Documentation

| Functions    |                     Parameters                     |                                                              Description                                                               |
| ------------ | :------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------: |
| eatCircle    | width, height, points, target_x, target_y, circles |               Player eats a circle by colliding with it, and removing the circle and increasing in size (width, height)                |
| quitGame     |               p_wins, e_wins, clock                | Quits the game by checking if the player or enemy won, and displaying a game over message, player and enemy win variables are booleans |
| is_colliding |   x1, y1, x2, y2, width, height, width2, height2   |                             Will return true if two shapes are colliding, and if not it will return false                              |
| draw_text    |            text, color, font_size, x, y            |                                                Draws menu text, x and y are size inputs                                                |

---

### Classes

See the initialization for the classes below:
Circles fill up the board and can be eaten, the Text Boxes are the menu text objects that are created

```python
class Circle:
    def __init__(self):
        self.x = random.randint(30, 900)
        self.y = random.randint(30, 700)
        self.pos = (self.x, self.y)
        self.color = GREEN
        self.size = 10

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.size)


class TextBox:
    def __init__(self, position_x, position_y, height, width, inner_color):
        self.position_x = position_x
        self.position_y = position_y
        self.size_height = height
        self.size_width = width
        self.inner_color = inner_color
        self.rect = pygame.Rect(
            self.position_x, self.position_y, self.size_width, self.size_height)

    def display(self, screen):
        pygame.draw.rect(screen, self.inner_color, (self.position_x,
                                                    self.position_y, self.size_width, self.size_height))

```
