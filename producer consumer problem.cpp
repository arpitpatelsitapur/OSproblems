//implement producer consumer problem for buffer size of n
#include"iostream"
using namespace std;
void up(int &x){
	x++;
}
void down(int &x){
	if(x>0){
	  x--;
    }
}
int main(){
	int n=5;
	int buffr[n];
	int empty=n;
	int full=0;
	//int mutex=1;
	while(1){
		cout<<"---------------------------------------------"<<endl;
		cout<<"Empty "<<empty<<" Full "<<full/*<<" Mutex "<<mutex*/<<endl;
		int x;
		cout<<"Enter your choice :"<<endl<<"1. Produce"<<endl<<"2. Consume"<<endl;
		cin>>x;
		if(x==1){
			// producer
			if(empty!=0 /*&& mutex==1*/){
				cout<<"Enter the data : ";
				cin>>buffr[full];
				down(empty);
				//down(mutex);
				//up(mutex);
				up(full);
			}
			else 
			   cout<<"Buffer is full. Consume the Data first."<<endl;
		}
		else if(x==2){
			//consumer
			if(full>0 /*&&mutex==1*/ ){
				down(full);
				//down(mutex);
				cout<<"The data is "<<buffr[full]<<endl;
				//up(mutex);
				up(empty);
			}
			else
			   cout<<"Buffer is empty. Produce the data first."<<endl;
		}
		else 
		   break;
	}
	return 0;
}
