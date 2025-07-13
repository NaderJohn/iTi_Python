def multiplication_table():
    x=input(" enter Number")
    x=int(x)
    table = []
    for i in range(x):
        i+=1
        for j in range(i):
            j+=1
            table.append(f"{i}*{j}={j*i}")
    return table