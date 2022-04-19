"""05. n-gramP
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ
"""
from typing import List, Tuple, Union

from src.chapter1.answer03 import split_word


def get_n_gram(sequence: Union[str, List[str]], N: int) -> List[List[str]]:
    """引数の文字列orリストからn-gramを返却

    Args:
        sequence (Union[str, List[str]]): シーケンス
        N (int): n-gramを構成する数.
    Returns:
        List[str]: シーケンスから取得したn-gramの結果
    """
    res = list()
    for i in range(len(sequence)-N+1):
        res.append(list(sequence)[i:i+N])
    return res

def solution05(text: str) -> Tuple[List[List[str]], List[List[str]]]:
    words = split_word(text)
    word_bi_gram = get_n_gram(words, 2)
    char_bi_gram = get_n_gram(text, 2)
    return word_bi_gram, char_bi_gram
