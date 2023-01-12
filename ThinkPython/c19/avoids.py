#!/usr/bin/env python3


def avoids(word, forbidden):
      return set(word) <= set(forbidden)



print(avoids('gabriel', 'abcdefghijklmnopqr'))
