"""02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""
def concat_alternately(text1: str, text2: str) -> str:
    """文字列を交互に連結する. 一方が多い場合はそのまま連結する

    Args:
        text1 (str): 文字列1
        text2 (str): 文字列2
    Returns:
        str: 連結した文字列
    """
    min_length = min(len(text1), len(text2))
    tmp = "".join([i+j for i,j in zip(text1[:min_length], text2[:min_length])])
    if len(text1) > min_length:
        return tmp+"".join(text1[min_length:])
    else:
        return tmp+"".join(text2[min_length:])

def solution02(text1: str, text2: str) -> str:
    return concat_alternately(text1, text2)
