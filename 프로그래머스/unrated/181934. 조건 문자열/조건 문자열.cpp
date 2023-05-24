#include <string>
#include <vector>

using namespace std;

int solution(string ineq, string eq, int n, int m) {
    int answer = 0;
    if (eq.compare("=") == 0){
        if (ineq.compare(">") == 0){
            if (n >= m){
                return 1;
            } else {
                return 0;
            }
        } else {
            if (n <= m){
                return 1;
            } else {
                return 0;
            }
        }
    } else {
        if (ineq.compare(">") == 0){
            if ( n > m ){
                return 1;
            } else {
                return 0;
            }
        } else {
            if (n < m){
                return 1;
            } else {
                return 0;
            }
        }
    }
    return answer;
}