// implementation of FCFS scheduling(non-preemptive)
#include"iostream"
#include<iomanip>
using namespace std;
int main(){
	int n=4;
	int bt[n]={5,10,3,6},at[n]={0,1,2,3};
	int ct[n],tat[n],wt[n],rt[n];
    int temp=0;
	int x=0,sum=bt[0];
	for(int i=0;i<n;i++){
	    if(sum>10){// do nothing
		}
	    else if(sum<10){
		    x++;
			sum+=bt[i+1];
	    }
	    else{
            x++;
			break;		   
	    }
    }
    for(int i=0;i<n;i++){
    	ct[i]=temp+bt[i];
    	temp=ct[i];
	}
	int sum1=0;
	for(int i=0;i<n;i++){
		tat[i]=ct[i]-at[i];
		sum1+=tat[i];
	}
	int sum2=0;
	rt[0]=0;
	for(int i=1;i<n;i++){
		rt[i]=ct[i-1];
		sum2+=rt[i];
	}
	int sum3=0;
	wt[0]=0;
	for(int i=1;i<n;i++){
		wt[i]=tat[i]-bt[i];
		sum3+=wt[i];
	}
	cout<<"Process\tArrival_time\tBurst_time\tTurnaround_time\tWaiting_time\tResponse_time"<<endl;
	for(int i=0;i<n;i++){
		cout<<"P"<<i+1<<"\t\t"<<at[i]<<"\t\t"<<bt[i]<<"\t\t"<<tat[i]<<"\t\t"<<wt[i]<<"\t\t"<<rt[i]<<endl;
	}
	cout<<endl;
	cout<<setw(35)<<"The throughput of CPU : "<<x<<endl;
	cout<<setw(35)<<"Average turn around time : "<<sum1/(float)n<<endl;
	cout<<setw(35)<<"Average response time : "<<sum2/(float)n<<endl;
	cout<<setw(35)<<"Average waiting time is : "<<sum3/(float)n<<endl;
	return 0;
}