# Regular Expressions


### Basics

* Regular expressions are mini-language for specifying text patterns. 
* Regex strings often use **\\** backslashes so use raw strings: **r'\\d'**
* Import the **re** module first 
* Call the **re.compile()** function to create a regex object. 
* Call the regex object's **search()** method to create a match object. 
* Call the match object's **group()** method to get the matched string.
* **\\d** is the regex for a numeric digit character. 

### Groups and Pipes

* Groups are created in regex strings with parentheses. 
* The first set of parentheses is group 1, second is group 2, and so on. 
* Calling **group()** or **group(0)** returns the full matching string, **group(1)** returns group 1's matching string and so on. 
* Use **\\(** and **\\)** to match literal parentheses in the regex string. 
* The **|** pipe can match one of many possible groups. 