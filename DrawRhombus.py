inputValue = int(input('input interger:'))

base = ' '
for i in range(inputValue):
    base = ' '+str(2*(inputValue-1-i)+1)+base+str(2*(inputValue-1-i)+1)+' '

length = len(base.strip())
graph = []
for j in range(inputValue):
    line = ' '
    for k in range(j):
        line = '  '+line+'  ' + '   '
    for i in range(inputValue-j):
        line = ' '+str(2*(inputValue-1-i)+1)+line+str(2*(inputValue-1-i)+1)+' '
    line = line.strip()
    length_temp = int((length-len(line))/2)
    for m in range(length_temp):
        line = ' '+line+' '
    graph.append(line)
for j in range(inputValue):
    graph.append(graph[inputValue-1-j])
for line in graph:
    print(line)
