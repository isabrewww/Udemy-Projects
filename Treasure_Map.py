row1 = ["ㅤ", "ㅤ", "ㅤ"]
row2 = ["ㅤ", "ㅤ", "ㅤ"]
row3 = ["ㅤ", "ㅤ", "ㅤ"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
row = int(position[1]) - 1
column = int(position[0]) - 1

map[row][column] = "X"

print(f"\n{row1}\n{row2}\n{row3}")