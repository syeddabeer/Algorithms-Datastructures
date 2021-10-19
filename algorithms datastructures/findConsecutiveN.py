def findConsecutiveN(N):
    start=1
    end=(N+1)//2
    
    while start < end:
        Sum=0
        
        for i in range(start, end+1):
            Sum+=i
            
            if Sum == N:
                for j in range(start, i+1):
                    print(j, end= " ")
                    
                print()
                break;
            
            if Sum > N:
                break
                
        Sum = 0
        start += 1
        
Number=125
findConsecutiveN(Number)