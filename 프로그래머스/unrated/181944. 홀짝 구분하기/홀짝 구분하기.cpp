#include <iostream>

using namespace std;

int main(void) {
    int n;
    string ans;
    cin >> n;
    if (n % 2 == 1) {
        ans += string("odd");
    } else {
        ans += string("even");
    }
    cout << n << " is "<< ans;
    return 0;
}