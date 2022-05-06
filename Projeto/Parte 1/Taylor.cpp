/*
*********************************************
*    Gustavo Hiroshi Yoshio   - 32033273    *
*    Vitória Karpovas Chisman - 32008554    *
*    Rafael Junqueira Pezeiro - 32035901    *
*********************************************
*/

#include <iostream>
#include <stdio.h>
using namespace std;

double taylor(double result, double T)
{
  double temp;
  for(double i = 1; i < T; i++)
    {
      temp = 1/i;
      result += temp;
    }
  return result;
}

int main()
{
  double T = -1;
  while(T != 0)
    {
      double resultado = 0.00;
      cout << "Para sair, digite 0\n\nEscolha um número para descobrir a Série de Taylor\nNúmero: ";
      cin >> T;
      resultado = taylor(resultado, T);
      cout << "Resultado: " << resultado << endl << endl;
    }
}
