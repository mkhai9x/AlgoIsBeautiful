## Maximum index a pointer can reach in N steps by avoiding a given index B

Given two integers <code>N</code> and <code>B</code>, the task is to print the maximum index a pointer, starting from <code>0th</code> index can reach in an array of natural numbers <code>(i.e., 0, 1, 2, 3, 4, 5…)</code>, say <code>arr[]</code>, in <code>N</code> steps without placing itself at index <code>B</code> at any point.
In each step, the pointer can move from the Current Index to a <b>Jumping Index</b> or can remain at the <b>Current Index</b>. 
<code>Jumping Index = Current Index + Step Number</code>

> **Example :**
> <pre>
> Input: N = 3, B = 2 
> Output: 6 
> </pre>
> **Explanation :**
> <pre>
> Step 1:
> Current Index = 0
> Step Number = 1
> Jumping Index = 0 + 1 = 1
> Step 2:Current Index = 1
> Step Number = 2
> Jumping Index = 1 + 2 = 3
> Step 3:
> Current Index = 3
> Step Number = 3
> Jumping Index = 3 + 3 = 6
> Therefore, the maximum index that can be reached is 6.
> </pre>

