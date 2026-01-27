#include <iostream>
using namespace std;

int main() 
{
    string a[10] ;
    //cin >>a;

    for(int index = 0; index < 10; index++)
    {
        cin >> a[index];
    } 

    for(int index = 9; index>=0; index--)
    {
        cout << a[index];
    }

    

    // Please write your code here.
    return 0;
}