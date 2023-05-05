#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> lines) {
    int answer = 0;
    sort(lines.begin(), lines.end());
    vector<int> line(202, 0);
    for (int i=0; i<3; i++){
        int st = lines[i][0];
        int end = lines[i][1];
        for (int j=lines[i][0]; j<lines[i][1]; j++){
            line[j+100] += 1;
        }
    }
    
    for (int i=0; i < 202; i++){
        if (line[i] > 1){
            answer += 1;
        }
    }
    return answer;
}