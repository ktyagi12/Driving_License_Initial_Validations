# Driving License Application Form
print '*' * 150
print '\t\t\tSaarthi Driving License Application'
print '\t\t', '*' * 150
vision_thres = 6

fname = raw_input('Enter your first name: ')
lname = raw_input('Enter your last name: ')
year_birth = input('Enter your year of birth: ')
vision = input('Enter your eyesight (eg. 6): ')
city = raw_input('Enter your city name: ').upper()

if (fname == ''or year_birth == '' or vision=='' or city =='' or vision <0):
	print ' Either of the fields is not filled.'
else:
	if (city != 'PUNE' or vision != 6):
		print 'Sorry!! Either you are applying region other than Pune or your vision is not appropriate...'
	else:
		if (year_birth <=2000):
			print'Congratulations!! You can proceed for the license application...'
		else:
			print'Sorry!! You are not eligible for the license application...'

