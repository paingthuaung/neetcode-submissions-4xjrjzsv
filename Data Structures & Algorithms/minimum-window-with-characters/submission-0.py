class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t contain no char, return empty string
        if t == "":
            return ""
        # create two hashmap, countT for count every char in t
        # window for counting every char in s
        countT, window = {}, {}
        # for every char in t, count how many char present
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        # create have and need, have is what we current have to meet need
        # need is necessary char count to meet condition
        have, need = 0, len(countT)
        # create substring window res and length of substring resLen
        # resLen set initially as biggest number
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            # if current char in s is in t and if total count of 
            # that char in t and s are same, increase have
            if c in countT and window[c] == countT[c]:
                have += 1
            # when have and need are meet, check current window
            # and shrik window as possible
            while have == need:
                # compare current window to current smallest window
                if (r - l + 1) < resLen:
                    # if current window is smaller than smallest window so far
                    # update window, res equal to current left and right
                    res = [l, r]
                    resLen = r - l + 1 # update lenght of window lenght
                # shrink window by removing char from left pointer
                window[s[l]] -= 1
                # if char in left we removed included in t and 
                # our current window count of left char is less 
                # than count of char in t, decrease have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        # get left and right char of smallest window
        l, r = res
        # return if resLen not equal to infinity, r + 1 is necessary
        # because slice char in python not include last char
        return s[l: r + 1] if resLen != float("infinity") else ""
        