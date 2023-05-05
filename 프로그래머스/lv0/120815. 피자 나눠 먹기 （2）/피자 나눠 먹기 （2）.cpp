#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;
    int a = 1;
    while (true) {
        if (n*a == 6*answer){
            break;
        }
        if (n*a > 6*answer){
            answer += 1;
        } else if (n*a < 6*answer){
            a += 1;
        }
    }
    return answer;
}