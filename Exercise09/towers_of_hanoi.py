n = 4
start = range(n, 0, -1)
end = []
temp = []

def move_rings(n, start, end, temp):


    if n == 1:
        end.append(start.pop())
        return 
    move_rings(n-1, start, temp, end)

    move_rings(1, start, end, temp)

    move_rings(n-1, temp, end, start)
   
    print end



move_rings(n, start, end, temp)