N, N_list = int(input()), input().split()
if all([int(item) > 0 for item in N_list]): print(any([item == item[::-1] for item in N_list])) 
else: print(False)
