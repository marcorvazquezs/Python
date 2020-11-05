# Working with Files 

**Root Folder**: the lowest folder 

**Current Working Directory**: the folder that any relative paths are relative to. 

**Absolute paths**: begin with the root folder, relative paths do not. 

### os module 

* Use the **os.path.join()** function to combine folders with the correct slash. 
* **os.getcwd()** - will return the current working directory. 
* **os.chdir()** - will change the current working directory. 
* **os.path.abspath()** - returns an absolute path form of the path passed to it. 
* **os.path.isabs()** - returns True if the path passed to it is absolute. 
* **os.path.relpath()** - returns the relative path between two paths passed to it. 
* **os.makedirs()** - can make folders. 
* **os.path.getsize()** - returns a file's size. 
* **os.listdir()** - returns a list of strings of filenames
* **os.path.exists()** - returns True if the filename passed to it exists. 
* **os.path.isfile()** and **os.path.isdir()** return True if they were passed a filename or file path. 


## Reading and Writing Files

* **open()** will return a file object which has reading and writing-related methods. 
  * pass **'r'** (or nothing) to **open()** to open the file in read mode 
  * **'w'** for write mode 
  * **'a'** for append mode 
  * Opening a non-existant filename in write or append mode will create that file
* Call **read()** or **write()** to read the contents of a file or write a string to a file. 
* Call **readlines()** to return a list of strings of the file's content. 
* Call **close()** when you are done with the file. 
* **Shelve** module can store Python values in a binary file 
  * **shelve.open()** returns a dictionary-like shelf value

## Exceptions and Assertions 

* Raise your own exceptions using: **raise Exception('This is the error message.')**
  * User errors should raise exceptions
* Use assertions using: **assert condition, 'Error message'** 
  * Assertions are for detecting programmer errors that are not meant to be recovered from. 

## Logging 
* The logging module lets you display logging messages. 
* After calling **basicConfig()** to set up logging, call **logging.debug()** to create a log message. 
* Five log levels
  * DEBUG
  * INFO 
  * WARNING
  * ERROR
  * CRITICAL
* To disable log messages use **logging.disable(logging.CRITICAL)**

## Debugger
* Debugger is a tool that lets you execute Python code one line at a time and shows you the values in variables. 
* Open the Debug Control window with **Debug > Debugger** before running the program. 
  * The **Over** button will step over the current line of code and pause on the next one. 
  * The **Step** button will step into a function call. 
  * The **Out** button will step out of the current function you are in. 
  * The **Go** button will continue the program until the next breakpoint or end of the program. 
  * The **Quit** button will immediately terminate the program. 
  * Breakpoints can be set by right-clicking the file editor window and selecting "Set Breakpoint"