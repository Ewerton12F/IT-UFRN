#include <iostream>

using namespace std;

int main(){
    // Seu código vai aqui
    int M, A, B, C, maior;
    cin >> M >> A >> B;
	C = M - (A + B);
	
	if ((40<=M<=100) && (1<=A<=M) && (1<=B<=M) && (A!=B)) {
		maior = A;
		if (B > maior) {
			maior = B;
		}
		if (C > maior) {
			maior = C;
		}
		
		cout << maior;
	}

    return 0;
}
