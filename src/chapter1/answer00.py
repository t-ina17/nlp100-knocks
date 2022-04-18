"""00. 文字列の逆順
文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""
def reverse_string(text: str) -> str:
    """文字列を逆順に返却する
    Args:
        text (str): 文字列
    Returns:
        str: 逆順の文字列
    """
    return "".join(list(text[::-1]))

def solution00(text: str) -> str:
    return reverse_string(text)
