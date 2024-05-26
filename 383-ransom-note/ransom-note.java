class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        char[] ransomArray = ransomNote.toCharArray();
        char[] magazineArray = magazine.toCharArray();

        for(char c : ransomArray){
            int index = new String(magazineArray).indexOf(c);

            if(index == -1){
                return false;
            }

            magazineArray[index] = '.';
        }

        return true;
    }
}