def fake_divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        result = first / second
        return result
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
