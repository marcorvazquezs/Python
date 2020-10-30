# Regular Expressions

* Regular expressions are mini-language for specifying text patterns. 
* Regex strings often use **\\** backslashes so use raw strings: **r'\\d'**
* Import the **re** module first 
* Call the **re.compile()** function to create a regex object. 
* Call the regex object's **search()** method to create a match object. 
* Call the match object's **group()** method to get the matched string.
* **\\d** is the regex for a numeric digit character. 