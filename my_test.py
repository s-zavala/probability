import unittest
import prob_calculator


class TestProb(unittest.TestCase):
    def test_Hat(self):
        bowler = prob_calculator.Hat(magenta=5, cerulean=5, polkadot=1)
        actual = bowler.contents
        expected = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta',
                    'cerulean', 'cerulean', 'cerulean', 'cerulean', 'cerulean',
                    'polkadot']
        self.assertEqual(actual, expected, 'Expected a Hat obj with contents matching kwarg types.')

    def test_draw(self):
        beret = prob_calculator.Hat(cyan=3, sienna=3)
        beret.draw(3)
        actual = len(beret.contents)
        expected = 3
        self.assertEqual(actual, expected, 'Expected draw to remove items from contents.')

    def test_experiment(self):
        bucket = prob_calculator.Hat(red=4, black=4)
        ex = prob_calculator.experiment(bucket, expected_balls={'red': 1, 'black': 1},
                                        num_balls_drawn=2, num_experiments=1000)
        actual = ex
        expected = 0.5714
        self.assertAlmostEqual(actual, expected, delta=0.02, msg='Expected a different probability.')


if __name__ == "__main__":
    unittest.main()
