Intro to Testing
================

---

Overview
--------

- Why test?
- Writing tests
- Using nose
- Using mock
- Tips

---

Why test your code?
-------------------

- Did you ever realize something you wrote was wrong weeks after you wrote it?
- Ever had a program run for hours and then crash while saving the results?
- Do you want to publish something that is _wrong_?
- Can you refactor your code without fear?
- Could someone else change your codebase without breaking things?
- Is your code tightly coupled?

---

unittest (built into python)
----------------------------

- to test calc.py, make calc_tests.py
- make a class that extends unittest.TestCase
- for each test:
    - arrange - set up the environment
    - act - run your code
    - assert - say what should have happened

---

minimal unittest example
------------------------

calc.py:

    !python
        def eval_tokens(expression):
            return 7

test_calc.py:

    !python
        import operator, unittest, calc

        class TestCalc(unittest.TestCase):
            def test_eval_tokens(self):
                # arrange
                tokens = [3,operator.add,4]
                # act
                res = calc.eval_tokens(tokens)
                # assert
                self.assertEqual(res,7)

---

nosetests
---------
nose finds and runs tests for you

    >pip install nose mock
    >nosetests
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.055s

    OK

Tip: `nosetests -s` will let you see print statements and use pdb
---

mock
----

- temporary monkey-patching - replace one class, function or method with
  another. For example, you can make your own sys.stdin
- mock objects - objects that behave like other objects. You could make
  something that looks like Tweepy, but doesn't talk to Twitter.

---

patch example
------------

    !python
    import mock
    import random

    def fake_randint(a,b):
        return 4

    with mock.patch('random.randint', fake_randint):
        print random.randint(1,6)
        print random.randint(10,20)
    print random.randint(10,20)

------

mock example
------------

    !python
    import mock, requests

    def function_to_test():
        resp = requests.get("http://infolab.tamu.edu")
        if resp.status_code!=200:
            raise Exception("Rquest failed!")
        return " ".join(resp.iter_lines())

    def fake_get(url):
        assert 'infolab' in url
        result = mock.MagicMock()
        result.status_code = 200
        result.iter_lines.return_value = ['hello','world']
        return result

    with mock.patch('requests.get',fake_get):
        print function_to_test()

---

tips
----

- functional and decoupled code is easier to test -> good code is easy to test
- When you don't know what to write, write the test backwards - you know what
  to assert
- library code needs more tests
- you can write the tests first
- test as you go, don't go back and test legacy code
- mock external APIs like Twitter
- put the tests for `base/models.py` in `base/tests/models_tests.py`.
- be pragmatic - 100% coverage is not always something to strive for

---

Questions?
==========
