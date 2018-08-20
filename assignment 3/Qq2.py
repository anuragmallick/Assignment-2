our_list = [] 
list2 = ['google','apple','facebook','microsoft','tesla'] 

first_v = (input('Enter first value: '))
second_v = (input('Enter second value: '))
third_v = (input('Enter third value: '))
 
our_list.append(first_v)
our_list.append(second_v)
our_list.append(third_v)

print(' (Q1)The list thus created is\t our_list=', our_list)
print('\n Adding this following list to a predefined list...which is,')
print('list2=',list2)
final=our_list+list2
print('\n\n',final)
