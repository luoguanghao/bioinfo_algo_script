#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
const int maxn = 35;

int Tree[maxn][2];
int pre[maxn];
int post[maxn];
int check[maxn];
bool flag;
int buildTree(int preL,int preR,int postL,int postR){
	int v = pre[preL];
	//printf("%d, %d %d %d %d\n",v,preL,preR,postL,postR);
	if(postR-postL==2){
		Tree[v][0]=post[postL];
		Tree[v][1]=post[postL+1];
	}else if(postR-postL==1){
		flag = false;
		Tree[v][0]=post[postL];
	}else if(postR-postL==0){
		return v;
	}else if(postL>postR){
		flag = false;
		return -1;
	}else{
		int indx;
		for(indx=postL;post[indx]!=pre[preL+1];indx++);
		Tree[v][0]=buildTree(preL+1,preL+1+indx-postL, postL,indx);
		Tree[v][1]=buildTree(preL+2+indx-postL,preR, indx+1, postR-1);
	}
	return v;
}

int cnt=0;
void inTra(int v){
	if(v==-1) return;
	inTra(Tree[v][0]);
	if(cnt) printf(" ");
	printf("%d",v); cnt++;
	inTra(Tree[v][1]);
}

int main(){
	fill(Tree[0],Tree[0]+maxn*2,-1);
	fill(check,check+maxn,0);
	flag = true;
	
	int n; scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&pre[i]);
	}
	for(int i=0;i<n;i++){
		scanf("%d",&post[i]);
	}
	int start = buildTree(0,n-1,0,n-1);
	if(flag) printf("Yes\n");
	else printf("No\n");
	inTra(start);
	printf("\n");
}
/*
8
1 2 4 8 5 6 7 3
8 4 6 7 5 2 3 1


9
1 2 4 8 5 6 7 9 10
8 4 6 9 10 7 5 2 1
*/