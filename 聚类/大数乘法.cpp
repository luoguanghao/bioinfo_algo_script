#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int weishu=0;

string product(string a,string b,int l){
	string ans;
	ans.resize(31);
	for(int i=0;i<31;i++){
		ans[i] = '0';
	}
	cout <<ans <<endl;
	int up = 0, add=0;
	for(int i=l-1;i>=0;i--){
		printf("i=%d\n",i);
		int n1 = a[i]-'0';
		int j;
		for(j=l-1;j>=0;j--){
			printf("j=%d\n",j);
			int n2 = b[j]-'0';
			add = ans[l-i-1+l-j-1]-'0'+n1*n2+up;
			printf("* %d %d add=%d\n",n1,n2,n1*n2+up);
			ans[l-i-1+l-j-1] = (add%10+'0');
			up = add/10;
			printf("up=%d\n",up);
		}
		ans[l-i-1+l-j-1] = up+'0';
		cout << ans<<endl;
		up=0;
	}
	return ans;
}

int main(int argc, char *argv[]) {
	string a = "167";
	string b = "338";
	int l = 3;
	string ans = product(a, b, l);
	cout << ans;
}