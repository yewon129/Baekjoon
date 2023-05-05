#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    string box1 = "";
    string box2 = "";
    box1 += to_string(a);
    box2 += to_string(b);
    box1 += to_string(b);
    box2 += to_string(a);
    int ans1 = stoi(box1);
    int ans2 = stoi(box2);
    if (ans1 > ans2){
        answer = ans1;
    } else {
        answer = ans2;
    }
    
    return answer;
}