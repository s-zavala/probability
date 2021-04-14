"""
Probability Calculator by Sofia Zavala
"""


class Hat:
    def __init__(self, **contents):
        self.contents = [key for key, value in contents.items() for x in range(value)]
    
    def draw(self, num):
        pass


if __name__ == '__main__':
    bowler = Hat(red=5, blue=5)
    print('spam')
