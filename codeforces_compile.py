import os,sys

n  = int(raw_input())

a = raw_input().split()
b = raw_input().split()
c = raw_input().split()

dict_a = dict()
dict_b = dict()
dict_c = dict()

for elem_a in a:
	if elem_a in dict_a:
		dict_a[elem_a] += 1
	else:
		dict_a[elem_a] = 1

for elem_b in b:
	if elem_b in dict_b:
		dict_b[elem_b] += 1
	else:
		dict_b[elem_b] = 1

for elem_b in b:
	if elem_b in dict_a:
		dict_a[elem_b] -= 1

for elem_c in c:
	if elem_c in dict_b:
		dict_b[elem_c] -= 1

for keys_a in dict_a.keys():
	if dict_a[keys_a] == 1:
		print keys_a
		break

for keys_b in dict_b.keys():
	if dict_b[keys_b] == 1:
		print keys_b
		break
