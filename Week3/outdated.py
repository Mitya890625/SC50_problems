

data_dict = {'January':1, 'February': 2, 'March':3, 'April':4, 'May':5, 
             'June':6, 'Jule':7,'August':8, 'September':9, 
             'October':10, 'November':11, 'December':12}
data = input().replace(',', '').replace('/',' ').split(' ')
m, d, y = data
if m in data_dict:
    print(d, data_dict[m], y, sep='-')
else:
    print(d, m, y, sep='-')