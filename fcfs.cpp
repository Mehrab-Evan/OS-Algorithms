#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

struct Process
{
    int arrival_time;
    int burst_time;
};

int main() {

    Process P[5];
    for(int i=0; i<5; i++) {
        scanf("%d%d",&P[i].arrival_time, &P[i].burst_time);
    }
    
    for(int i=0; i<5; i++) {
        for(int j=i+1; j<5; j++) {
            if(P[i].arrival_time > P[j].arrival_time) {
                swap(P[i],P[j]);
            }
        }
    }
    
    for(int i=0; i<5; i++) {
        cout << P[i].arrival_time << " " << P[i].burst_time << endl;
    }
    
    int sum = 0;
    int ct[5];
    for(int i=0; i<5; i++) {
      if(sum < P[i].arrival_time) {
          sum += (P[i].arrival_time - sum);
      }
      sum = sum + P[i].burst_time; 
      ct[i] = sum;
    }
    
    cout << endl;
    for(int i=0; i<5; i++) {
        cout << 'p' << i << " " << P[i].arrival_time << " " << P[i].burst_time << " " << ct[i] << endl;
    }
    // cout << sum << endl;

    return 0;
/*
0 2
4 3
3 5
10 2
5 4
*/
}
