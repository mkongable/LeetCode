#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int hammingWeight(uint32_t n) { //this function counts the number of 1's in a 32-bit unsigned integer
    int count = 0;
    for (int i = 0; i < 32; i++) {
        if (n & 0x1) {
            count++;
        }
        n >>= 1;
    }
    return count;
}

bool isPowerOfTwo(int n) {
    if (n <= 0) {
        return false;
    } else {
        //check to see if there is exactly one 1 in the binary representation of n

        //convert n to uint32_t
        uint32_t n32 = n;
        int count = hammingWeight(n32);
        if (count == 1) {
            return true;
        } else {
            return false;
        }
    }
}

int main() {
    uint32_t n = 1;
    cout << hammingWeight(n) << endl;
    return 0;
}