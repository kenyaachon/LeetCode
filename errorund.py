import sys

def butterrors():
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())

    except OSError as err:
        print("OS error: {0}".format(err))

    except ValueError:
        print("Could not change data to an integer")
    except:
        print("Unexpected error", sys.exc_info()[0])
        raise

def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)]

    for i in range(1, n+1):
        for w in range(W, 0, -1):  
            if wt[i-1] <= w:
                dp[w] = max(dp[w], dp[w-wt[i-1]] + val[i-1])

    return dp[W]

def main():
    val = [60, 100, 120]
    wt = [10, 20, 30]

    W = 50
    n = len(val)
    print(knapSack(W, wt, val, n))


if __name__=="__main__":
    main()

