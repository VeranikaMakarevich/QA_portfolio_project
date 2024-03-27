import random
import time

# driver sleep from 1 to 4 seconds
def delay():
    time.sleep(random.randint(1, 4))


# different variables

url = 'https://qasvus.wixsite.com/ca-marketing' # website url
cm_title = 'Home | California Marcketing' # website title

# variables for XPath
X_head = "(//div[@class='CJF7A2'])[1]" # XPath for header
img_l = "//img[@width='120']" # XPath for logo image
nw = "//a[contains(.,'CALIFORNIA MARCKETING')]" # XPath for name of website
L1 = "//img[contains(@src,'auto/Facebook.png')]" #first social network link
L2 = "//img[contains(@src,'auto/Twitter.png')]" # second social network link
L3 = "//img[contains(@src,'auto/VK%20Share.png')]" # third social network link
L4 = "//img[contains(@src,'auto/YouTube.png')]" # fourth social network link
L5 = "(//img[@fetchpriority='high'])[5]" # fifth social network link
L6 = "//img[contains(@src,'auto/LinkedIn.png')]" # sixth social network link
L7 = "(//img[@fetchpriority='high'])[7]" # seventh social network link





