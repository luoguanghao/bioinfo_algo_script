#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct nodetype{
	int v;
	struct nodetype *l, *r;
};
int n;
int layerList[1001];

struct nodetype* Insert(struct nodetype* T ,int item){
	if(T==NULL){
		T = (struct nodetype*)malloc(sizeof(struct nodetype));
		T->l = T->r = NULL;
		T->v = item;
		return T;
	}
	if(item<T->v){
		T->l = Insert(T->l, item);
	}else{
		T->r = Insert(T->r, item);
	}
	return T;
}

int BFS(struct nodetype* T){
	queue<struct nodetype*> q;
	q.push(T);
	struct nodetype *last = T, *tmplast;
	int level = 0;
	int cnt=0;
	while(q.size()){
		struct nodetype *top = q.front();
		q.pop();
		cnt++;
		if(top->l!=NULL){
			q.push(top->l);
			tmplast = top->l;
		}
		if(top->r!=NULL){
			q.push(top->r);
			tmplast = top->r;
		}
		if(top==last){
			layerList[level] = cnt; cnt=0;
			last = tmplast;
			if(q.size()) level++;
		}
	}
	return level;
}

int main(int argc, char *argv[]) {
	scanf("%d",&n);
	int tmp;
	struct nodetype* Tree = NULL;
	for(int i=0;i<n;i++){
		scanf("%d",&tmp);
		Tree = Insert(Tree,tmp);
	}
	
	int level = BFS(Tree);
	
	printf("%d + %d = %d\n",layerList[level],layerList[level-1],layerList[level]+layerList[level-1]);
}