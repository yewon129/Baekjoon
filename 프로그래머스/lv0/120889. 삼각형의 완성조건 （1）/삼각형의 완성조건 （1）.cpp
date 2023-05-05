#include <string>
#include <vector>

using namespace std;

int solution(vector<int> sides) {
    int answer = 0;
    int maxV = max(sides[0], sides[1]);
    maxV = max(maxV, sides[2]);
    int sumV = sides[0] + sides[1] + sides[2] - maxV;
    if (maxV >= sumV){
        answer = 2;
    } else {
        answer = 1;
    }
    return answer;
}