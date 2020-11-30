


def find_ratio(pegs):
    first_peg = pegs[1]
    
    for denom in range(1,10):
        nom_cap = first_peg*denom
        mod_gears = [rad * denom for rad in pegs]
        #print(mod_gears)
        for nom in range(denom, nom_cap):
            neg = False
            gear_ratios = [0]*len(pegs)
            gear_ratios[0] = nom
            for i in range(1, len(mod_gears)):
                distance = gear_ratios[i-1] + mod_gears[i-1]
                gear_ratios[i] = mod_gears[i] - distance
                if(gear_ratios[i] <= 0): 
                    neg = True
                    break
            if gear_ratios[-1]== float(gear_ratios[0]) / 2 and not neg:
                return [nom,denom]
 
    return [-1,-1]



test1 = [4,30,50]   #[12,1]
test2 = [4,17,50] #[-1,-1]
test3 = [6, 35, 50]

print(find_ratio(test1))
print(find_ratio(test2))
print(find_ratio(test3))
