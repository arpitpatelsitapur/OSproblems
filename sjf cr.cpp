// sjf cr
#include<iostream>
#include"iomanip"
using namespace std;
int main(){
	int n=4;
	int pid[n]={1,2,3,4};
	int bt[n]={8,4,9,5};
	int tat[n],wt[n];
	int index,temp1,temp2,min;
	for(int i=0;i<n;i++){
		index=i;
		min=bt[i];
	    for(int j=i+1;j<n;j++){
	       if(min>bt[j]){
	   	    index=j;
	   	    min=bt[j];
	       }
        }
        temp1=bt[i];          temp2=pid[i];
        bt[i]=bt[index];      pid[i]=pid[index];
        bt[index]=temp1;      pid[index]=temp2;
	}
	wt[0]=0;
	for(int i=1;i<n;i++){
		wt[i]=bt[i-1]+wt[i-1];
	}
	for(int i=0;i<n;i++){
	    tat[i]=bt[i]+wt[i];
	}
    int total_wt=0,total_tat=0;
    cout<<"Process ID\tBurst Time\tWaiting Time\tTurnaround Time\n";
    for(int i= 0;i<n;i++){
        total_wt+=wt[i];
        total_tat+=tat[i];
        cout<<pid[i]<<"\t\t"<<bt[i]<<"\t\t"<<wt[i]<<"\t\t"<<tat[i]<<"\n";
    }
    cout<<endl<<"Average Waiting Time = " <<(float)total_wt /(float)n<<endl;
    cout<<"Average Turnaround Time = " <<(float)total_tat /(float)n<<endl;
	return 0;
}
