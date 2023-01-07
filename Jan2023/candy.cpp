#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getDecreasingSequenceLength(vector<int>& ratings, int idx) {
    int length = 1;
    for (int i = idx + 1; i < ratings.size(); i++) {
        if (ratings[i] < ratings[i-1]) {
            length++;
        } else {
            break;
        }
    }
    return length;
}

int candy(vector<int>& ratings) {
    //look at decreasing sequences of ratings and assign the candies accordingly. The bottom of each decreasing sequence should be 1
    vector<int> candies(ratings.size(), -1);
    int idx = 0;

    while (idx < ratings.size()) {
        int decreasingSeqLength = getDecreasingSequenceLength(ratings, idx);

        bool dupBehind;
        if (idx == 0) {
            dupBehind = false;
        } else {
            dupBehind = ratings[idx-1] == ratings[idx];
        }

        if (decreasingSeqLength == 1) { //we are going uphill or staying the same
            if (idx == 0) {
                candies[idx] = 1; //first kid always gets 1 candy
            } else if (!dupBehind) {
                //uphill
                candies[idx] = candies[idx-1] + 1;
            } else {
                //staying the same
                candies[idx] = 1;
            }
        } else {
            //going downhill

            //decreasing sequence length > 1
            vector<int> fillIn (decreasingSeqLength, 0);
            for (int i = 0; i < fillIn.size(); i++) {
                fillIn[i] = decreasingSeqLength - i;
            }

            //get the previous element
            int prevEle = -1;
            if (idx > 0) {
                prevEle = candies[idx-1];
            }

            //see if the first element of the fill array needs to be modified to hurdle over a peak
            if (prevEle >= fillIn[0] && !dupBehind) {
                fillIn[0] = prevEle + 1;
            }

            //fill in the array
            for (int i = 0; i < fillIn.size(); i++) {
                candies[idx + i] = fillIn[i];
            }
            idx += decreasingSeqLength - 1;
        }
        idx++;
    }

    //sum the candies
    int sum = 0;
    for (int i = 0; i < candies.size(); i++) {
        sum += candies[i];
    }

    return sum;
}

int main() {
    vector<int> ratings = {0,1,2,3,2,1};
    cout << candy(ratings);
    return 0;
}