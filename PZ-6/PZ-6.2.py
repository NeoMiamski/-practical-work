# ��� ������������� ������ A ������� N. ���������� � ����� ������������� 
# ������ B ���� �� ������� ������� ��� �������� ��������� ������ � ������� 
# ��������, � ����� � � ���������: A2,  �4,  �6, �,  A1,  A3,  �5, � . �������� 
# �������� �� ������������. 
try:
    n = int(input("������� ������ ������: "))
    A = []
    B = []
    for i in range(1, n + 1):
        A.append(i)
    for j in range(2, n + 1, 2):
        B.append(j)
    for k in range(1, n + 1, 2):
        B.append(k)
    print(A)
    print(B)
except ValueError:
    print('�� ����� ������������ ��������')