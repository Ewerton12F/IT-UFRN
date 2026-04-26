#include <iostream>

using namespace std;

int main(){
    // Lendo a entrada do exercício
    int B, C;
    cin >> B >> C;

    // Seu código vai aqui

    int sum = B + C;

    if (sum % 2 == 0) {
        cout << "Bino";
    } else {
        cout << "Cino";
    }

    return 0;
}
