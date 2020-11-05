## Web Scraping with Python 

* The **requests** module is a third-party module for downloading web pages and files. 
* **requests.get()** returns a Response object. 
* **raise_for_status()** Response method will raise an exception if the download failed. 
* Save a downloaded file to your hard drive with calls to the **iter_content()** method. 
  
## Selenium 

* To import Selenium run: **from selenium import webdriver**
* Open a browser: **webdriver.Firefox()**
* Send browser to a URL: **browser.get('URL')**
* Return a list of WebElement objects: **browser.find_elements_by_css_selector()**
* Clicks on an element in the browser: **click()**
* **send_keys()** method types into a specific element in the browser. 
* **submit()** method simulates clicking on the Submit button for a form. 
* Browser can also be controlled with: 
  * **back()**
  * **forward()**
  * **refresh()**
  * **quit()**

