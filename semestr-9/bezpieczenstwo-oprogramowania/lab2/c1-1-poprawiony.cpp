#include <iostream>

using namespace std;

int main(){
	long abc[40];
	long def[10];

	for(int i=0;i<30;i++) abc[i]=i;
	abc[0]++;
	cout << sizeof(long) << sizeof(int) << sizeof(long long) << endl;	
}
