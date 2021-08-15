#include <iostream>
#include <iomanip>

using namespace std;

int main(){

	float tempo, vmedia, space, gcar = 12, gasto;

	cin >> tempo;
	cin >> vmedia;

	space = vmedia*tempo;

	gasto = space/gcar;

	cout << setprecision(3) << fixed;
	cout << gasto << endl;

	return 0;
}