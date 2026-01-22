#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int a,n;

    cin>>a>>n;

   
    for(int index =0; index <n; index++)
    {
        a+=n;
        cout << a<<endl;
    }

    return 0;
}