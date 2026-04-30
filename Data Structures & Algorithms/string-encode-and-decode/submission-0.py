class Solution:
        def encode(self, strs: List[str]) -> str:
            res = ""

            for s in strs:
                res += str(len(s)) + "#" + s

            return res

      
        def decode(self, s: str) -> List[str]:
            res = []
            i = 0

            while i < len(s):
                j = i

                # find #
                while s[j] != "#":
                    j += 1
                
                length = int(s[i:j])
                words  = s[j+1 : j+1+length]

                res.append(words)

                i = j + 1 + length

            return res
