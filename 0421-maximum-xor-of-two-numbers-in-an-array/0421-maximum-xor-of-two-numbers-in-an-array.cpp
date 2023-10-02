#include <iostream>
#include <vector>

using namespace std;

class TrieNode {
public:
    TrieNode* children[2];
    TrieNode() {
        children[0] = nullptr;
        children[1] = nullptr;
    }
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    
    void insert(int num) {
        TrieNode* curr = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr->children[bit] == nullptr) {
                curr->children[bit] = new TrieNode();
            }
            curr = curr->children[bit];
        }
    }
    
    int getMaxLength(int num) {
        TrieNode* curr = root;
        int res = 0;
        for (int i = 31; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr->children[1 - bit] != nullptr) {
                res |= (1 << i);
                curr = curr->children[1 - bit];
            } else {
                curr = curr->children[bit];
            }
        }
        return res;
    }
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        Trie trie;
        int res = 0;
        for (int num : nums) {
            trie.insert(num);
        }
        for (int num : nums) {
            res = max(res, trie.getMaxLength(num));
        }
        return res;
    }
};