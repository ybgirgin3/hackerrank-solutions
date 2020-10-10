
#include <iostream>
#include <cstdio>
using namespace std;
using std::cin;
using std::cout;
using std::endl;
using std::fixed;


int main() {
  // variables
  int a;
  long b;
  char c;
  float d;
  double e;

  // getting inputs
  cin >> a >> b >> c >> d >> e;
  cout << a << endl;
  cout << b << endl;
  cout << c << endl;

  cout.precision(3);
  cout << fixed << d << endl;

  cout.precision(3);
  cout << fixed << e << endl;

  return 0;
}
