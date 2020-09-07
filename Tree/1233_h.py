class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = defaultdict(dict)
        self.res = []
        
        
        def traverse(path, trie):
            if  '#' in trie :
                self.res.append(path)
                return
            for key in trie:
                traverse(path+'/%s'%key, trie[key])
        
        for path in folder:
            cur = trie
            for d in path.split('/')[1:]:
                if d not in cur :
                    cur[d] = defaultdict(dict)
                cur = cur[d]
            cur['#'] = '#'
            
        for key in trie:
            cur = trie[key]
            # print(key, trie[key])
            traverse('/%s'%key, trie[key])
        
        return self.res