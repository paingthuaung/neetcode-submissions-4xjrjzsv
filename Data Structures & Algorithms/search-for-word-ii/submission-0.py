class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_index = -1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        root = TrieNode()
        # add all words into trie node
        for i, word in enumerate(words):
            node = root # start from root for each word
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

            node.word_index = i
        
        row = len(board)
        col = len(board[0])
        res = []
        
        def dfs(r, c, parent):
            # 1. Check board boundaries
            if r < 0 or r >= row or c < 0 or c >= col:
                return 

            # 2. Get current character
            ch = board[r][c]

            # 3. Check whether character exists in Trie
            if ch not in parent.children:
                return 
            # 4. Move to the corresponding Trie node
            curr_node = parent.children[ch]
            # 5. Check whether we found a complete word
            if curr_node.word_index != -1:
                res.append(words[curr_node.word_index])
                curr_node.word_index = -1
            # 6. Mark board cell as visited
            board[r][c] = '#'

            # 7. Explore four directions
            dfs(r + 1, c, curr_node)
            dfs(r - 1, c, curr_node)
            dfs(r, c + 1, curr_node)
            dfs(r, c - 1, curr_node)

            # 8. Restore board cell
            board[r][c] = ch
            # PRUNING STEP: If curr_node has no children left, delete it from parent
            if not curr_node.children and curr_node.word_index == -1:
                parent.children.pop(ch)
        
        for r in range(row):
            for c in range(col):
                dfs(r, c, root)
        return res

        

            
        