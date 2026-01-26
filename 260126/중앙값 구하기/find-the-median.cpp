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
            if(b>c)
            {
                 two = b;
            }
            else
            {
                two = c;
            }
            


            cout << two;

        }
        else
        {
            //c 가 더큼

             if(b>a)
            {
                 two = b;
            }
            else
            {
                two = a;
            }
             cout << two;


        }


    }
    else// b>a
    {
        one = b;
        two = a;

        if(b>c)
        {
            if(a>c)
            {
                 two = a;
            }
            else
            {
                two = c;
            }
            


            cout << two;

        }
        else
        {
            //c 가 더큼

             if(b>a)
            {
                 two = b;
            }
            else
            {
                two = a;
            }
             cout << two;
        }


    }
    

    // Please write your code here.
    return 0;
}