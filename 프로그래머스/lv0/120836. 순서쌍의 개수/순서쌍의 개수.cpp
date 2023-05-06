#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int i = 1;
    while (i <= n) {
        if (n%i == 0){
            answer += 1;
        }
        i += 1;
    }
    return answer;
}