def sumComp(n):
    highcompositenum = [2, 3, 2, 5, 2, 3, 7, 2, 11, 13, 2, 3, 5, 17, 19, 2, 23, 7, 29, 3, 31, 2, 37, 41, 43, 47, 5, 53, 59, 2, 11, 61, 3, 67, 71, 73, 79, 13, 83, 89, 2, 97, 101, 103, 107, 7, 109, 113, 17, 127, 131, 137, 139, 3, 5, 149, 151, 19, 2, 157, 163, 167, 173, 179, 181, 191, 193, 197, 19]

    sum = 1
    for i in range(0, n):
        sum *= highcompositenum[i]

    return sum

def triangleSum(nthnum, divsormin):
    n = 4
    while True:
        

        sum = (nthnum * (nthnum + 1))/2
        #sum = sumComp(n)
        divisors = 0
        
        #for i in range(1, sum+1):
        
        if ((sum % 2 == 0) and (sum % 5 == 0) and (sum % 3 == 0)):
            i = 1.0
            while i <= sum:
                if sum % i == 0:
                    divisors += 1
                i+=1

            print("sum", sum, " nth num",nthnum, " divisors ", divisors)

        if divisors > divsormin:
                print(sum, " is the first triangle number to have more than 500 divisors")
                return

        nthnum += 1
        n += 1
    

        '''
        while i <= sum:
            if sum % i == 0:
                m = sum / i
                divisors += 1
                if m % i == 0 :   
                    divisors += 1
            if divisors > divsormin:
                print(sum, " is the first triangle number to have more than 500 divisors")
                return
            i+=1
        '''


def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

def primesFile(nth):
    list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163
, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251
, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349
, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443
, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557
, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647
, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757
, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863
, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983
, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 
1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171
, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277,
1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 
1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471
, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559,
1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 
1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753
, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871,
1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 
1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081
, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161,
2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381
, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473,
2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699
, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791,
2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 
2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999]

    return list


def triangle(nth, divisorMin):
    primesList = primesFile(nth)
    divisors = 1

    while True:
        #primesList = primes(nth)
        frequency = []
        sum = (nth * (nth + 1))/2
        storedSum = sum

        #the frequency of each primer factor for the triangle number
        i = 0
        freq = 0
        listlen = len(primesList)
        while sum > 1.0 and i < listlen:
            while sum % primesList[i] == 0:
                sum /= primesList[i]
                freq += 1
            
            frequency.append(freq)
            freq = 0
            i+=1

        #use the for 
        listlen = len(frequency)
        for i in range(0, listlen):
            if frequency[i] != 0:
                divisors *= (frequency[i] + 1)

        if divisors > divisorMin:
            print(storedSum, " is the first triangle number to have more than 500 divisors")
            print(divisors, "divisors")
            return
        divisors = 1
        nth += 1



def main():
    #triangleSum(7, 5)
    #triangleSum(6, 3)
    #triangleSum(8, 5)
    #triangleSum(12370, 500)

    #triangle(7, 5)
    #primes(13)
    triangle(10000, 500)


if __name__== "__main__":
    main()