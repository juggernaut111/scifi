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
   primes = [2]   # list to store primes
   count = 0
   short = True

   for i in xrange(3, 10000, 2):
      if count >= 99:     # storing 1st 100 primes.  can comment out later
         break
      ret = checkPrime(i)
      if ret:
         if short:
            count += 1
#         print str(i) + ":  Prime"
         primes.append(i)

   mers = {}
   for i in primes:
      ret = True
      listOfPrimes = []
      newNum = i
      while ret:
         newNum = 2 * newNum + 1
         ret = checkPrime(newNum)
         listOfPrimes.append(newNum)
      mers[i] = listOfPrimes
   print mers
   longest = 0
   longestPrime = 0
   for itr in sorted(mers.keys()):
      if len(mers[itr][:-1]) > longest:
         longest = len(mers[itr][:-1])
         longestPrime = itr
      print str(itr) + " " + str(mers[itr][:-1]) + ".  Last number, which is composite was " + str(mers[itr][-1]) + ".  Length was " + str(len(mers[itr][:-1]))
   print "The prime with the longest run was: " + str(longestPrime) + " with a run of " + str(longest)

if __name__ == "__main__":
   main()


# algo
# 1) store 1st 100 primes in array and store if they have any primes when applying 2p + 1
# 2) as we generate primes, we calculate then and there if it has a string of primes (more efficient)