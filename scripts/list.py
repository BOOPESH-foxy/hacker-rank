t = int(input())
task_list = []
for _ in range (t):
    to_perform,i,*e = input().split()
    e = e[0] if e else ''

    if to_perform in "insert":
        task_list.insert(int(i) ,int(e))
    elif to_perform in "print":
        print(task_list)
    elif to_perform in "remove":
        task_list.remove(i)
    elif to_perform in "append":
        task_list.append(i)
    elif to_perform in "sort":
        task_list.sort()
    elif to_perform in "pop":
        task_list.pop()
    elif to_perform in "reverse":
        task_list.sort(reverse = True)
        