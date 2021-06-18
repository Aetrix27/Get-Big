import unittest
import random

# Some functions are slightly changed due to pygame not working with unittest

GREEN = (0, 255, 0)


class Circle:
    def __init__(self):
        self.x = random.randint(30, 900)
        self.y = random.randint(30, 700)
        self.pos = (self.x, self.y)
        self.color = GREEN
        self.size = 10


def eatCircle(width, height, points, target_x, target_y, circles):
    for circle in circles:
        if is_colliding(target_x, target_y, circle.x, circle.y, width, height, circle.size, circle.size):
            circles.remove(circle)
            if circle.size == 10:
                width += 2
                height += 2
                points += 2
            elif circle.size == 15:
                width += 5
                height += 5
                points += 5
            elif circle.size == 20:
                width += 10
                height += 10
                points += 10
    return width, height, circles, points


def is_colliding(x1, y1, x2, y2, width, height, width2, height2):
    """Returns True if two shapes are colliding, or False otherwise"""
    # If one rectangle is on left side of the other
    if (x1 >= x2 + width2) or (x2 >= x1 + width):
        return False

    # If one rectangle is above the other
    if (y1 >= y2 + height2) or (y2 >= y1 + height):
        return False

    return True


def quitGame(p_wins, e_wins, event_type):
    if event_type == "QUIT":
        return "quit"
    elif event_type == "KEYUP":
        if p_wins == True:
            return "p_wins"
        elif e_wins == True:
            return "e_wins"


class TestApp(unittest.TestCase):

    def test_eat_circle(self):
        circles = []

        circle1 = Circle()
        circle1.size = 15
        circles.append(circle1)

        width = 20
        height = 20
        points = 0
        target_x = circles[0].x+1
        target_y = circles[0].y+1
        isCorrect = False
        new_width = 0
        new_height = 0
        new_width, new_height, circles, points = eatCircle(
            width, height, points, target_x, target_y, circles)

        if new_width > width and new_height > height and points > 0:
            isCorrect = True

        self.assertTrue(isCorrect, 'Circle cannot be eaten')

    def test_quit_game_logic(self):
        result = ""
        result = quitGame(True, False, "KEYUP")

        self.assertEqual(result, "p_wins")


if __name__ == '__main__':
    unittest.main()
