# Lockboxes

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
<ul>
<li>Prototype: def canUnlockAll(boxes)</li>
<li>boxes is a list of lists</li>
<li>A key with the same number as a box opens that box</li>
<li>You can assume all keys will be positive integers</li>
<li>There can be keys that do not have boxes<li>
<li>The first box boxes[0] is unlocked<li>
<li>Return True if all boxes can be opened, else return False</li>
</ul>
		carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
		#!/usr/bin/python3

		canUnlockAll = __import__('0-lockboxes').canUnlockAll

		boxes = [[1], [2], [3], [4], []]
		print(canUnlockAll(boxes))

		boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
		print(canUnlockAll(boxes))

		boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
		print(canUnlockAll(boxes))

		carrie@ubuntu:~/0x01-lockboxes$


		carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
		True
		True
		False
		carrie@ubuntu:~/0x01-lockboxes$
