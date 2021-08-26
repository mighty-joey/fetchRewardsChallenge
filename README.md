# FetchRewardsChallenge

This is a test script designed to fulfill the requirements of the Fetch Rewards SDET coding exercise.

First we need to ensure that the machine running this script has all of the necessary software. The requirements include:
- Python
- Selenium
- Google Chrome
- ChromeDriver

# Installation
To install Python, visit the Python website at https://www.python.org/ and follow the installation instructions for your operating system.

To install Selenium, you can do so via the Command Prompt or Terminal. Assuming you have ‘pip’ installed on your machine, you can simply run the command ‘pip install selenium’ (PC) or ‘pip3 install selenium’ (Mac). This will install Selenium onto your machine. Help with this process can be found here: https://selenium-python.readthedocs.io/installation.html

To install Google Chrome, visit this website https://www.google.com/chrome/ and follow the installation instructions for your operating system.

To install ChromeDriver, visit this website: https://chromedriver.chromium.org/downloads and install the version of ChromeDriver that matches your version of Google Chrome and operating system. To find out which version of Chrome you have, simply select the three dots on the upper right corner of Chrome > Help > About Google Chrome and find the version number.

Ensure that ChromeDriver is in an easily accessible location on your machine. I have ChromeDriver inside the ‘Applications’ folder on my Mac for easy access. This is an important step, because we will need to know the file path to ChromeDriver on your machine in a later step.

# Running the script
Open Command Prompt or Terminal. From the command line, you will need to navigate to the directory that contains this script. Once inside the correct directory, run ‘python3 main.py /Applications/chromedriver’. This assumes that you’ve placed ChromeDriver inside your Applications folder on a Mac. On a PC, the path will be something like ‘C:\Program Files (x86)\chromedriver.exe’, assuming you’ve placed the ChromeDriver inside your Program Files folder.

The script will open Chrome to the supplied URL, test the application using an optimal algorithm, and output the results via the command line interface.

Thanks for giving me the opportunity to show you my work!

