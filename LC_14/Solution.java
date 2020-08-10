/** 
 *  Solution to Leetcode #14 "Longest Common Prefix" using a trie data structure
 */ 
class Solution {
  public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0)
       return "";  
    if (strs.length == 1)
       return strs[0];
    Trie trie = new Trie();      
    for (int i = 1; i < strs.length ; i++) {
      trie.insert(strs[i]);
    }
    return trie.searchLongestPrefix(strs[0]);
  }
  
  public static void main(String[] args) {
    Solution s = new Solution();
    String[] strs = {"cat"};
    System.out.println(s.longestCommonPrefix(strs));
  }
}