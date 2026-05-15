#include <bits/stdc++.h>
using namespace std;

int main() {
    float nota1, nota2, nota3;
    cin >> nota1 >> nota2 >> nota3;
    int media = (nota1 + nota2 + nota3) / 3;
    
    if (nota1 && nota2 && nota3 >= 4 && media >= 6) {
        cout << "Aprovado";
    } else {
        int recuperacao;
        cin >> recuperacao;
        if (nota1 < nota2 && nota1 < nota3) {
            nota1 = recuperacao;
        } else if (nota2 < nota1 && nota2 < nota3) {
            nota2 = recuperacao;
        } else if (nota3 < nota1 && nota3 < nota2) {
            nota3 = recuperacao;
        } 
        if (nota1 && nota2 && nota3 >= 3 && media >= 5) {
            cout << "Aprovado por nota";
        } else {
            cout << "Reprovado";
        }
    }
}