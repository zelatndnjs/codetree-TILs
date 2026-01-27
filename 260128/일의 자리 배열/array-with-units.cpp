#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int a,b;
    cin >>a>>b;

int ar[10];

ar[0] = a;
ar[1] = b;
cout <<ar[0]<<" ";
cout <<ar[1]<<" ";


for(int index = 2; index < 10; index ++)
{
 ar[index] =  ar[index-2] + ar[index-1] ;
 cout << ar[index] % 10<<" ";
}


    return 0;
}