#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    int flag = 0;
    vector<int> box(1002, 0);
    int maxV = 0;
    for (int i : array){
        box[i] += 1;
        if (i > maxV){
            maxV = i;
        }
    }
    int boxV = 0;
    for (int i; i <= maxV; i++){
        if (boxV < box[i]){
            answer = i;
            boxV = box[i];
            flag = 0;
        } else if (boxV == box[i]){
            flag = -1;
        }
    }
    
    if (flag == -1){
        answer = -1;
    }
    
    return answer;
}