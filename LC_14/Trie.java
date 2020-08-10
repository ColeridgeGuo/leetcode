/** 
 *  Trie is an efficient information reTrieval data structure. Using Trie, 
 *  search complexities can be brought to optimal limit (key length).
 */ 

class Trie {
  private TrieNode root;

  public Trie() {
    root = new TrieNode();
  }

  // Inserts a word into the trie.
  public void insert(String word) {
    TrieNode node = root;
    for (int i = 0; i < word.length(); i++) {
      char currentChar = word.charAt(i);
      if (!node.containsKey(currentChar)) {
        node.put(currentChar, new TrieNode());
      }
      node = node.get(currentChar);
    }
    node.setEnd();
  }
  
  // search a prefix or whole key in trie and
  // returns the node where search ends
  private TrieNode searchPrefix(String word) {
    TrieNode node = root;
    for (int i = 0; i < word.length(); i++) {
       char curLetter = word.charAt(i);
       if (node.containsKey(curLetter)) {
         node = node.get(curLetter);
       } else {
         return null;
       }
    }
    return node;
  }

  // Returns if the word is in the trie.
  public boolean search(String word) {
     TrieNode node = searchPrefix(word);
     return node != null && node.isEnd();
  }
  
  // Returns if there is any word in the trie
  // that starts with the given prefix.
  public boolean startsWith(String prefix) {
    TrieNode node = searchPrefix(prefix);
    return node != null;
  }
  
  public String searchLongestPrefix(String word) {
    TrieNode node = root;
    StringBuilder prefix = new StringBuilder();
    for (int i = 0; i < word.length(); i++) {
      char curLetter = word.charAt(i);
      if (node.containsKey(curLetter) 
      && (node.getLinks() == 1) 
      && (!node.isEnd())) {
        prefix.append(curLetter);
        node = node.get(curLetter);
      }
      else
        return prefix.toString();

     }
     return prefix.toString();
  }
}