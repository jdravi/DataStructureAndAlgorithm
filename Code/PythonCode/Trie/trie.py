class TrieNode:


    def __init__(self):
        self.child = {}
        self.isLast = False
        for char in range(97,123):
            self.child[chr(char)] = None

class Trie:

     def __init__(self):

         self.root = TrieNode()

     def insert(self,string):

         current_node  = self.root
         str_len = len(string)

         for index,each_char in enumerate(string):

             next_node  = current_node.child[each_char]

             if next_node is None:
                 next_node = TrieNode()
                 current_node.child[each_char] = next_node

             current_node = next_node

             if index == str_len-1:
                current_node.isLast = True



     def suggestions(self,root,prefix,res):

        if root.isLast:
            res.append(prefix)
        else:
            for char in range(ord('a'),ord('z')+1):

                if root.child[chr(char)] is not None:

                    self.suggestions(root.child[chr(char)],prefix + chr(char),res)

        return res

     def suggestions_util(self,string):


         prefix = ""

         current_root = self.root
         for each_char in string:

             if current_root.child[each_char] is not None:
                 prefix = prefix + each_char
                 current_root = current_root.child[each_char]
                 print("sugesstion for {} is {}".format(prefix,self.suggestions(current_root,prefix,[])))



















trie  = Trie()
trie.insert("gforgeeks")
trie.insert('geeksquiz')

trie.suggestions_util("gekk")
#print(trie.suggestions(trie.root,"d",[]))
