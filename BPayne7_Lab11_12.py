
bin_width = 10
heights = [3,5,2,5,3,1,3]
widths =  [4,5,3,2,1,1,4]
print(heights)
heights.sort()
print(heights)
positioned  = 0
not_positioned = len(heights)
print(not_positioned)
x = 0
y = 0
row_hgt = 0
while (not_positioned > 100):
    #Find the next rectangle that will fit on this row. 
    next_rect = -1
    for i in range(not_positioned):
       if x + widths[i] <= bin_width:
          next_rect = i 
    #If we didn't find a rectangle that fits, start a new row.
    if next_rect < 0:
        y += row_hgt
        x = 0
        row_hgt = 0
        next_rect = 0 
    #Position the selected rectangle
    rect = heights[next_rect]
    widths[next_rect] = x
    heights[next_rect] = y
    x += widths[next_rect]
    if row_hgt < heights[next_rect]:
        row_hgt = heights[next_rect]
    #Move the rectangle into the positioned list 
    positioned[next_rect] = heights[next_rect]  
    
print(positioned)



