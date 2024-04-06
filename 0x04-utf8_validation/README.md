  <h1>UTF-8 Validation</h1>

  <h2>Description</h2>
  <p>Write a method that determines if a given data set represents a valid UTF-8 encoding.</p>

  <h2>Prototype</h2>
  <pre><code>def validUTF8(data)</code></pre>

  <h2>Return</h2>
  <p>True if data is a valid UTF-8 encoding, else return False</p>

  <h2>Constraints</h2>
  <ul>
   <li>A character in UTF-8 can be 1 to 4 bytes long</li>
   <li>The data set can contain multiple characters</li>
   <li>The data will be represented by a list of integers</li>
   <li>Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer</li>
  </ul>

  <h2>Example</h2>
  <pre><code>data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
  </code></pre>

  <h2>Output</h2>
  <pre><code>$ ./0-main.py
True
True
False
  </code></pre>

