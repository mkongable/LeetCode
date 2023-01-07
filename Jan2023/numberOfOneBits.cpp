#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int hammingWeight(uint32_t n) {
    int count = 0;
    for (int i = 0; i < 32; i++) {
        if (n & 0x1) {
            count++;
        }
        n >> 1;
    }
    return count;
}

int main() {
    uint32_t n = 0b00000000000000000000000000001011;
    cout << hammingWeight(n) << endl;
    return 0;
}