/*
Distances Between Leaves Problem: Compute the distances between leaves in a weighted tree.
     Input:  An integer n followed by the adjacency list of a weighted tree with n leaves.
     Output: An n x n matrix (di,j), where di,j is the length of the path between leaves i and j.

Code Challenge: Solve the Distances Between Leaves Problem. The tree is given as an adjacency list of a graph whose leaves are integers between 0 and n - 1; the notation a->b:c means that node a is connected to node b by an edge of weight c. The matrix you return should be space-separated.
----------
Sample Input:
4
0->4:11
1->4:2
2->5:6
3->5:7
4->0:11
4->1:2
4->5:4
5->4:4
5->3:7
5->2:6
-------------
Sample Output:
0	13	21	22
13	0	12	13
21	12	0	13
22	13	13	0
-------------
Lo Kwongho 2018.9
*/

#include <iostream>
#include <vector>
using namespace std;
const int INF = 999999;
const int maxn = 70;
int main(int argc, char *argv[]) {
	int n;
	int Graph[maxn][maxn];
	for(int i=0;i<maxn;i++){
		for(int j=0;j<maxn;j++){	
			if(i==j)
				Graph[i][j]=0;
			else
				Graph[i][j]=INF;
		}
	}
	int v1,v2,tmpw;
	scanf("%d",&n);
	int outDegree[maxn] = {0};
	while(1){
		scanf("%d",&v1);
		if(v1==-1)
			break;
		outDegree[v1]++;
		scanf("->%d:%d",&v2,&tmpw);
		Graph[v1][v2]=tmpw;
	}
	vector<int> leave;
	for(int i=0;i<maxn;i++){
		if(outDegree[i]==1){
			leave.push_back(i);
			//printf("%d ",i);
		}
	}
	printf("%d\n",leave.size());
	/*
	for(int i=0;i<6;i++){
		for(int j=0;j<6;j++){
			printf("%3d",Graph[i][j]);
		}
		printf("\n");
	}
	*/
	
	for(int v=0;v<maxn;v++){
		for(int i=0;i<maxn;i++){
			for(int j=0;j<maxn;j++){
				if(Graph[i][v]<INF&&Graph[v][j]<INF&&Graph[i][j]>Graph[i][v]+Graph[v][j]){
					Graph[i][j]=Graph[i][v]+Graph[v][j];
				}
			}
		}
	}
	
	for(int i=0;i<leave.size();i++){
		for(int j=0;j<leave.size();j++){
			printf("%d",Graph[i][j]);
			if(j!=leave.size()-1)
				printf(" ");
		}
		printf("\n");
	}
	
	
}