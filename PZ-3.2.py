
x1 = int(input('������� ���������� x1: '))
y1 = int(input('������� ���������� y1: '))
x2 = int(input('������� ���������� x2: '))
y2 = int(input('������� ���������� y2: '))
if (1 <= x2 <= 8 and y1 == y2) or (1 <= y2 <= 8 and x1 == x2):
    print("True")
else:
    print("False")