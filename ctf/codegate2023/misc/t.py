name1 = "check1p2p3p4p5p6p"
print(f'name1     : {name1}')

# 문자열을 리스트로
name_list = list(name1)  
print(f'name_list : {name_list}')

# 리스트 역순으로
name_list.reverse() 
print(f'name_list : {name_list}')

# 리스트를 문자열로
name2 = ''.join(name_list)
print(f'name2     : {name2}')
