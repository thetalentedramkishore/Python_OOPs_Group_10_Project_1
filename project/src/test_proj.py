""""This file consists of all the test cases"""
from proj import DataAccess
from proj import main

tst = DataAccess()


def test_marks():
    """"To test marks method"""
    assert tst.marks(99001200) == 1


def test_hobbies():
    """"To test hobbies method"""
    assert tst.hobbies(99001201) == 2


def test_travel():
    """"To test travel method"""
    assert tst.travel(99001214) == 3


def test_languages():
    """"To test languages method"""
    assert tst.languages(99001210) == 4


def test_domain():
    """"To test domain method"""
    assert tst.domain(99001203) == 5
