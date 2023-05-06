#include <string>
#include <vector>

using namespace std;

int solution(int a, int b, int n) {
    int answer = 0;
    while (n >= a ){
        int newV = (n / a) * b;
        answer += newV;
        int box = n % a;
        n = newV + box;
    }
    return answer;
}