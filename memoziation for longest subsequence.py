#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     19-03-2017
# Copyright:   (c) DELL 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def lcs(s1, s2):
  if len(s1) == 0 or len(s2) == 0:
      return 0
  try:
      return cache[(s1, s2)]
  except KeyError:
      if s1[-1] == s2[-1]:
          cache[(s1, s2)] = 1 + lcs(s1[:-1], s2[:-1])
      else:
          cache[(s1, s2)] = max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))
  return cache[(s1, s2)]
def main():
    pass

if __name__ == '__main__':
    main()
cache = {}
(u,v)=(raw_input(),raw_input())
print lcs(u,v)
