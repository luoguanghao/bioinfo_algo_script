#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct EdgeType{
	int nextNode;
	int visited;
};

int main(int argc, char *argv[]) {
	int tmpindx,tmp;
	int countEdge = 0;
	vector<int> output;
	
	vector<EdgeType> Graph[2005];
	int visited[2005] = {0};
	
	while(1){
		scanf("%d",&tmpindx);
		if(tmpindx == -1) break;
		scanf(" -> ");
		while(1){
			EdgeType newE;
			newE.visited = 0;
			scanf("%d",&newE.nextNode); countEdge++;
			Graph[tmpindx].push_back(newE);
			char flag;
			if(getchar()=='\n') break;
		}
	}
	stack<int> s;
	s.push(6);
	
	while(s.size()){
		int top = s.top();
		int i;
		for(i=0;i<Graph[top].size();i++){
			if(Graph[top][i].visited==0){
				s.push(Graph[top][i].nextNode);
				Graph[top][i].visited=1;
				break;
			}
		}
		if(i==Graph[top].size()){
			printf("%d ",s.top());
			s.pop();
		}
	}
	printf("\n");
}
	
	