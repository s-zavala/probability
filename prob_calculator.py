"""
Probability Calculator by Sofia Zavala
"""
import random


class Hat:
    def __init__(self, **contents):
        self.contents = [key for key, value in contents.items()
                         for x in range(value)]
        # self.size = len(self.contents)

    def draw(self, num):
        """
        Given a number, choose at random a ball from
        self.contents without replacement.
        Args: num=int
        Return a list of strings=the balls picked.
        """
        sample = self.contents[:]
        balls = []
        for draw in range(num):
            try:
                ball = random.choice(sample)
            except IndexError:
                sample = self.contents[:]
                ball = random.choice(sample)
            sample.remove(ball)
            balls.append(ball)
        return balls
        # Using random.choices()
        # result = []
        # if num > self.size:
        #     reps = num // self.size
        #     extra = num % self.size
        #     for x in range(reps):
        #         draw = random.choices(sample, k=self.size)
        #         result.extend(draw)
        #     draw = random.choices(sample, k=extra)
        #     result.extend(draw)
        #     return result
        # else:
        #     return random.choices(sample, k=num)


def experiment(hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    """
    Args:
    hat= a Hat obj
    expected_balls= a dict with keys= ball colors and
     values= expected number of draws
        eg. {'red': 2, 'green': 3}
    num_balls_drawn= number of balls drawn for each experiment
    num_experiements= number of trials
    Returns a probability.
    """
    prob = 1
    for num in range(num_experiments):
        res = hat.draw(num_balls_drawn)
        count = dict.fromkeys()
    return prob


if __name__ == '__main__':
    bowler = Hat(red=5, blue=5)
    a = bowler.draw(5)
    b = bowler.draw(10)
    c = bowler.draw(20)
    print('spam')
