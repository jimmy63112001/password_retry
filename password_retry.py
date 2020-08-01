#advanced version for password-retry
password = 'green608360'
i = 3
while i > 0:
	pwd = input('type your password: ')
	if pwd == password:
		print('log in successfully!')
		break
	else:
		i = i-1
		print('fail! you still have', i ,'times remaining')