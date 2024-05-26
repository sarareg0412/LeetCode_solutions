/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int maxGood = 0;
        int minBad = n;
        int curr = 0;

        while(maxGood != minBad - 1){
            curr = maxGood +(minBad-maxGood)/2;
            if(isBadVersion(curr)){
                minBad = curr;
            }else{
                maxGood = curr;
            }
        }

        return minBad;
    }
}