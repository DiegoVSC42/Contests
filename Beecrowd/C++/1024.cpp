#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string palavra;
    int valor_ascii, casos;
    char letra;

    cin >> casos;
    cin.ignore();
    
    for (int i = 0; i < casos; i++)
    {   
        cin.ignore();
        getline(cin,palavra);
        for (int i = 0; i < palavra.size(); i++)
        {
            letra = palavra[i];
            valor_ascii = letra;
            if ((valor_ascii >= 65 && valor_ascii <= 90) || (valor_ascii >= 97 && valor_ascii <= 122))
            {
                valor_ascii += 3;
                letra = valor_ascii;
                palavra[i] = letra;
            }
        }
        reverse(palavra.begin(), palavra.end());

        for (int i = palavra.size() / 2; i < palavra.size(); i++)
        {
            letra = palavra[i];
            valor_ascii = letra;
            valor_ascii -= 1;
            letra = valor_ascii;
            palavra[i] = letra;
        }

        cout << palavra << endl;
    }
    return 0;
}