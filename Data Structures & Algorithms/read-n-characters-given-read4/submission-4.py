# read4(buf4: List[str]) -> int is provided by the judge.
class Solution:
    def __init__(self):
        # we need somewhere to store the intermediate, do we acc maybe not
        self.load = [''] * 4
        self.pointer = 0
        self.countread = 0

    def read(self, buf: List[str], n: int) -> int:
        written = 0
        while written < n:
            if self.pointer == self.countread:
                # reload more
                self.countread = read4(self.load)
                if self.countread == 0:
                    break
                self.pointer = 0
            
            # write one character at a time
            buf[written] = self.load[self.pointer]
            written += 1
            self.pointer += 1

        return written