print('%s : %d' % ('문자열', 30))
print('{} : {}'.format('문자열', 30))
print('%f, %.2f' %(1.123, 1.123))
print('{:f}, {:.2f}'.format(1.123, 1.123))
print('{:5f}'.format(1.123456))
print('%o, %x, %X' % (10,10,10))
print('{:b}, {:o}'.format(10,10))
print('{:x}, {:X}'.format(10,10))
print('|%5d|' % 123)
print('|%5s|' % 'abc')
print('|{:5}|'.format(123))
print('|{:5}|'.format('abc')) 
print('|%-5d|' % 123)
print('|%5s|' % 'abc')
print('|{:<5}|'.format(123))
print('|{:>5}|'.format('abc'))
print('|{:^5}|'.format('abc'))
print('|%05d|' % 123) 
print('|{:05}|'.format(123))
print('|{:_>5}|'.format('abc'))
print('|{:-^5}|'.format('abc'))
print('{:,}'.format(1000000))
print('{:,.2f}'.format(1000000))

print('{:^70}'.format('Python Shop'))
print('{:<5}: {:<65}'.format('No.', 1078718855))
print('{:<5}: {:<65}'.format('Addr', '서울시 종로구 종로3가'))
print('{:<5}: {:<65}'.format('Name', '김사장'))
print('{:<5}: {:<65}'.format('H.P', '070 1234 5678'))
print('{:-<70}'.format('-'))
print('{:>25}{:^15}{:^15}{:^15}'.format('Items', 'Units', 'QTY', 'Price'))
print('{:-<70}'.format('-'))
print('{:>25}{:^15,}{:^15,}{:>15,}'.format('Blue-Tooth', 8500, 1, 85000))
print('{:>25}{:^15,}{:^15,}{:>15,}'.format('USB3.0 8G', 8000, 1, 8000))
print('{:-<70}'.format('-'))
print('{:<10}{:>60,}'.format('Total',93000))
print('{:-<70}'.format('-'))
print('{:<25}{:>45,}'.format('Pay Money',93000))
print('{:<25}{:>45,}'.format('Receive Money',100000))
print('{:<25}{:>45,}'.format('Change Money',7000))
print('{:-<70}'.format('-'))




