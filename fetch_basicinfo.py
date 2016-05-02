import codecs
import os

for root, dirs, files in os.walk('2015/'):
	id = 1
	for filename in files:
		with open('2015/'+filename, 'rb') as f:
			string = f.read()
			string = codecs.decode(string, 'gbk')
			student_id = string.split('\n')[32].split('&nbsp;')[1].split('</td>')[0]
			student_name = string.split('\n')[36].split('&nbsp;')[1].split('</td>')[0]
			student_sex = string.split('\n')[40].split('&nbsp;')[1].split('</td>')[0]
			student_ist = string.split('\n')[48].split('&nbsp;')[1].split('</td>')[0]
			student_major = string.split('\n')[52].split('&nbsp;')[1].split('</td>')[0]
			student_ps = string.split('\n')[54].split('&nbsp;')[1].split('</td>')[0]
			student_class = string.split('\n')[58].split('&nbsp;')[1].split('</td>')[0]
			student_from = string.split('\n')[60].split('&nbsp;')[1].split('</td>')[0]
			student_birthday = string.split('\n')[70].split('&nbsp;')[1].split('</td>')[0]
			print(student_id+':'+student_name+', '+student_ist+'('+student_major+')')
			id += 1
