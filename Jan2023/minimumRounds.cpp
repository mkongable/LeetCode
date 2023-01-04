#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

int minimumRounds(vector<int>& tasks) {
    //https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
    
    /*create a map to map task difficulty to the number of occurrences
    if the number of occurences of a difficulty is 1, then we cannot sort it out
    if the number of occurences of a difficulty is greater than 1, then there are several cases:
        case 1: occurences % 3 == 0, then we can sort it out in occurences / 3 rounds
        case 2: occurences % 3 == 1, then we can sort it out in occurences / 3 + 1 rounds
        case 3: occurences % 3 == 2, then we can sort it out in occurences / 3 + 1 rounds
    loop through every difficulty and its number of occurrences and calculate the number of rounds needed to process it
    return the result
    */
   //create unordered_map to map difficulty to number of occurrences
    unordered_map<int, int> map;
    for (int i = 0; i < tasks.size(); i++) {
        if (map.find(tasks[i]) == map.end()) {
            map[tasks[i]] = 1;
        } else {
            map[tasks[i]]++;
        }
    }

    //loop through every difficulty and its number of occurrences and calculate the number of rounds needed to process it
    int counter = 0;
    for (auto it = map.begin(); it != map.end(); it++) {
        if (it->second == 1) {
            return -1;
        } else if (it->second % 3 == 0) {
            counter += it->second / 3;
        } else if (it->second % 3 == 1) {
            counter += it->second / 3 + 1;
        } else if (it->second % 3 == 2) {
            counter += it->second / 3 + 1;
        }
    }
    return counter;
}