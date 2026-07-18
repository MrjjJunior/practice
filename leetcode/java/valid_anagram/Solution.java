
class Solution {
    public boolean isAnagram(String s, String t) {

        char[] char_t = t.toCharArray();
        char[] char_s = s.toCharArray();

        Arrays.sort(char_t);
        Arrays.sort(char_s);

        if(s.length() != t.length()) {
            return false;
        }
        else if(Arrays.equals(char_s, char_t)){
            return true;
        }
        else{
            return false;
        }

    }
}
