class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);        
        int response = 0;
        int length = s.length();
        for (int i = 0; i < length; i++) {
            int current = map.get(s.charAt(i));            
            if (i < length -1 && current < map.get(s.charAt(i+1))) {
                response -= current;
            } else {
                response += current;
            }
        }
        return response;
    }
}