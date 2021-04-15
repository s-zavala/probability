"""
Probability Calculator by Sofia Zavala
"""
import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, value in kwargs.items()
                         for x in range(value)]

    def draw(self, num: int):
        """
        Given a number, choose at random a ball from
        self.contents without replacement.
        Return a list of strings of the balls picked.
        """
        if num >= len(self.contents): return self.contents
        rec = []
        # Record balls picked.
        for trial in range(num):
            # Repeat num times.
            ball = random.choice(self.contents)
            # Select a random ball.
            rec.append(ball)
            # Store the picked ball in rec.
            self.contents.remove(ball)
            # Remove the picked ball from contents.
        return rec


def experiment(hat, expected_balls: dict, num_balls_drawn: int,
               num_experiments: int):
    """
    Args:
    hat= a Hat object
    expected_balls= a dict with keys of ball colors and
     values of expected number of draws
        eg. {'red': 2, 'green': 3}
    num_balls_drawn= number of balls drawn for each experiment
    num_experiements= number of trials
    Returns a probability.
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


if __name__ == '__main__':
    bowler = Hat(red=5, blue=5)
    p = experiment(bowler, {'red': 2, 'blue': 2}, 5, 100)
    print('Probability: ', p)
