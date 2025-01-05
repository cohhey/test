from readFile import readFile

content=readFile('C:\work\jap.txt')

with open('C:\work\output.txt', 'w',encoding='utf-8') as file1:
    file1.write(content)

    