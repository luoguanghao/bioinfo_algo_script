#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
const int maxn = 100005;

map<int,int> check;
int Link[maxn];
int Next[maxn];

int main(){
	
	int start,n; cin>>start>>n;
	int add,v,nex;
	for(int i=0;i<n;i++){
		scanf("%d %d %d",&add,&v,&nex);
		Link[add]=v;
		Next[add]=nex;
	}
	
	int newlink=start;
	int delink=-1,delStart=-1;
	int ptr=Next[start];
	while(ptr!=-1){
		if(!check[abs(Link[ptr])]){
			Next[newlink] = ptr;
			newlink = ptr;
			check[abs(Link[ptr])] = 1;
		}else{
			if(delStart==-1){
				delStart=ptr;
			}else{
				Next[delink]=ptr;
			}
			delink = ptr;
		}
		ptr = Next[ptr];
	}
	Next[delink]=-1;
	Next[newlink]=-1;
	ptr=start;
	while(1){
		if(Next[ptr]==-1){
			printf("%05d %d -1\n",ptr,Link[ptr]);
			break;
		}
		printf("%05d %d %05d\n",ptr,Link[ptr],Next[ptr]);
		ptr = Next[ptr];
	}
	ptr = delStart;
	while(1){
		if(Next[ptr]==-1){
			printf("%05d %d -1\n",ptr,Link[ptr]);
			break;
		}
		printf("%05d %d %05d\n",ptr,Link[ptr],Next[ptr]);
		ptr = Next[ptr];
	}
}