#include <iostream>
#include <cstdio>
using namespace std;

int main() {
  //define integers
  int a,b;

  // define string list
  string c[] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

  // get integers
  cin >> a;
  cin >> b;

  for (int i = a; i <= b; i++) {
    cout << ((i <= 9)?c[i]:((i % 2 == 0) ? "even":"odd")) << endl;
  }
}
