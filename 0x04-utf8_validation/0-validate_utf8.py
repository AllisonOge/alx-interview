#!/usr/bin/python3
"""0-validate_utf8.py"""


def validUTF8(data):
    """
    fn to determine if a given set represents a valid UTF-8 encoding

    Params:
        data: List[int] - a list of integers where each integer represent a
        character
    """
    # a valid character should be 1 to 4 bytes long
    def char_isutf8(c):
        """validate character"""
        if c <= 0x7F:  # 1 byte validity
            return True
        if 0x00 == c:  # accept '\0'
            return True
        if 0xC280 <= c and c <= 0xDFBF:  # 2 byte validity
            return (c & 0xE0C0) == 0xC080
        if 0xEDA080 <= c and c <= 0xEDBFBF:
            return False  # reject UTF-16 surrogates
        if 0xE0A080 <= c and c <= 0xEFBFBF:  # 3 byte validity
            return (c & 0xF0C0C0) == 0xE08080
        if 0xF0908080 <= c and c <= 0xF48FBFBF:  # 4 byte validity
            return (c & 0xF8C0C0C0) == 0xF0808080
        return False
    return all(list(map(char_isutf8, data)))
