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

Concatenation of an Array:
  Simple and direct, no notes.

Reverse ALinked List:
  This one confused me at first. I did not know how to return to the Optional[ListNode] type at first. 
  After some googling i had figured it out, but what really got me was the head = ListNode bit. 
  I understood why it had to be there, but i was racking my brain trying to figure out how to get rid of the first index. 
  Then i remembered i can use slices to cut the first (technically second) index out. 
  Spent a whole lot of time trying to find a workaround when the fundamentals come in to save the day yet again.
