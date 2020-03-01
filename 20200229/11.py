## 방법1
import sys
sys.stdin = open("input11.txt", "rt")
n = int(input())

for i in range(n):
    tmp = input().upper()
    size = len(tmp)
    for j in range(size//2):
        if tmp[j] != tmp[-1-j]: # -1로 뒤 부터 인덱스 접근.
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' %(i+1))

## 방법2
for i in range(n):
    tmp = input().upper()
    if tmp == tmp[::-1]:
      print('#%d NO' %(i+1))
    else:
      print('#%d YES' %(i+1))