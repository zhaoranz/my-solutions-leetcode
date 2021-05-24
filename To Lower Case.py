class Solution:
    def toLowerCase(self, s: str) -> str:
        res =''
        for ch in s:
            if ord(ch) >=65 and ord(ch)<=90:
                res += chr(ord(ch)+32)
            else:
                res += ch
        return res
#C++
class Solution {
public:
    string toLowerCase(string s) {
        for(auto &i: s) i |= 32;
        return s;
        
    }
};
