#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int minV = arr[0];
    if (arr.size() == 1){
        answer.push_back(-1);
    }
    else {
     for (int i; i < arr.size(); i++){
         if (arr[i] < minV){
             minV = arr[i];
         }
     }
        
    for (int i; i< arr.size(); i++){
        if (arr[i] != minV){
            answer.push_back(arr[i]);
        }
    }
    }
    return answer;
}