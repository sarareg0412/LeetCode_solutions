class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] ransomArray = ransomNote.toCharArray();

        for(char c : ransomArray){
            int index = magazine.indexOf(c);

            if(index == -1){
                return false;
            }

            magazine = magazine.replaceFirst("" + c, "");
        }

        return true;
    }
}