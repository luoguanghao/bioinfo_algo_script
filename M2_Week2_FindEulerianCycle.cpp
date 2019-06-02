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
	//printf("%d",countEdge);
	int cnt = 0;
	int start = 0;
	while(1){
		stack<int> s;
		s.push(start);
		while(1){
			tmp = s.top();
			printf("%d ",tmp);
			int i;
			for(i=0;i<Graph[tmp].size();i++){
				if(Graph[tmp][i].visited==0){
					s.push(Graph[tmp][i].nextNode);
					Graph[tmp][i].visited = 1;
					cnt++;
					break;
				}
			}
			if(i==Graph[tmp].size()){
				printf("\n");
				break; //一圈走完
			}
		}
		
		if(cnt<countEdge){
			for(int i=0;i<2005;i++){ //找出有未走路径的点
				int j;
				for(j=0;j<Graph[i].size();j++){
					if(Graph[i][j].visited==0){
						start = i;
						break;
					}
				}
				if(j<Graph[i].size()) break;
			}
			for(int i=0;i<2005;i++){ //visited全部设0
				int j;
				for(j=0;j<Graph[i].size();j++){
					Graph[i][j].visited=0;
				}
			}
			cnt=0;
		
		}else{
			while(s.size()){
				output.push_back(s.top());
				s.pop();
			}
			break;
		}
	}
	
	for(int i=output.size()-1;i>=0;i--){
		printf("%d ",output[i]);
	}
	
	return 0;
}