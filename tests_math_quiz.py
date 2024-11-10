import unittest
from math_quiz import random_number_generator, operator_selection, math_problem_generator


class TestMathGame(unittest.TestCase):

    def test_random_number_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operator_selection(self):
        operators = ['-','+', '*', '/']
        for _ in range(1000):
            op = operator_selection()
            self.assertIn(op, operators)
            pass

    def test_math_problem_generator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 3, '-', '5 - 3', 2),
                (4, 2, '*', '4 * 2', 8)
            ]

            for num1, num2, operator, exp_prob, exp_ans in test_cases:
                prob, answer = math_problem_generator(num1, num2, operator)
                self.assertEqual(prob, exp_prob)
                self.assertEqual(answer, exp_ans)
                pass

if __name__ == "__main__":
    unittest.main()
