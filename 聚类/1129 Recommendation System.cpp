#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
const int maxn = 50005;

int n,k;
int clickTime[maxn];
int SortLink[maxn];

bool cmp(int a,int b){
	if(clickTime[a]==clickTime[b]){
		return a<b;
	}
	return clickTime[a]>clickTime[b];
}

void Sort(int item){
	int i;
	for(i=1;i<=n&&SortLink[i]!=item;i++);
	int v;
	for(v=i-1;v>=1;v--){
		if(clickTime[SortLink[v]]<clickTime[item]){
			SortLink[v+1] = SortLink[v];
		}else if(clickTime[SortLink[v]]==clickTime[item]&&SortLink[v]>item){
			SortLink[v+1] = SortLink[v];
		}else{
			break;
		}
	}
	SortLink[v+1] = item;
}

int main(int argc, char *argv[]) {
	fill(clickTime,clickTime+maxn,0);
	
	int tmp;
	scanf("%d %d",&n,&k);
	
	scanf("%d",&tmp);
	clickTime[tmp]++;
	for(int i=1;i<=n;i++){
		SortLink[i] = i;
	}
	Sort(tmp);
	//printf("* %d\n",SortLink[1]);
	
	for(int i=1;i<n;i++){

		//sort(SortLink+1, SortLink+n+1, cmp);
		scanf("%d",&tmp);
		printf("%d:",tmp);
		for(int v=1;v<=k&&v<=i;v++){
			printf(" %d",SortLink[v]);
		}
		printf("\n");
		clickTime[tmp]++;
		Sort(tmp);
	}
	
}