#include <iostream>
using namespace std;

int main(){
    int idade;
    cin >> idade;

    if(idade < 16) {
        cout << "Não vota";
    } else if (18 <= idade && idade <= 70) {
        cout << "Voto obrigatório";
    } else {
        cout << "Voto opcional";
    }
    return 0;
}
