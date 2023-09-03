input_text = input()



Drawing_List = input_text.split(",")

WC = 0
"""WC means Width Coder"""
HC = 0
"""HC means Height Coder"""
BC = 0
"""BC means Blank Coder"""
DC = 0
"""DC means Dashed Coder"""
total_widths_list = [0]
total_heights_list = [0]

offset_starter = 0

offset_diff = 0

max_width = 0
max_height = 0

height_counter = 0
shape_counter = 0

Total_Height_For_DL = 0
N_Counter = 0

D_Counter = 0

Balancer_x = 0
Balancer_y = 0
searcher = 0

int_counter = 0


"""Dashed Lines Counter"""

"""
-------------------------------------------------------------------------------------------------------------------
"""

def grouped_shape_counter(Drawing_List):
    shapes = {"T": 0, "S": 0, "V": 0, "R": 0, "E": 0}
    count_list = []

    for draw in Drawing_List:
        if draw == "N" or draw == "B":
            count_list.append(shapes.copy())
            shapes = {"T": 0, "S": 0, "V": 0, "R": 0, "E": 0}
        elif draw == "DL":
            continue
        elif len(draw) >1 and draw[0] in shapes.keys():
            shapes[draw[0]] += 1
    count_list.append(shapes)
    return count_list

number_counter = 0
list_of_list = []

offset_list = []

for lists in range(len(grouped_shape_counter(Drawing_List))):
    for numbers in grouped_shape_counter(Drawing_List)[lists].values():
        number_counter += int(numbers)
    list_of_list.append(number_counter)
    number_counter = 0

#print(list_of_list)
#print(grouped_shape_counter(Drawing_List))


"""
-------------------------------------------------------------------------------------------------------------
"""

for search in Drawing_List:
    if search[0] == "O":
        if offset_starter == 0:
            offset_starter = 1
            if int(search[1]) > 1:
                searcher -= 1

offset = 0 + offset_starter

for draws in Drawing_List:

    if len(draws) == 2:

        if draws[0] == "T":
            height = int(draws[1])
            total_widths_list[WC] += (2*(height)-1+1)
            if total_heights_list[HC] < height:
                total_heights_list[HC] = height

        elif draws[0] == "S":
            height = int(draws[1])
            total_widths_list[WC] += height+1
            if total_heights_list[HC] < height:
                total_heights_list[HC] = height

        elif draws[0] == "V":

            width = int(draws[1])
            height = (width+1)//2
            total_widths_list[WC] += width+1
            if total_heights_list[HC] < height:
                total_heights_list[HC] = height

        elif draws[0] == "O":
            total_widths_list[WC] += int(draws[1])



    elif len(draws) == 1:
        if draws[0] == "N":
            #total_widths_list[WC] =+ list_of_list[WC]
            total_widths_list.append(0)
            WC += 1
            total_heights_list.append(0)
            HC += 1

        elif draws[0] == "B":
            BC += 1

    elif len(draws) == 3:
        if draws[0] == "V":
            width = int(draws[1]), int(draws[2])
            width = int("".join(map(str, width)))
            height = (width+1)//2
            total_widths_list[WC] += width+1
            if total_heights_list[HC] < height:
                total_heights_list[HC] = height


    else:
        if draws[0] == "R":
            height = int(draws[1])
            width = int(draws[3])
            total_widths_list[WC] += width+1
            if total_heights_list[HC] < height:
                total_heights_list[HC] = height


        elif draws[0] == "E":
            height = int(draws[1])
            width = int(draws[3])
            total_widths_list[WC] += width+1
            if total_heights_list[HC] < height:
                total_heights_list[HC] = height

#total_widths_list[WC] += list_of_list[WC]

"""
-----------------------------------------------------------------------------------------------------------------------
"""

max_width = max(total_widths_list)

for heights in total_heights_list:
    max_height += heights

offset += searcher

max_height += BC + 1

canvas = [[" " for w in range(max_width)] for h in range(int(max_height)-1)]
"""
-----------------------------------------------------------------------------------------------------------------------
"""

def pixel_creator(canvas, x, y, char="*"):
    if 0 <= x < len(canvas[0]) and 0 <= y < len(canvas):
        canvas[y][x] = char

def T_Drawer(canvas, peak, height, offset):
    x, y = peak
    for i in range(height):
        for j in range((x - i), x + i + 1):
            pixel_creator(canvas, j + offset + offset_diff, y+i + (total_heights_list[N_Counter]-height))

def S_Drawer(canvas, top_left, height, offset):
    x,y = top_left
    width = height
    for i in range (height):
        for j in range(width):
            pixel_creator(canvas, x + j + offset, y + i + (total_heights_list[N_Counter]-height))

def V_Drawer(canvas, top, width, offset):
    x,y = top
    height = (width +1) // 2
    for i in range(height):
        for j in range(x - i + offset, x+i+offset+1):
            pixel_creator(canvas, j+width//2, y + height - 1 - i)


def R_Drawer(canvas, top_left, height, width, offset):
    x,y = top_left
    for i in range (height):
        for j in range(width):
            #print(current_height)
            pixel_creator(canvas, x + j + offset, y + i + (total_heights_list[N_Counter]-height))

def E_Drawer(canvas, top_left, height, width, offset):
    x, y = top_left
    for i in range(height):
        for j in range(width):
            pixel_creator(canvas, x + j + offset + Balancer_x, y + i, char=" ")

def Canvas_Printer(canvas):
    for row in canvas:
        print("".join(row))
"""
------------------------------------------------------------------------------------------------------------------------
"""



current_height = 0
current_width = 0
max_height_in_row = 0

int_total_heights_list = [0]

for p in range(len(total_heights_list)):
    int_total_heights_list.append(int_total_heights_list[p] + total_heights_list[p])

indenter = 0

for search in Drawing_List:
    if search == "DL":
        if D_Counter == 0:
            canvas.append([" " for w in range(max_width)])
            current_height += 1
            D_Counter += 1

D_Counter = 0

#if BC == 1:
    #canvas[0].pop(0)
#print(offset)

for draws in Drawing_List:
    if len(draws) == 2:
        if draws[0] == "T":
            #print(offset)
            height = int(draws[1])
            if indenter == 0:
                current_width += height-1
            max_height_in_row = max(max_height_in_row, height)
            T_Drawer(canvas, (current_width, current_height), height, offset)
            current_width += height + 1

        elif draws[0] == "S":
            height = int(draws[1])
            max_height_in_row = max(max_height_in_row, height)
            S_Drawer(canvas, (current_width, current_height), height, offset)
            current_width += height+ 1

        elif draws[0] == "V":
            width = int(draws[1])
            max_height_in_row = max(max_height_in_row, (width + 1//2))
            V_Drawer(canvas, (current_width, current_height), width, offset)
            current_width += width+1


        elif draws[0] == "D":
            if D_Counter == 0:
                for d in range(len(canvas[0])):
                    canvas[0][d] = "-"
                D_Counter += 1
            elif D_Counter%2 == 0:
                D_spawner = int(D_Counter/2 - 2)
                current_height += 1
                canvas.append([" " for w in range(max_width)])
                for z in range(len(canvas[Total_Height_For_DL+1])):
                        canvas[Total_Height_For_DL+1][z] = "-"
                canvas[Total_Height_For_DL+1].pop()
                offset = 0

        elif draws[0] == "O":
            offset_list.append(offset)
            offset += int(draws[1])
            offset_diff = offset - offset_list[len(offset_list) - 1]
            offset_diff -= 1
            for q in range(offset_diff):
                for index, list in enumerate(canvas):
                    if index == 0:
                        list.append("-")
                    else:
                        list.append(" ")


    elif len(draws) == 1:
        if draws[0] == "N":
            current_height += max_height_in_row
            Balancer_x = int(((max_width - 1 - current_width) / 2))
            for l in range(int_total_heights_list[int_counter]+1, int_total_heights_list[int_counter+1]+1):
                for x in range(Balancer_x):
                    canvas[l].insert(0, " ")
                    canvas[l].pop()
            current_width = 0
            int_counter += 1
            max_height_in_row = 0
            offset = 0 + offset_starter
            D_Counter += 1
            Total_Height_For_DL += total_heights_list[N_Counter]
            N_Counter += 1


            #print(Total_Height_For_DL)

        elif draws[0] == "B":
            current_height += 1
            Total_Height_For_DL +=1

    elif len(draws) == 3:
        if draws[0] == "V":
            width = int(draws[1]), int(draws[2])
            width = int("".join(map(str, width)))
            max_height_in_row = max(max_height_in_row, (width + 1//2))
            V_Drawer(canvas, (current_width, current_height), width, offset)
            current_width += width+1


    else:
        if draws[0] == "R":
            height = int(draws[1])
            width = int(draws[3])
            max_height_in_row = max(max_height_in_row, height)
            R_Drawer(canvas, (current_width, current_height), height, width, offset)
            current_width += width+ 1


        elif draws[0] == "E":
            height = int(draws[1])
            width = int(draws[3])
            E_Drawer(canvas, (current_width, current_height), height, width, offset)
            current_width += width+ 1
            max_height_in_row = max(max_height_in_row, height)

bottom_line = max_width + offset_diff + offset_starter

for draws_2 in range(len(Drawing_List)):
    if Drawing_List[draws_2] == "DL" and Drawing_List[draws_2 + 1] == "DL":
        for l in range(int_total_heights_list[0] + 1, int_total_heights_list[1] + 1):
            for x in range(1):
                canvas[l].insert(0, " ")
                canvas[l].pop()

while "DL" in Drawing_List:
    while not(len(canvas[0]) <= (bottom_line - 1)):
        canvas[0].pop(0)
        break
    break


Canvas_Printer(canvas)

if "DL" in Drawing_List:
    print("-" * (bottom_line - 1))
else:
    print("-" * (max_width - 1))

"""
print(total_heights_list)
print(total_widths_list)
print(max_width)
print(max_height)
print(canvas)
"""



