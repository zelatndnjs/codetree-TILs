#include <iostream>
using namespace std;

int main() 
{
    int a;
    int b;

    cin>>a;
    cin>>b;
    
    bool state ;

    if(a>=b)
    {
        state = true;
        cout << state<<endl;
    }
    else
    {
        state = false;
        cout << state<<endl;
    }

     if(a>b)
    {
        state = true;
        cout << state<<endl;
    }
    else
    {
        state = false;
        cout << state<<endl;
    }

    if(a<=b)
    {
        state = true;
        cout << state<<endl;
    }
    else
    {
        state = false;
        cout << state<<endl;
    }

      if(a<b)
    {
        state = true;
        cout << state<<endl;
    }
    else
    {
        state = false;
        cout << state<<endl;
    }

    if(a==b)
    {
        state = true;
        cout << state<<endl;
    }
    else
    {
        state = false;
        cout << state<<endl;
    }
  if(a!=b)
    {
        state = true;
        cout << state<<endl;
    }
    else
    {
        state = false;
        cout << state<<endl;
    }


    
    // Please write your code here.
    return 0;
}