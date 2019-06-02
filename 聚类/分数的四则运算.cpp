#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

struct figureType{
	long up,down;	
};

int gcd(int a,int b){
	if(b==0) return a;
	return gcd(b, a%b);
}

struct figureType normalize(struct figureType f){
	int flag=1;
	if(f.up*f.down<0) flag=-1;
	
	int cf = gcd(abs(f.up), abs(f.down));
	f.up = abs(f.up) / cf;
	f.down = abs(f.down) / cf;
	f.up *= flag;
	return f;
}

void Print(struct figureType f){
	if(f.up*f.down>0){
		if(f.down==1){
			printf("%ld",f.up);
		}else{
			long dai=f.up/f.down;
			if(dai==0){
				printf("%ld/%ld",f.up,f.down);
			}else{
				printf("%ld %ld/%ld",dai,f.up-f.down*dai,f.down);
			}
				
		}
	}else if(f.up*f.down<0){
		if(f.down==1){
			printf("(%ld)",f.up);
		}else{
			long dai=f.up/f.down;
			if(dai==0){
				printf("(%ld/%ld)",(f.up),f.down);
			}else{
				printf("(%ld %ld/%ld)",dai,(-f.up)-f.down*(-dai),f.down);
			}
		}		
	}else if(f.down==0){
		printf("Inf");
	}else{
		printf("0");
	}
}

void add(struct figureType f1,struct figureType f2){
	struct figureType newf;
	newf.up = f1.up*f2.down+f1.down*f2.up;
	newf.down = f1.down*f2.down;
	Print(f1); printf(" + "); Print(f2); printf(" = ");
	Print(normalize(newf));
	printf("\n");
}

void subtract(struct figureType f1,struct figureType f2){
	struct figureType newf;
	newf.up = f1.up*f2.down-f1.down*f2.up;
	newf.down = f1.down*f2.down;
	Print(f1); printf(" - "); Print(f2); printf(" = ");
	Print(normalize(newf));
	printf("\n");
}

void multipu(struct figureType f1,struct figureType f2){
	struct figureType newf;
	newf.up = f1.up*f2.up;
	newf.down = f1.down*f2.down;
	Print(f1); printf(" * "); Print(f2); printf(" = ");
	Print(normalize(newf));
	printf("\n");
}

void divide(struct figureType f1,struct figureType f2){
	struct figureType newf;
	newf.up = f1.up*f2.down;
	newf.down = f1.down*f2.up;
	Print(f1); printf(" / "); Print(f2); printf(" = ");
	Print(normalize(newf));
	//newf = normalize(newf);
	printf("\n");
}

int main(){
	struct figureType f1,f2;
	scanf("%ld/%ld %ld/%ld",&f1.up,&f1.down,&f2.up,&f2.down);
	
	f1 = normalize(f1); f2 = normalize(f2);
	
	add(f1,f2);
	subtract(f1,f2);
	multipu(f1,f2);
	divide(f1,f2);
}