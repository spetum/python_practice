

##s1 = { 1, 2, 3, 4, 5}
##s2 = { 7, 8, 9}
##s1.update(s2,[6,7,8])
##print (s1)
##
##
##s1 = { 1, 2, 3, 4, 5}
##s2 = { 7, 8, 9}
##s1.update(s2)
##print (s1)
##s1.update([6,7,8])
##print (s1)
##s1.remove(6)
##
#### s1.remove(6)
#### KeyError ; not in set s1
##
##print (s1)
##
#### discard는 해당 원소를 집합 안에서 삭제한다.
#### 해당 원소가 집합 안에 없어도 KeyError를 발생시키지 않는다.
#### 
##s1 = { 1, 2, 3, 4, 5, 6, 7}
##s1.discard(6)
##print (s1)
##
##s1 = { 1, 2, 3, 4, 5, 7}
##s1.discard(6) 
##print (s1)



ss1 = { 1,2,3}
ss2 = { 2,3,4}
ss3 = { 3,4,5}

ss4 = ss1.intersection(ss2,ss3) ## 교집합
print (ss4)

print(ss1.intersection(ss2))
print(ss1.intersection(ss2,ss3))

ss4 = ss1.difference(ss2) ## 차집합
print (ss4)

ss4 = ss3.difference(ss1, ss2)
print (ss4)


ss4 = ss1.symmetric_difference(ss2) ## 양쪽 모두에게 없는 원소들을 출력해준다.
print (ss4)
