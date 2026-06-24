class TimeMap:

    def __init__(self):
        # Initialize an empty dictionary (hash map) to store keys.
        # It will map each key to a list of [timestamp, value] pairs.
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is being seen for the first time, initialize its value as an empty list.
        if key not in self.map:
            self.map[key] = []
        
        # Append the new [timestamp, value] pair to the end of the key's list.
        # Because input timestamps arrive in ascending order, this list stays naturally sorted.
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # If the key does not exist anywhere in our map, return an empty string immediately.
        if key not in self.map:
            return ""
        
        # Retrieve the sorted list of historical [timestamp, value] pairs for this key.
        history = self.map[key]
        
        # Initialize the left pointer 'l' to the start of the history list (index 0).
        l = 0
        
        # Initialize the right pointer 'r' to the end of the history list (last index).
        r = len(history) - 1
        
        # Initialize the result string to an empty string. This serves as our default fallback.
        result = ""
        
        # Loop continues running as long as the search space contains at least one valid element.
        while l <= r:
            # Find the middle index of our current search boundaries using floor integer division.
            mid = (l + r) // 2
            
            # Check if the stored timestamp at the middle index is less than or equal to our query timestamp.
            if history[mid][0] <= timestamp:
                # Since it is valid, update 'result' with this middle string value. It is our best candidate so far.
                result = history[mid][1]
                
                # Because the list is in ascending order, all elements before 'mid' are even smaller.
                # To find a closer past timestamp, we discard the left half and shift our search window to the right side.
                l = mid + 1
            else:
                # If the middle timestamp is greater than our query, it means this time is in the future.
                # Because the list is in ascending order, everything to the right of 'mid' is even further in the future.
                # We discard the future values by shifting our right pointer to search the left side.
                r = mid - 1
        
        # Return the final recorded value, which is the closest valid historical entry, or "" if none existed.
        return result
