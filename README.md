This ReadME Contains analysis' of each Blind75 Problem Solution and my thought process behind each solution.

Contains Duplicate:
  This solution is functional, but it relies on checking every value with itself taking O(n^2) time. 
  This is computatioally inefficienc when compared to other solutions for this problem.
  I'd Like to return to this problem when i have a better understanding of hashing , which should allow  for this problem to be solved in O(n) time.

Remove Duplicate:
  My main struggle with this problem was centered around me iterating over a list that i was altering. 
  It took me about 20 minuites to realize that i should probably use a copy of the list to iterate while editing the real list to get the right output.
  Another lesson learned, never change something and read from it simultaneously, as you can always create a copy to utilize that same information
  

Valid Anagram:
  This solution is rudimentary, and there were much simpler ways to solve the problem.
  The easiest way wouldve been to use the python sorted() function on each of the strings and simply return if the strings were equal or not.
  I learned that there's most likely always a more streamlined way to do what you're oing, and you should always look for that way.

Remove Element:
  This one was easy, just had to remember to exclude anything that doesn't directly contribute to the task at hand. 
  Simplicity is the key.
