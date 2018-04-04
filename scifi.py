# try to replicate 2p + 1
# figure how long something can stay prime
# later try 2c + 1 and see how long it turns

import math


def checkPrime(i):
   prime = True
   sqrt = int(math.sqrt(i) + 1)
   for j in xrange(2,sqrt):
      if i % j == 0:
         prime = False
         break

   return prime


def main():
   for i in xrange(2,100):
      ret = checkPrime(i)
      if ret:
         print str(i) + ":  Prime"
         # ret2 = True
         # secPrime = i
         # while ret2:
         #    secPrime = 2 * secPrime + 1
         #    ret2 = checkPrime(secPrime)
         #    if ret2:
         #       print secPrime

#      print str(i) + " " + str(ret)

if __name__ == "__main__":
   main()

   # for i in xrange(1, 100):
   #    prime = True
   #    if i == 1:
   #       prime = False
   #    elif i == 2:
   #       pass
   #    else:
   #       sqrt = int(math.sqrt(i) + 1)
   #       for j in xrange(2,sqrt):
   #          if i % j == 0:
   #             prime = False
   #             break
   #
   #    return prime
   #    # if prime:
   #    #    print str(i) + " is prime"
   #    # else:
   #    #    print str(i) + " is composite"


# algo
# 1) store 1st 100 primes in array and store if they have any primes when applying 2p + 1
# 2) as we generate primes, we calculate then and there if it has a string of primes (more efficient)