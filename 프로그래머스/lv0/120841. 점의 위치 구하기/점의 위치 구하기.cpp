#include <string>
#include <vector>

using namespace std;

int solution(vector<int> dot) {
    int answer = 0;
    int a = dot[0];
    int b = dot[1];
    if (a < 0){
        if (b < 0){
            answer = 3;
        } else {
            answer = 2;
        }
    } else {
        if (b > 0) {
            answer = 1;
        } else {
            answer = 4;
        }
    }
    return answer;
}