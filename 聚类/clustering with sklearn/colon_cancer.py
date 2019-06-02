from os.path import dirname
from sklearn import datasets, svm

def Input():
	# 训练集
	X = []
	Y = []
	# 验证集
	check_x=[]
	check_y=[]
	
	# 导入患癌标本
	dataset1 = open(dirname(__file__)+'colon_cancer.txt').read().strip().split('\n')
	dataset1=[list(map(float,line.split()))[:20] for line in dataset1]
	# 患癌标本前10个（25%）作为验证集，剩下的作为训练集
	X += dataset1[10:]
	check_x += dataset1[:10]
	Y += [1]*(len(dataset1)-10)
	check_y += [1]*10
	
	# 导入不患癌标本
	dataset2 = open(dirname(__file__)+'colon_healthy.txt').read().strip().split('\n')
	dataset2=[list(map(float,line.split()))[:20] for line in dataset2]
	# 不患癌标本前5个（25%）作为验证集，剩下的作为训练集
	X += dataset2[5:]
	check_x += dataset2[:5]
	Y += [0]*(len(dataset2)-5)
	check_y += [0]*5
	
	# 导入待测试标本
	dataset3 = open(dirname(__file__)+'colon_test.txt').read().strip().split('\n')
	test_X = [list(map(float,line.split()))[:20] for line in dataset3]
	
	return [X ,Y , test_X , check_x , check_y]

if __name__ == '__main__':
	
	[X_train ,y_train , test_X,check_x, check_y] = Input() # 我把输入数据这一个操作写到一个Input函数里了
	
	kernel = 'linear' # 参数选择：选择线性核函数
	
	# 固定操作
	clf = svm.SVC(kernel=kernel, gamma=10)
	clf.fit(X_train,y_train) # 输入训练集数据	
	
	print(clf.predict(test_X)) # 输入待测试数据，输出结果，结果是0，代表阴性。结果是在一个[]中的，这是因为可以同时输入一组待测数据，然后以list的格式输出一组数据的结果

	# 怎么知道机器通过学习，画出的分类平面是否准确呢。我们将验证集的数据代入，将机器分类结果和已知的结果比较，计算正确率
	predict_for_ckeck = clf.predict(check_x)
	cnt=0
	for i in range(len(check_y)):
		if check_y[i]==predict_for_ckeck[i]:
			cnt+=1
	print('Accuracy %.2f%%'%(cnt/len(check_y)*100))
	
	