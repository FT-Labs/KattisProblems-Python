"""
Author : Arda
Date : 8/30/2020
"""

probabilities = {}

def socks(k, m, n):
  total = k + m + n
  if total < 2:
    return 0

  if (k, m, n) in probabilities:
    return probabilities[(k, m, n)]

  prob = 0

  # Selected a white pair
  if n >= 2:
      prob += n * (n-1)

  # Selected two paired socks
  if m >= 2:
    # Successful pair
    prob += m
  if m >= 4:
    # Mismatched pair
    prob +=m* (m-1) * socks(k+2, m-4, n)

  # Selected mixed white and paired socks
  if m >= 2 and n >= 1:
    prob += socks(k+1, m-2, n-1) * m * n * 2

  # Selected a singleton (always mismatched)
  if k >= 2:
    prob += socks(k-2, m, n) * k * (k-1)
  if k >= 1 and m >= 1:
    prob += socks(k, m-2, n) * k * m * 2
  if k >= 1 and n >= 1:
    prob += socks(k-1, m, n-1) * k * n * 2


  prob /= total * (total - 1.0)
  probabilities[(k, m, n)] = prob

  return prob


m,n = [int(x) for x in input().split()]
print(probabilities)
print(1-socks(0,m*2,n))










