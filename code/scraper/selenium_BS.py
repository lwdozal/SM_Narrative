# selenium_BS second try

# import required modules
from selenium import webdriver
import time, urllib.request
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


import pandas as pd



#get URl path
def path():
    global driver

    driver = webdriver.Chrome()
	# return driver


# go to page url
def url_name(url):
	# global driver
	# driver = webdriver.Chrome()
	driver.get(url)
    # webdriver will wait for 4 sec before throwing a
    # NoSuchElement exception so that the element
    # is detected and not skipped.
	time.sleep(4)


def login(username, password):
    # log_but = driver.find_element("css selector","L3NKy")
#taken from other source
######## Connect to instagram
    driver.get("https://www.instagram.com/")
    # driver.maximize_window() #get full page

    ####### Log in to Instagram
    time.sleep(5) #you're not a robot wait 5 seconds to run the next code script
    username=driver.find_element("css selector","input[name='username']")
    password=driver.find_element("css selector","input[name='password']")
    username.clear() #clear default text in input area
    password.clear() #clear default text in input area
    username.send_keys("lwddissertation")
    password.send_keys("Sandia005!")
    login = driver.find_element("css selector","button[type='submit']").click()

# skip pop-ups
    time.sleep(10)
  

def not_now():
#save your login info?
	time.sleep(10)
	notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not now')]").click()
	#turn on notif
	time.sleep(10)
	notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()


def get_image(url):
      #maybe look into how you can get them individually?
      url_name(url)
      image = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, '_aagv')))

def get_metadata():
      main_comment = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mount_0_0_D1"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1')))
      # XPATH: //*[@id="mount_0_0_D1"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1
      print("main_comment", main_comment)
    #   time = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'time')))
      time = driver.find_element(By.XPATH, '//*[@id="mount_0_0_D1"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1')
      print("time", time)
      # XPATH //*[@id="mount_0_0_D1"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[4]/div/a/span/time
      number_comments = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mount_0_0_Xn"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[3]/a/span')))
      print("number_comments", number_comments)
      likes = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, '<span class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj" style="line-height: 18px;"><span class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs">283</span> likes</span>')))
      print("likes", likes) 

def save_metadata():
      return None


	# main_comment = driver.find_element(By.CLASS_NAME, '_ap3a _aaco _aacu _aacx _aad7 _aade')  #'//*[@id="mount_0_0_D1"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1')
	# main_comment = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mount_0_0_D1"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1')))
	#   main_comment = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
    
'''
For instance, consider this page source:

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
</html>
The form elements can be located like this:

login_form = driver.find_element(By.XPATH, "/html/body/form[1]")
login_form = driver.find_element(By.XPATH, "//form[1]")
login_form = driver.find_element(By.XPATH, "//form[@id='loginForm']")

Absolute path (would break if the HTML was changed only slightly)

First form element in the HTML

The form element with attribute id set to loginForm

The username element can be located like this:

username = driver.find_element(By.XPATH, "//form[input/@name='username']")
username = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[1]")
username = driver.find_element(By.XPATH, "//input[@name='username']")

First form element with an input child element with name set to username
First input child element of the form element with attribute id set to loginForm
First input element with attribute name set to username

The “Clear” button element can be located like this:

clear_button = driver.find_element(By.XPATH, "//input[@name='continue'][@type='button']")
clear_button = driver.find_element(By.XPATH, "//form[@id='loginForm']/input[4]")

Input with attribute name set to continue and attribute type set to button
Fourth input child element of the form element with attribute id set to loginForm

XPATH comment: 
//*[@id="mount_0_0_D1"][@class = "_ap3a _aaco _aacu _aacx _aad7 _aade"]
/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1/text()
//*[@id="mount_0_0_9Q"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1/text()

//*[@id="mount_0_0_9Q"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1/text()

Class comment:
x12nagc
or
_ap3a _aaco _aacu _aacx _aad7 _aade
<h1 class="_ap3a _aaco _aacu _aacx _aad7 _aade" dir="auto">In Wädenswil ZH wurde am 15. Januar 2024 eine 56-jährige Frau von einen Mann getötet. <br><br>Das ist der 2. Feminizid in der Schweiz in diesem Jahr von dem wir wissen. <br><br>Nehmt ihr uns eine, antworten wir alle!<br><br>Nächste Sitzung:<br>17.1.24<br>19:00<br>Kasama<br><br>Nächste Kundgebung:<br>03.02.24<br>(genaue Uhrzeit wird bekanntgegeben)<br>Ni-una-menos-Platz<br><br><a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/niunamenos/" role="link" tabindex="0">#niunamenos</a></h1>

XPATH hashtag:
//*[@id="mount_0_0_D1"][@class = "_ap3a _aaco _aacu _aacx _aad7 _aade"]/a[1][@tabindex = "0"]



'''

def cGPTtry():
      
    #   get into the html
    html = driver.page_source
    print(html)
    soup = bs(html, 'html.parser')

      #find post caption
    post_caption = soup.find("div", class_ = "X12Pu").text
    print(post_caption)

    #   get commetns
    comment_section = driver.find_elements(By.CSS_SELECTOR, "ul.Mr508")
    #   all_comments = comment_section.find_elements_by_css_selector("ul > div > li")
    comment_number = 0
    comments = []
    for comment in comment_section:
        commenter_username = comment.find_element(By.CSS_SELECTOR, "h3").text
        print("commenter_username", commenter_username)
        comment_text = comment.find_element(By.CSS_SELECTOR, "span").text
        print("comment_text"), comment_text
        comment_hashtags = comment.find_element(By.CSS_SELECTOR, "a" )
        print("comment_hashtags", comment_hashtags)
        comment_number +=1
        comments.append({"comment_number": comment_number,"username": commenter_username, "comment": comment_text, "hashtags": comment_hashtags})

    print("comments", comments)
   


#Amazon testing

def amazonxpath_shortcuts():
      # assign your website to scrape
    driver = webdriver.Chrome()
    web = 'https://www.amazon.com'
    web2 = 'https://www.amazon.com/s?k=record+player&language=en_US&crid=11M6RHNNPRMJW&sprefix=record+player%2Caps%2C164&ref=nb_sb_ss_ts-doa-p_1_13'
    driver.get(web)
    driver.implicitly_wait(10)
    keyword = "record player"
    search = driver.find_element(By.ID, 'twotabsearchtextbox')
    search.send_keys(keyword)
# click search button
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')
    search_button.click()

    driver.implicitly_wait(5)

    account = []
    comment = []
    numLikes = []
    data = []
    numComments = []
    geoLoc = []

    product_name = []
    product_link = []
    product_price = []
#amzn1.asin.1.
# class="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16" data-component-id="12" data-cel-widget="search_result_2"><div class="sg-col-inner"><div cel_widget_id="MAIN-SEARCH_RESULTS-3" class="s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1" data-csa-c-pos="1" data-csa-c-item-id="amzn1.asin.1.B0BNVNVQJ4" data-csa-op-log-render="" data-csa-c-type="item" data-csa-c-id="h77vvr-k4r3ly-xry1ax-27swpg" data-cel-widget="MAIN-SEARCH_RESULTS-3">

    
    # items = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, '"sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16"')))
    items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
    for item in items:
        name = item.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]')
        product_name.append(name.text)
        #get link to item page
        link = item.find_element(By.XPATH, './/a[@class = "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
        product_link.append(link.text)
        #get item price
        whole_price = item.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
        fraction_price = item.find_elements(By.XPATH,'.//span[@class="a-price-fraction"]')
        if whole_price != [] and fraction_price != []:
            price = '.'.join([whole_price[0].text, fraction_price[0].text])
        else:
            price = 0
        product_price.append(price)

    driver.quit()

    print("product_name",product_name)
    print("product_link",product_link)
    dict = {'product_name':product_name, 'product_price': product_price, 'product_link': product_link}
    product_info = pd.DataFrame(dict)
    print(product_info)
    product_info.to_csv('amazon_teSt.csv', header=False)




def url_info(df):
    driver = webdriver.Chrome()

    wait10 = WebDriverWait(driver, 10)
    posts = df["0"].tolist()
    print("posts list", posts)

    accounts = []
    comments = []
    likes = []
    dates = []
    img_acessability = []
    images = []
    img_source = []
    url = []
    post_id = []

    

    for idx, post in enumerate(posts):
        print("post", post)
        driver.get(post)
        print("driver.current_url", driver.current_url)
        shortcode = post.split("/")[-2 ]
        print("shortcode", shortcode)
        post_id.append(shortcode)
        wait10




        # get the 'main' page content to make our lives better
        page_content = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > main")))
        print("page_content", page_content)

        s1likes = bs(page_content.get_attribute('innerHTML'), 'html.parser')
        print("s1likes", s1likes)
        #get number of followers
        num_likes = s1likes.findAll('span', {'class': 'xdj266r'})
        print("num_likes", num_likes)




        # account = current_url.find_element(By.XPATH, '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"]').get_attribute('span')
        account = driver.find_element(By.CSS_SELECTOR, '#mount_0_0_ee > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x4h1yfo > div > div.x5yr21d.xw2csxc.x1odjw0f.x1n2onr6 > div > div:nth-child(1) > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > span > div > div > span:nth-child(1) > div > a > div > div > span')
       
    #<span class="_ap3a _aaco _aacw _aacx _aad7 _aade" dir="auto">street_style_voyage</span>
        accounts.append(account)
        wait10
        # comment = driver.find_element(By.XPATH, '//span[contains(@class, "x193iq5w")]')
        comment = driver.find_element(By.XPATH, '//*[@id="mount_0_0_ee"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/span/div/span')
        # comment = driver.find_element(By.XPATH, '//span[@class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj"]')
        comments.append(comment)
        wait10
        like = driver.find_element(By.XPATH, '//span[contains(@class, "html-span xdj266r")]')
        likes.append(like)
        wait10
        time = driver.find_element(By.XPATH, '//time[@class= "x1p4m5qa"]').get_attribute("datetime")
        dates.append(time)
        download_url = driver.find_element(By.CSS_SELECTOR, "img[style='object-fit: cover;']").get_attribute('src')
        print("download_url: ", download_url)
        url.append(download_url)
        wait10
        jpg = urllib.request.urlretrieve( download_url, '{}.jpg'.format(shortcode))
        print("jpg path", jpg)
        images.append(jpg[0])

    

        
        carousel_src = []
        if driver.find_element(By.XPATH, '//div[@role="button"]') is not None:
            driver.find_element(By.XPATH, '//div[@role="button"]').click()
            img_alt = driver.find_element(By.XPATH, '//div[@class= "_aagv"]/img').get_attribute("alt")
            driver.find_element(By.CSS_SELECTOR, '#mount_0_0_ee > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div.x6s0dn4.x78zum5.xdt5ytf.xdj266r.xkrivgy.xat24cr.x1gryazu.x1n2onr6.xh8yej3 > div > div.x6s0dn4.x1dqoszc.xu3j5b3.xm81vs4.x78zum5.x1iyjqo2.x1tjbqro > div > div > div > div > div > div > div._aamn > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x10l6tqk.x1ey2m1c.x13vifvy.x17qophe.xds687c.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div > div > ul > li:nth-child(2) > div > div > div > div > div._aagv > img').get_attribute('alt')
    
            img_acessability.append(img_alt)
            img_src = driver.find_element(By.XPATH, '//div[@class= "_aagv"]/img').get_attribute("src")
            carousel_src.append(img_src)

        else:
            img_alt = driver.find_element(By.XPATH, '//div[@class= "_aagv"]/img').get_attribute("alt")
            img_acessability.append(img_alt)
            img_src = driver.find_element(By.XPATH, '//div[@class= "_aagv"]/img').get_attribute("src")
            img_source.append(img_src)
        
        img_source.append(carousel_src)
    driver.quit()



    dict = {'post_id':post_id,'Urls':url,'Accounts':accounts, 'comments': comments, 'likes':likes, 'dates': dates, 'img_acessability': img_acessability, "jpg": images, "img_source":img_source, }
    product_info = pd.DataFrame(dict)
    print(product_info)
    product_info.to_csv('insta_test.csv')




    #account element
    #<span class="_ap3a _aaco _aacw _aacx _aad7 _aade" dir="auto">street_style_voyage</span>
    #<span class="_ap3a _aaco _aacw _aacx _aad7 _aade" dir="auto">street_style_voyage</span>

    #Comment
    # <span class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj" style="line-height: 18px;">We've captured some latest looks of <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/bellahadid/" role="link" tabindex="0">@bellahadid</a><br>All styled by <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/mollyddickson/" role="link" tabindex="0">@mollyddickson</a><br>Which look is your fave? (1-4)<br>1. Vintage corset dress <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/roberto_cavalli/" role="link" tabindex="0">@roberto_cavalli</a><br>2. Vintage <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/ysl/" role="link" tabindex="0">@ysl</a> floral dress from <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/tabvintage/" role="link" tabindex="0">@tabvintage</a><br>3. <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/gucci/" role="link" tabindex="0">@gucci</a> blazer with mini skirt and loafers<br>4. <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/ferragamo/" role="link" tabindex="0">@ferragamo</a> jacket and capri pants<br><br><a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/bellahadid/" role="link" tabindex="0">#bellahadid</a><br>.<br>.<br>.<br>.<br>.<br><a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/vintagetrends/" role="link" tabindex="0">#vintagetrends</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/streetstylevoyage/" role="link" tabindex="0">#streetstylevoyage</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/vintagedress/" role="link" tabindex="0">#vintagedress</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/vintageysl/" role="link" tabindex="0">#vintageysl</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/robertocavalli/" role="link" tabindex="0">#robertocavalli</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/streetstyle/" role="link" tabindex="0">#streetstyle</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/streetfashion/" role="link" tabindex="0">#streetfashion</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/celebstyle/" role="link" tabindex="0">#celebstyle</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/gucci/" role="link" tabindex="0">#gucci</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/minidress/" role="link" tabindex="0">#minidress</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/chic/" role="link" tabindex="0">#chic</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/bellahadidstyle/" role="link" tabindex="0">#bellahadidstyle</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/fashiontrend/" role="link" tabindex="0">#fashiontrend</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/ootdfashion/" role="link" tabindex="0">#ootdfashion</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/floraldress/" role="link" tabindex="0">#floraldress</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/corsetdress/" role="link" tabindex="0">#corsetdress</a> <a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz  _aa9_ _a6hd" href="/explore/tags/corsetstyle/" role="link" tabindex="0">#corsetstyle</a></span>

    #likes
    #<span class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs">1,109</span>
    
    #Time
    # <time class="x1p4m5qa" datetime="2024-05-04T17:32:31.000Z" title="May 4, 2024">2 days ago</time>

    #Button
    # if button exists click the button and get the new image
    # <div class=" _9zm2"></div> .click()

    #Image
    # <div class="_aagv" style="padding-bottom: 123.241%;"><img alt="Photo shared by Street_style_voyage on May 04, 2024 tagging @bellahadid, and @maisonhjewels. May be an image of 1 person, hair, makeup and dress." crossorigin="anonymous" src="https://scontent.cdninstagram.com/v/t51.29350-15/441465252_792989706377389_6026880839310602566_n.webp?stp=dst-jpg_e35&amp;efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEzMzEuc2RyLmYyOTM1MCJ9&amp;_nc_ht=scontent.cdninstagram.com&amp;_nc_cat=101&amp;_nc_ohc=GxRc6rk8hAEQ7kNvgFTB6km&amp;edm=APs17CUBAAAA&amp;ccb=7-5&amp;ig_cache_key=MzM2MDY3NzA4Nzg0NDE2NjM2Nw%3D%3D.2-ccb7-5&amp;oh=00_AfATop3Fsk_oxZZUPBCjH_m6VdbKKhBRsK5fbN2ACp2tew&amp;oe=663DA497&amp;_nc_sid=10d13b" class="x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3" style="object-fit: cover;"></div>
    return None

if __name__ == "__main__":
     amazonxpath_shortcuts()




