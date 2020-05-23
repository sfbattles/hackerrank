def staircase(num_of_stairs):
    print_char = " "
    for x in range(num_of_stairs,0,-1):
        for y in range(1, num_of_stairs+ 1):            
            if y >= x:
                print_char = "#"
            else:
                print_char = " "    
            print(f"{print_char}",end="")        
        print()
            

staircase(10)
