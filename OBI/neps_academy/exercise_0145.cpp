#include <iostream>

using namespace std;

int main(){
    // Lendo a entrada do exercício
    int X;
    cin >> X;

    // Seu código vai aqui
    if(X <= 1000) {
        if(X == 0) {
            cout << "nulo";
        } else if (X < 0) {
            cout << "negativo";
        } else if (X > 0) {
            cout << "positivo";
        }
    }

    return 0;
}
