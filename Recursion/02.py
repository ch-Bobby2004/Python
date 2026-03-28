def rec_tree(n):
    if n == 0:
        return
    print(n)
    rec_tree(n-1)
    print(n)
    
    
rec_tree(5)