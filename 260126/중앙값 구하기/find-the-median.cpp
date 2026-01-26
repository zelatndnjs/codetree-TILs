#include <iostream>
using namespace std;

int main() {

    int a,b,c;

    int one;
    int two;
    int three;


    cin>>a>>b>>c;

    if(a>b)
    {
        one = b;
        two = a;

        if(a>c)
        {
            two = c;
            three = a;

            cout << two;

        }
        else{
             two = a;
            three = c;

            cout << two;

        }


    }
    else{
         one = a;
         two = b;

        if(b>c)
        {
            two = c;
            three = b;

            cout << two;


        }
        else{
             two = b;
             three = c;
             
             cout << two;

        }

    }
    

    // Please write your code here.
    return 0;
}