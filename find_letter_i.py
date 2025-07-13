def find_letter_i():
    x=input("Enter any name  ")
    x=str(x)
    positions = []
    for i in range(len(x)):
        if x[i]=="i":
            positions.append(i+1)
    return {"text": x, "positions": positions}