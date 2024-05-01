<h1>Making Change</h1>

<p>Given a pile of coins of different values, this function determines the fewest number of coins needed to meet a given total amount.</p>

<h2>Prototype</h2>

<pre><code>def makeChange(coins, total)
</code></pre>

<h2>Returns</h2>
<p>The function returns the fewest number of coins needed to meet the total amount.</p>

<ul>
  <li>If the total is 0 or less, it returns 0.</li>
  <li>If the total cannot be met by any number of coins in your possession, it returns -1.</li>
</ul>

<h2>Parameters</h2>
<ul>
  <li><code>coins</code>: A list of the values of the coins in your possession. The value of each coin will always be an integer greater than 0.</li>
  <li><code>total</code>: The total amount to be met using the coins.</li>
</ul>

<h2>Constraints</h2>
<ul>
  <li>You can assume you have an infinite number of each denomination of coin in the list.</li>
</ul>

<h2>Example</h2>

<pre><code>print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
</code></pre>

