//https://leetcode.com/problems/jump-game/description/
public boolean canJump(int[] nums) {
    //claim, if the last element can be reached, any element before also can be reached
    int rightPtr = 0; // keeps track of the farthest reached so far
    for (int i = 0; i < nums.length; i++) {
        if (i > rightPtr) {
            //we ran past the rightmost reachable index
            break;
        }
        int lastIdxReached = i + nums[i];
        rightPtr = Math.max(lastIdxReached, rightPtr); //update the frontier if we can extend
    }
    if (rightPtr < nums.length - 1) {
        return false;
    } else {
        return true;
    }
}