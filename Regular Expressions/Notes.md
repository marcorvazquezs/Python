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

### Regex Repetition 

* The **?** says the group matches zero or one times. 
* The **\*** says the group matches zero or more times. 
* The **+** says the group matches one or more times. 
* The **{ }** braces can match a specific number of times. 
* The **{ }** braces with two numbers matches a minimum and maximum number of times. 
  * Leaving out the first or second number in the curly braces says there is no minimum or maximum. 
* Greedy matching match the longest string possible, nongreedy matching match the shortest string possible. 
  * Putting a question mark after the curly braces makes it do a nongreedy match. 

### Character Classes 

#### Recap

* The regex method **findall()** is passed a string, and returns all matches in it, not just the first match 
  * If the reges has 0 or 1 group, **findall()** returns a list of strings. 
  * If the regex has 2 or more groups, **findall()** returns a list of tuples of strings. 
  * You can make your own character classes with square brackets: **[aeiou]** 
  * A **^** caret makes it a negative character class, matching anything not in the brackets: **[aeiou]**

#### Shorthand Character Classes

* **\\d** - Any numeric digit from 0 to 9
* **\\D** - Any character that is *not* a numeric digit from 0 to 9
* **\\w** - Any letter, numeric digit, or the underscore character. (Think of this as matching "word" characters.)
* **\\W** - Any character that is *not* a letter, numeric digit, or the underscore character. 
* **\\s** - Any space, tab, or newline character. (Think of this as matching "space" characters.)
* **\\S** - Any character that is *not* a space, tab, or newline. 


