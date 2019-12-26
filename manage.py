#!/usr/bin/env python

from app import create_app, db


app = create_app( 'default')



def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


def userDB():    pass


if __name__ == '__main__':
    test()
