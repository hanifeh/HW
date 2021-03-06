x = int(input("meghdare x ra vared konid : "))
series_number = int(input("tedad jomalate mored niaz ra vared konid : "))
m = 0
save_list = []
answer = 0

for i in range(1, series_number+1):

    m += i * (x ** i)
    save_list.append(1/m)
    if i % 2 == 1:
        answer += save_list[i-1]
    else:
        answer -= save_list[i-1]

print(answer)
