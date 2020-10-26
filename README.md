# Automate Workday Job Applications

The motivator behind developing this python script, was the amount of time I found myself wasting by filling out redundant job application information. I noticed that the majority of jobs I was applying to used Workday, hence they followed a similar structure and format. 
I've always been intrigued when my friends tell me "they wrote a script to do x", so I decided to automate this process and solve this pain point of mine!  
### Features
* Logs which jobs I've applied to and when I applied to them
* Automatically uploads my resume
* Automatically fills out <i>My Information</i> section, including contact and address information etc. 
* Automatically fills our <i>Work Experience</i> section (dev status: in progress)
### Dependencies
* Python 3.7
* SELENIUM (popular framework used for web browser automation )
* CHROME DRIVER ( download [here!](http://chromedriver.chromium.org/) ) which was used as the web driver.
* PANDAS library, which was used to read my application answers from an .xlsx file.
