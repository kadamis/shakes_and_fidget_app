import threading
import math
def cuber(n):
    print(" The Jones Polynomial: {}".format(n**(-2)-n**(-1)+1-n+n**2))

def squarer(n):
    print("Square Root: {}".format(math.sqrt(n)))

if __name__ == "__main__":
# create the thread
    t1 = threading.Thread(target=squarer, args=(5,))
    t2 = threading.Thread(target=cuber, args=(5,))

# start the thread t1
    t1.start()
# start the thread t2
    t2.start()

# wait until t1 is completed
    t1.join()
# wait until t2 is completed
    t2.join()

    nop = int(input("Give number of players:"))
    
    for i in range(nop):
        
        p = input("Player:")
        level = int(input("Give level:"))
        power = int(input("Give power stat:"))
        intel = int(input("Give intel stat:"))
        dext = int(input("Give dext stat:"))
        energy = int(input("Give energy stat:"))
        luck = int(input("Give luck stat:"))
        armor = int(input("Give armor stat:"))
        ma = int(input("Give max armor in percentage:"))
        
        stat1 = (5*luck)/(2*level)
        stat2 = armor*level
        
        tot = 0
        if stat1<=50 and stat2<=25:
            tot = power+intel+dext+energy+luck+armor
        elif stat1>50 and stat2<=25:
            tot = power+intel+dext+energy+20*level+armor
        elif stat1<=50 and stat2>25:
            tot = power+intel+dext+energy+luck+level*ma
        elif stat1>50 and stat2>25:
            tot = power+intel+dext+energy+20*level+level*ma
        else:
            print("error") 
        index = tot/level
        
        print(tot, index)

# both threads completed
    print("Done!")
