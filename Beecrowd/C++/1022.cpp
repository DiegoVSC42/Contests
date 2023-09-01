#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{

    string operacao;
    int n1, n2, d1, d2;
    int n3, d3;
    char c1, c2, c3;
    int stop;
    int contagem;
    int cont_space = 0;
    scanf("%d", &contagem);

    for (int i = 0; i < contagem; i++)
    {
        scanf("%d %c %d %c %d %c %d", &n1, &c1, &d1, &c2, &n2, &c3, &d2);

        switch (c2)
        {
        case '+':
            d3 = d1 * d2;
            n3 = (((d3 / d1) * n1) + ((d3 / d2) * n2));
            break;
        case '-':
            d3 = d1 * d2;
            n3 = (((d3 / d1) * n1) - ((d3 / d2) * n2));
            break;
        case '*':
            n3 = n1 * n2;
            d3 = d1 * d2;
            break;
        case '/':
            n3 = n1 * d2;
            d3 = d1 * n2;
            break;
        }

        cout << n3 << "/" << d3 << " = ";

        bool neg = (n3 < 0 || d3 < 0) ? true : false;
        if (neg)
        {
            n3 = abs(n3);
            d3 = abs(d3);
        }

        int j = 2;
        while (j != 1000)
        {
            if (n3 % j == 0 && d3 % j == 0)
            {
                n3 = n3 / j;
                d3 = d3 / j;
                j = 2;
            }
            else
            {

                j++;
            }
        }

        if (neg)
        {
            cout << "-" << n3 << "/" << d3 << endl;
        }
        else
        {
            cout << n3 << "/" << d3 << endl;
        }
    }

    return 0;
}