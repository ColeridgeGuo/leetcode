class TrieNode {

  // R links to node children
  private TrieNode[] children;

  private final int R = 26;

  private boolean isEnd;
  
  private int size; // number of children non null links

  public TrieNode() {
    children = new TrieNode[R];
  }

  public boolean containsKey(char ch) {
    return children[ch - 'a'] != null;
  }
  public TrieNode get(char ch) {
    return children[ch - 'a'];
  }
  public void put(char ch, TrieNode node) {
    children[ch - 'a'] = node;
    size++;
  }
  public void setEnd() {
    isEnd = true;
  }
  public boolean isEnd() {
    return isEnd;
  }
  public int getLinks() {
    return size;
  }
}