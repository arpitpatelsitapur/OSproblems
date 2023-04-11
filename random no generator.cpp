// program that generates a random roll number between 1 to 70 excluding the detained ones
#include"iostream"
#include"cstdlib"
#include"time.h"
// needed when time() is used in srand ()*/
using namespace std;
int main(){
	int n=70,no;
	srand(time(0 ));   
	//The call to srand() provides a value which varies every time and hence the pseudo-random number varies for every program call.
	//Computer can't sense randomness so PRNG (Pseudo Random Number Generator) generates a sequence of random numbers is used in C++. 
	//This Pseudo-Random Number Generator is capable of sensing randomness in a program. 
	int roll_no;
	cout<<"Enter how many students you want to pick : ";
	cin>>no;
	cout<<"Random Roll_no between 1 to 70 excluding the detained ones : "<<endl;
	for(int i=1;i<=no;i++){
	    do{
		   roll_no=rand()%n;
	       cout<<roll_no<<" ";
        }while(roll_no==35||roll_no==64||roll_no==66||roll_no==0);
    }
	return 0;
}
