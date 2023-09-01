#include <iostream>

using namespace std;

int main(){

    long int a, b, c;
    while(cin >> a >> b){

        c = a ^ b ;
        cout << c << endl;
    }

    return 0;
}
/*
9 + 6
1001
0110
1111
8421
15

4 + 6

0100
0110
0010
0020
2
*/