// TODO: Not working (podium vector iteration)
#include <iostream>
#include <vector>
using namespace std;

int main(){
    // Seu código vai aqui
    int T1, T2, T3;

    vector<int> original = {5, 2, 4, 6, 1, 3};
    vector<int> sorted = {5, 2, 4, 6, 1, 3};
    vector<int> podium[6];

    for (int j = 1; j <= sorted.size(); j++) {
        int chave = sorted[j];
        // Inserir A[j] na sequência ordenada A[1..j-1]
        int i = j - 1;
        while (i >= 0 && sorted[i] > chave) {
            sorted[i + 1] = sorted[i];
            i = i - 1;
        }
        sorted[i + 1] = chave;
    }
    
    for (int x; x <= sorted.size(); x++) {
        for (int y; y <= original.size(); y++) {
            if (sorted[x] == original[y]) {
                int c = 0;
                podium[c].push_back(y);
                c = c + 1;
            }
        }
    }

    for (int x : sorted) cout << x << " ";
    cout << "\n";
    for (int x : original) cout << x << " ";
    cout << "\n";
    for (int x : podium[0]) cout << x << " ";
    cout << "\n";
    
    return 0;
}
