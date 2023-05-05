#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string overwrite_string, int s) {
    string answer = "";
    int st = overwrite_string.length() + s;
    int n = my_string.length();
    for (int i=0; i < s; i++) {
        answer += my_string[i];
    }
    for (char c : overwrite_string){
        answer += c;
    }
    for (int i = st; i < n; i++){
        answer += my_string[i];
    }
    return answer;
}