#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    for (char c : str) {
        if (c >= 'a' && c <= 'z'){
            cout << char(toupper(c));
        } else if (c >= 'A' && c <= 'Z'){
            cout << char(tolower(c));
        }
    }
    return 0;
}