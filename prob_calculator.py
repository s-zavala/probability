"""
Probability Calculator by Sofia Zavala
"""
import random


class Hat:
    def __init__(self, **contents):
        self.contents = [key for key, value in contents.items()
                         for x in range(value)]
        self.size = len(self.contents)

    def draw(self, num):
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


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


if __name__ == '__main__':
    bowler = Hat(red=5, blue=5)
    a = bowler.draw(5)
    b = bowler.draw(10)
    c = bowler.draw(20)
    print('spam')
