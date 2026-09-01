coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
valid_cords=[[x,y] for x,y in coords if x>0 and y>0 ]
print(valid_cords)