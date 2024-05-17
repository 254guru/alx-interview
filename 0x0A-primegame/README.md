<h1>Prime Game</h1>

<p>Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including <code>n</code>, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.</p>

<p>They play <code>x</code> rounds of the game, where <code>n</code> may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.</p>

<h2>Prototype</h2>

<pre><code>def isWinner(x, nums)
</code></pre>

<h3>Parameters</h3>

<ul>
    <li><code>x</code> (int): The number of rounds.</li>
    <li><code>nums</code> (list of int): An array where each element represents the value of <code>n</code> for each round.</li>
</ul>

<h3>Return</h3>

<ul>
    <li>The name of the player that won the most rounds (<code>"Maria"</code> or <code>"Ben"</code>).</li>
    <li>If the winner cannot be determined, return <code>None</code>.</li>
</ul>

<h3>Assumptions</h3>

<ul>
    <li><code>n</code> and <code>x</code> will not be larger than 10000.</li>
    <li>You cannot import any packages in this task.</li>
</ul>

<h3>Example</h3>

<pre><code>x = 3
nums = [4, 5, 1]

# First round: n = 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: n = 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: n = 1
# Ben wins because there are no prime numbers for Maria to choose

# Result: Ben has the most wins
</code></pre>

<h3>Example Execution</h3>

<pre><code>carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

carrie@ubuntu:~/0x0A-primegame$
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
</code></pre>

<p>This script determines the overall winner after <code>x</code> rounds of the game based on the optimal play of both players. The output shows the player with the most wins across all rounds.</p>
