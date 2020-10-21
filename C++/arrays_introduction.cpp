#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int a[MAX], N,i;
  cin >> N;

  for(i = 1; i <= N; i++) {
      cin >> a[i];
  }

  for(i = 0; i < N; i++) {
      cout << a[N-i] << " ";
  } 



  /*
  // define integers
  int N;
  int input;
  vector<int> vector;

  // get integers n times and add them to vector
  for (int i = 0; i < N+1; i++) {
    vector.push_back(input);
  }
  // print vector
  for (vector<int>::const_iterator i = vector.begin(); i != path.end(); ++i) {
    cout << *i << ' ';
  }
  */
  return 0;
}

