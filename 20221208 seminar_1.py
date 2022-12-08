# 1) напечатать сторку в одну линию - C:\WINDOWS\System32\drivers\etc\nst


data = open('fileCWin.txt', 'a')
data.write('C:\WINDOWS\System32\drivers\etc') 
data.write('\\') # если вы хотите напечатать одну обратную косую черту, используйте: ("\\")
data.write('nst') 

#print(data.readline())

