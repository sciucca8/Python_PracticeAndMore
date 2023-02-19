def nb_year(p0, percent, aug, p):
    count = 0
    percent /= 100
    
    while p0 < p:
        print(p0 * percent, round(p0 * percent, 0), int(p0 * percent)) #round rounds to the closest int
        p0 = p0 + aug + int(p0 * percent)                              #here we use int because it rounds for defect
        
        count += 1
        
    return count
        
print(nb_year(1500000, 0.25, 1000, 2000000))