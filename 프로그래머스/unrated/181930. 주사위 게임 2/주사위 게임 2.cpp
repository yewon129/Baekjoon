#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int a, int b, int c) {
    int answer = 0;
    if (a != b and a != c and b != c){
        answer = a + b + c;
    } else if (a == b and b == c) {
        answer = (a+b+c) * (pow(a, 2) + pow(b,2) + pow(c,2)) * (pow(a,3) + pow(b,3) + pow(c, 3));
    } else {
        answer = (a+b+c) * (pow(a, 2) + pow(b,2) + pow(c,2));
    }
    return answer;
}