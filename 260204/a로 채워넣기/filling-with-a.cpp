#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    string a;
    cin >>a;

   
    
    int n = a.length();

     a[1] = 'a';
    a[n-2] = 'a';

    cout << a;

    return 0;
}