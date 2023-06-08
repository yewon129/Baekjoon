#include <string>
#include <vector>

using namespace std;

int solution(string num_str) {
    int answer = 0;
    for (char i: num_str){
        int box = i - '0';
        answer += box ;
    }
    return answer;
}