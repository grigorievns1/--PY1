salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
while months > 0:
    a = -(salary - spend)
    months -= 1
    spend *= 1.03
    need_money += a
# TODO Оформить решение

print(round(need_money))
