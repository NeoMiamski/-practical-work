# ��������� �������, ������� ������� �� ����� ������, ���������� ���������� � ���������� ����� ��������.
try:
    def LF(t):
        l = len(t)
        
        return l
    t = str(input())
    s = LF(t)
    print(s)
except ValueError:
    print('�� ����� ������������ ��������')