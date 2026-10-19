class Solution:
    """
    encode a list of strings to a string.
    decode returns the original list of strings
    trick: curate a delimiter, va a tener nombre y apellido
    """
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            num = len(word)
            encoded += str(num) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i < len(s):
            num = ""
            while i < len(s):
                if not s[i].isdigit():
                    break
                num += s[i]
                i += 1
            length = int(num)
            i += 1 # for the delimiter
            word = ""
            for _ in range(length):
                word += s[i]
                i += 1
            strings.append(word)
        return strings




