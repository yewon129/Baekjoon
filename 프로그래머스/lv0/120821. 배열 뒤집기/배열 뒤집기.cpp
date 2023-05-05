#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    for (int i: num_list){
        answer.insert(answer.begin(), i);
    }
    return answer;
}