#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> numbers) {
    sort(numbers.begin(), numbers.end());
    int idx = numbers.size();
    int answer = numbers[idx-1] * numbers[idx-2];
    return answer;
}