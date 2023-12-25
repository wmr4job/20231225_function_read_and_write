# function_read & write file
import os # 載入作業系統

# 讀取檔案
def read_file(filename):
	products = []
	if os.path.isfile(filename): # 檢查檔案是否存在
		with open(filename, 'r', encoding = 'utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue # 繼續，跳過這一次的迴圈
				name, price = line.strip().split(',')
				products.append([name, price])
		print(products)
	else:
		print('找不到檔案！')
	return products # 回傳清單內容

# 輸入商品,價格清單
def user_input(products): # 因為需要將新增的商品存入清單，要設定一個參數提供清單的名稱
	while True:
		name = input('請輸入商品名稱(輸入q離開)：')
		if name == 'q': # 輸入q離開(quit)
			break
		price = input('請輸入商品價格：')
		products.append([name, price]) # 存每個品項+價格
	return products # 回傳清單內容

# 印出商品價格
def print_products():
	for item in products:
		print(item[0], '的價格是', item[1])

# 寫入檔案
def write_file(filename, products): # 傳入檔名、要讀取的清單名稱
	with open(filename, 'w', encoding = 'utf-8') as f: # 打開檔案，並使用UTF-8的編碼
		f.write('商品,價格\n') # 增加標題列
		for item in products:
			f.write(item[0] + ',' + item[1] + '\n') # f.write將內容寫入，加上','是為了分隔內容


products = read_file('products.csv') # 將清單內容存到products
products = user_input(products) # 將使用者新增的內容存到products清單，再將回傳結果更新清單
print_products()
write_file('products.csv', products) # 將資料寫回該檔案