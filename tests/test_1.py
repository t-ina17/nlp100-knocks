import pytest
from src.chapter1.answer00 import solution00
from src.chapter1.answer01 import solution01
from src.chapter1.answer02 import solution02
from src.chapter1.answer03 import solution03
from src.chapter1.answer04 import solution04
from src.chapter1.answer05 import solution05
from src.chapter1.answer06 import solution06


def test_00():
    actual = solution00("stressed")
    expected = "desserts"
    assert actual == expected

def test_01():
    actual = solution01("パタトクカシーー")
    expected = "パトカー"
    assert actual == expected

def test_02():
    actual = solution02("パトカー", "タクシー")
    expected = "パタトクカシーー"
    assert actual == expected

def test_03():
    actual = solution03("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
    expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    assert actual == expected

def test_04():
    actual = solution04("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
    expected = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
    assert all( (k,v) in actual.items()
            for (k,v) in expected.items() )

def test_05():
    actual01, actual02 = solution05("I am an NLPer")
    expected01 = [["I", "am"], ["am", "an"], ["an", "NLPer"]]
    expected02 = [["I", " "], [" ", "a"], ["a", "m"], ["m", " "], 
                [" ", "a"], ["a", "n"], ["n", " "], [" ", "N"],
                ["N", "L"], ["L", "P"], ["P", "e"], ["e", "r"]]
    assert actual01 == expected01
    assert actual02 == expected02

def test_06():
    actual01, actual02, actual03 = solution06("paraparaparadise", "paragraph")
    expected01 = {'ad', 'ph', 'se', 'pa', 'ra', 'di', 'ag', 'is', 'ap', 'ar', 'gr'}
    expected02 = {'pa', 'ap', 'ar', 'ra'}
    expected03 = {'di', 'ad', 'is', 'se'}
    assert actual01 == expected01
    assert actual02 == expected02
    assert actual03 == expected03
    assert ("se" in actual01) == True
    assert ("se" in actual02) == False
    assert ("se" in actual03) == True
