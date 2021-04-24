"""
Probability Calculator by Sofia Zavala
04/14/2021
"""
import random
import copy


class Hat:
    def __init__(self, **kwargs):
        """ Define the sample space.

        Keyword args:
        keys -- types of balls
        values -- quantity of each type
        """
        self.contents = [key for key, value in kwargs.items()
                         for x in range(value)]

    def draw(self, num: int):
        """
        Pick a ball at random from contents num times, w/o replacement.
        Return a list of strings of the type of balls picked.
        """
        if num >= len(self.contents): return self.contents
        rec = []
        for trial in range(num):
            ball = random.choice(self.contents)
            # Select a random ball.
            rec.append(ball)
            self.contents.remove(ball)
            # Remove the picked ball from contents.
        return rec


def experiment(hat, expected_balls: dict, num_balls_drawn: int,
               num_experiments: int):
    """
    Simulate an experiment of drawing a combination of balls from a hat.

    Args:
    hat -- a Hat object
    expected_balls -- a dict with keys of ball colors and
    values of expected number of draws eg. {'red': 2, 'blue': 3}
    num_balls_drawn -- number of balls drawn for each experiment
    num_experiements -- number of trials
    Returns the probability of the drawing a certain combination.
    """
    def compare(list1, list2):
        copy = list2[:]
        for x in list1:
            if x in copy:
                copy.remove(x)
                continue
            else:
                return False
        return True

    event = Hat(**expected_balls)

    success = 0
    for num in range(num_experiments):
        cp = copy.deepcopy(hat)
        res = cp.draw(num_balls_drawn)
        if compare(event.contents, res):
            success += 1
        else: continue
    prob = success / num_experiments
    return prob
