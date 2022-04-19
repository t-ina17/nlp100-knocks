"""06. 集合
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
from typing import Set, Tuple

from src.chapter1.answer05 import get_n_gram


def solution06(text1: str, text2: str) -> Tuple[Set[str], Set[str], Set[str]]:
    X = set(["".join(i) for i in get_n_gram(text1, 2)])
    Y = set(["".join(i) for i in get_n_gram(text2, 2)])

    union = X | Y
    intersection = X & Y
    diff = X - Y

    return union, intersection, diff

