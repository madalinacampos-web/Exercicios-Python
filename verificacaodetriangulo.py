a=(int(input()))
b=(int(input()))
c=(int(input()))

if ((a+c)>b) and ((b+a)>c) and ((c+b)>a):
    print("É um triângulo")
else:
    print("Não é um triângulo")
