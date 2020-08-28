'''You are given a set A  and n  other sets.
Your job is to find whether set A  is a strict superset of each of the N sets.

Print True, if A  is a strict superset of each of the N  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.'''
s=set(map(int,input().split()))
n=int(input())
l=[]
def check():
  sub=set(map(int,input().split()))
  if sub.issubset(s):
    if len(sub)==len(s):
      l.append(0)
    else:
      l.append(1)
  else:
    l.append(0)
    
if all(l)==1:
  print("TRUE")
else:
  print("FALSE")
