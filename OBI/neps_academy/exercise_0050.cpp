#include <iostream>

using namespace std;

int main(){
    // Seu código vai aqui
    int A, B, C, D;

    cin >> A >> B >> C >> D;

    if (1 <= A <= 1000 && 1 <= B <= 1000 && 1 <= C <= 1000 && 1 <= D <= 1000) {
        if (A == B + C + D && B + C == D && B == C) {
            cout << "S";
        } else {
        cout << "N";
        } 
    }

    return 0;
}
