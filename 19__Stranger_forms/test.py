import unittest
from solution import stranger_forms


class TestStrangerForms(unittest.TestCase):
    def test_stranger_forms(self):
        cinema_layout = [
                '..*...*.**',
                '.....**...',
                '*.*...*..*',
                '.**....*.*',
                '...*..*.*.',
                '.***...*..',
                '*......*.*',
                '.....**..*',
                '..*.*.*..*',
                '***.*.**..'
            ]

        friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]

        expected = [[
            '..*GE.*.**',
            '...CD**...',
            '*.*B..*..*',
            '.**AF..*.*',
            '...*..*.*.',
            '.***...*..',
            '*......*.*',
            '.....**..*',
            '..*.*.*..*',
            '***.*.**..'
            ],
            [
            '..*...*.**',
            '.....**...',
            '*.*.GE*..*',
            '.**.CD.*.*',
            '...*B.*.*.',
            '.***AF.*..',
            '*......*.*',
            '.....**..*',
            '..*.*.*..*',
            '***.*.**..'
            ],
            [
            '..*...*.**',
            '.....**...',
            '*.*...*..*',
            '.**.GE.*.*',
            '...*CD*.*.',
            '.***B..*..',
            '*...AF.*.*',
            '.....**..*',
            '..*.*.*..*',
            '***.*.**..'
            ]]

        self.assertEqual(stranger_forms(cinema_layout, friends_configuration), expected)




    def test_stranger_forms_2(self):
        cinema_layout = [
                '..*...*.**',
                '.....**...',
                '*.*...*..*',
                '.**....*.*',
                '...****.*.',
                '.***...*..',
                '*......*.*',
                '.....**..*',
                '..*.*.*..*',
                '***.*.**..'
            ]

        friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]

        expected = [
            [
            '..*GE.*.**',
            '...CD**...',
            '*.*B..*..*',
            '.**AF..*.*',
            '...****.*.',
            '.***...*..',
            '*......*.*',
            '.....**..*',
            '..*.*.*..*',
            '***.*.**..'
            ]
        ]

        self.assertEqual(stranger_forms(cinema_layout, friends_configuration), expected)


    def test_stranger_forms_3(self):
        cinema_layout = [
                '..***.*.**',
                '.....**...',
                '*.*...*..*',
                '.**....*.*',
                '...****.*.',
                '.***...*..',
                '*......*.*',
                '.....**..*',
                '..*.*.*..*',
                '***.*.**..'
            ]

        friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]

        expected = []

        self.assertEqual(stranger_forms(cinema_layout, friends_configuration), expected)


if __name__ == "__main__":
    unittest.main()