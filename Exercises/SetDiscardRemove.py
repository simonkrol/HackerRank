n = int(input())
s = set(map(int, input().split())) 
n=int(input())
for i in range(n):
    m=input()
    if(m=="pop"):
        s.pop()
    else:
        m=list(map(str, m.split()))
        command="s."+m[0]+"("+m[1]+")"
        eval(command)
n=0
for i in s:
    n+=i
print(n)