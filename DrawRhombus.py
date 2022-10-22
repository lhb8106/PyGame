inputValue = int(input('input interger:'))

length =0
graph = []
for j in range(inputValue):
    line = ' '

    #공백 넣기
    for k in range(j):
        line = '  '+line+'  ' + '   '

    #문자열 등록
    for i in range(inputValue-j):
        line = ' '+str(2*(inputValue-1-i)+1)+line+str(2*(inputValue-1-i)+1)+' '
        
    line = line.strip()
    graph.append(line)

#반대로 한번 더 출력
for j in range(inputValue):
    graph.append(graph[inputValue-1-j])
    
for line in graph:
    print(line)
