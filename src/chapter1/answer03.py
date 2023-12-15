"""03. 円周率
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，
各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""
import re
from typing import List


def split_word(sentence: str) -> List[str]:
    """入力文を空白,コンマ,カンマで区切りし単語群を取得

    Args:
        sentence (str): 入力文
    Returns:
        List[str]: 単語群
    """
    return [word for word in re.split("[ .,]", sentence) if len(word) > 0]

def get_word_count(word_list: List[str]) -> List[int]:
    """単語リストから各単語の文字数リストを取得

    Args:
        word_list (List[str]): 単語リスト
    Returns:
        List[int]: 各単語の文字数の配列
    """
    return [len(word) for word in word_list]

def solution03(text: str) -> List[int]:
    return get_word_count(split_word(text))
