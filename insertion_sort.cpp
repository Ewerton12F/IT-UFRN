#include <iostream>
#include <vector>
using namespace std;

int main(){
    int T1, T2, T3;

    cin >> T1 >> T2 >> T3;
    vector<int> A = {5, 2, 4, 6, 1, 3};
    for (int x : A) cout << x << " ";
    cout << "\n" ;
    
    for (int j = 1; j <= A.size(); j++) {
        int chave = A[j];
        // Inserir A[j] na sequência ordenada A[1..j-1]
        int i = j - 1;
        while (i >= 0 && A[i] > chave) {
            A[i + 1] = A[i];
            i = i - 1;
        }
        A[i + 1] = chave;
    }
    
    for (int x : A) cout << x << " ";
    cout << "\n" ;

    return 0;
}

// #include <iostream>
// #include <vector>
// using namespace std;

// void insertionSort(vector<int>& arr) {
//     int n = arr.size();

//     for (int x : arr) cout << x << " ";
//     cout << "\n";

//     for (int i = 1; i < n; i++) {
//         int key = arr[i];
//         // Inserir A[j] na sequência ordenada A[1..j-1]
//         int j = i - 1;
//         while (j >= 0 && arr[j] > key) {
//             arr[j + 1] = arr[j];
//             j = j - 1;
//         }
//         arr[j + 1] = key;
//     }
// }

// int main(){
//     vector<int> A = {5, 2, 4, 6, 1, 3};
//     insertionSort(A);
    
//     for (int x : A) cout << x << " ";
//     cout << "\n";
    
//     return 0;
// }