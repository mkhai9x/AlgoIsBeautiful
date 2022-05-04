import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Test;

public class App {
    static public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        int[] counter = new int[26];
        for (char c : sArray) {
            counter[c - 'a']++;
        }
        for (char c : tArray) {
            counter[c - 'a']--;
        }
        for (int count : counter) {
            if (count != 0)
                return false;
        }
        return true;

    }

    public static void main(String[] args) throws Exception {
        System.out.println("Valid Anagram");
    }

    @Test
    public void sampleTest() {
        assertEquals(isAnagram("anagram", "nagaram"), true);
        assertEquals(isAnagram("rat", "car"), false);
        assertEquals(isAnagram("", "car"), false);
        assertEquals(isAnagram("car", ""), false);
    }
}
