# ������� ������� RectPS(x1,y1,�2,y2,P, S), ����������� �������� P � ������� S
# �������������� �� ���������, ������������� ���� ���������, �� ����������� (�1,
# y1), (�2, y2) ��� ��������������� ������ (x1, y1, x2, y2 � �������, P � S �
# �������� ��������� ������������� ����). � ������� ���� ������� �����
# ��������� � ������� ���� ��������������� � ������� ���������������� ���������.
try:
    def RectPS(x1, y1, x2, y2):

        P = abs(x1 - x2) * 2 + abs(y1 - y2) * 2
        S = abs(x1 - x2) * abs(y1 - y2)

        return P, S

    x1 = int(input("������� x1: "))
    y1 = int(input("������� y1: "))
    x2 = int(input("������� x2: "))
    y2 = int(input("������� y2: "))
    PS1 = RectPS(x1, y1, x2, y2)
    x1 = int(input("������� x1: "))
    y1 = int(input("������� y1: "))
    x2 = int(input("������� x2: "))
    y2 = int(input("������� y2: "))
    PS2 = RectPS(x1, y1, x2, y2)
    x1 = int(input("������� x1: "))
    y1 = int(input("������� y1: "))
    x2 = int(input("������� x2: "))
    y2 = int(input("������� y2: "))
    PS3 = RectPS(x1, y1, x2, y2)
    print(PS1, PS2, PS3)
except ValueError:
    print('�� ����� ������������ ��������')