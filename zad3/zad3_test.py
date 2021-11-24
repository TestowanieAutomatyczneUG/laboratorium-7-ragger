import unittest

from zad3 import statement

invoice = {
    "customer": "BigCo",
    "performances": [
        {
            "playID": "hamlet",
            "audience": 55
        },
        {
            "playID": "as-like",
            "audience": 35
        },
        {
            "playID": "othello",
            "audience": 40
        }
    ]
}

plays = {
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"}
}


class Test_statement(unittest.TestCase):
    def test_example_corret(self):
        self.assertEqual(statement(invoice, plays),
                         "Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n "
                         "Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n")

    def test_wrong_play(self):
        self.assertRaises(ValueError, statement, invoice, {
            "hamlet": {"name": "xx", "type": "xx"},
            "as-like": {"name": "gwegewq", "type": "fweqfwe"},
            "othello": {"name": "fqewfwqe", "type": "trageqfwedy"}
        })

    def test_wrong_play_type_hamlet(self):
        self.assertRaises(ValueError, statement, invoice, {
            "hamlet": {"name": "Hamlet", "type": "ffffff"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        })

    def test_wrong_play_type_as_like(self):
        self.assertRaises(ValueError, statement, invoice, {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "xD"},
            "othello": {"name": "Othello", "type": "tragedy"}
        })

    def test_wrong_play_type_othello(self):
        self.assertRaises(ValueError, statement, invoice, {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "xDDD"}
        })


    def test_random_customer(self):
        self.assertEqual(statement({
            "customer": "random",
            "performances": [
                {
                    "playID": "jan",
                    "audience": 1
                },
                {
                    "playID": "robert",
                    "audience": 2
                },
                {
                    "playID": "marek",
                    "audience": 3
                }
            ]}, {
            "jan": {"name": "Hamlet", "type": "tragedy"},
            "robert": {"name": "As You Like It", "type": "comedy"},
            "marek": {"name": "Othello", "type": "tragedy"}
        }
        ),
            "Statement for random\n Hamlet: $400.00 (1 seats)\n As You Like It: $306.00 (2 seats)\n Othello: $400.00 ("
            "3 seats)\nAmount owed is $1,106.00\nYou earned 0 credits\n")

    def test_key_error_hamlet(self):
        self.assertRaises(KeyError, statement, {
    "customer": "BigCo",
    "performances": [
        {
            "playID": "hamlet",
            "audience": 55
        },
        {
            "playID": "as-like",
            "audience": 35
        },
        {
            "playID": "othello",
            "audience": 40
        }
    ]
}, {"": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"}})
