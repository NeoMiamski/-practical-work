try:    
    A = []
    n = int(input("������� ������ ������: "))
    q = int(input("������� �����������: "))
    a1 = int(input("������� ������ �����: "))
    for i in range(0, n):
        if i == 0:
            A.append(a1)  
        else:
            A.append(a1+(i*q))
    print(A)
except ValueError:
    print('�� ����� ������������ ��������')