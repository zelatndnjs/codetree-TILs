#include <iostream>
using namespace std;

int main() {

    string a;
    string b;

     cin >>a;
     cin >>b;

     int c = a.length() ;
     int d = b.length() ; 


    if(c> d )
    {
        cout << a<<" "<<c; 

    }
    else if(c< d)
    {
        cout << b<<" "<<d;
    }
    else
    {
        cout << "same";
    }

    // Please write your code here.
    return 0;
}