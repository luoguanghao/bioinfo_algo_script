#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
using namespace std;
const int maxn = 1005;

struct mouseType{
	int weight,order;
	int rank;
};
mouseType mouseList[maxn];

bool cmp(mouseType* a,mouseType* b){
	return a->order<b->order;
}
bool cmp2(mouseType* a,mouseType* b){
	return a->weight>b->weight;
}

int main(){
	int np,ng;
	scanf("%d %d",&np,&ng);
	
	for(int i=0;i<np;i++){
		cin>>mouseList[i].weight;
	}
	for(int i=0;i<np;i++){
		cin>>mouseList[i].order;
	}
	
	vector<mouseType*> layer[maxn];
	int lv=0;
	for(int i=0;i<np;i++){
		layer[lv].push_back(mouseList+i);
	}
	sort(layer[lv].begin(), layer[lv].end(), cmp);
	
	lv++;
	while(1){
		for(int i=0;i<layer[lv-1].size();i+=ng){
			sort(layer[lv-1].begin()+i, min(layer[lv-1].end(),layer[lv-1].begin()+i+ng), cmp2);
			layer[lv].push_back(layer[lv-1][i]);
			printf("%d ",layer[lv-1][i]->weight);
			for(int j=1;j<ng&&j+i<layer[lv-1].size();j++){
				layer[lv-1][i+j]->rank = (layer[lv-1].size()/ng+1+1);
				printf("%d ",layer[lv-1][i+j]->weight);
			}
			printf("\n");
		}
		printf("\n");
		
		if(layer[lv].size()==1){
			layer[lv][0]->rank=1;
			break;
		}
		lv++;
	}
	sort(layer[0].begin(), layer[0].end(), cmp);
	
	for(int i=0;i<np;i++){
		printf("%d ",mouseList[i].rank);
	}
}