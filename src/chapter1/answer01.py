"""01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ
"""
from typing import List


def extract_char(text: str, letters: List[int]) -> str:
    """
    引数の文字列の指定した位置の文字を取り出す

    Args:
        text (str): 抽出対象の文字列
        letters (List[int]): 抽出する位置のリスト
    Returns:
        str: 指定した位置のみの文字列
    """
    return "".join([list(text)[i-1] for i in letters])

def solution01(text: str) -> str:
    return extract_char(text, [1,3,5,7])
