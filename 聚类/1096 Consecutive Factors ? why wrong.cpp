#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

int n;
queue<int> path,tmpp;
int value = 1;

int main(){
	scanf("%d",&n);
	for(int i=2;i<=n;i++){
		value*=i;
		tmpp.push(i);
		//printf("  %d i=%d\n",value,i);
		while(value>n){
			value /= tmpp.front();
			//printf("-- %d %d\n",tmpp.front(),value);
			tmpp.pop();
		}
		if(n%value==0){
			if(tmpp.size()>path.size()){
				path=tmpp;
			}
		}
	}
	printf("%lu\n",path.size());
	while(1){
		cout<<path.front();
		path.pop();
		if(path.size()) cout<<"*";
		else break;
	}
}