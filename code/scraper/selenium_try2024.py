'''
Laura 
data collection 2024
another attempt to use selenium after instaloader didn't work
'''

# pulled from  https://www.geeksforgeeks.org/download-instagram-posts-using-python-selenium-module/


# import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time, urllib.request
import sys
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
import os

import pandas as pd
from csv import writer



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


def login(username, password, url):
    # log_but = driver.find_element("css selector","L3NKy")
#taken from other source
######## Connect to instagram
    # driver.get("https://www.instagram.com/")
    # driver.maximize_window() #get full page
    driver.get(url)

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

# function to get first post
def first_post():
	time.sleep(3)
	# pic = driver.find_element("css selector","_aagu").click()
	# pic = driver.find_element(By.CLASS_NAME,"_aagv").click() 
	# pic = driver.find_element(By.CSS_SELECTOR,'span[class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"]').click()
	pic = driver.find_element(By.CSS_SELECTOR,'div[class="_aagw"]').click()
	print("first_post pic:",pic)
	print("first_post url", driver.current_url)
	# pic = driver.find_element(By.CLASS_NAME,"_aagw") #.click()
	# pic = driver.find_element(By.CLASS_NAME,"kIKUG").click()
	# pic = driver.find_element(By.CLASS_NAME, "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd").get_attribute('href')
	
	
	# popup_url = driver.find_element(By.TAG_NAME, "a").get_attribute('href')
	# popup_url = driver.find_element(By.XPATH, './/a').get_attribute('onclick').split('(')[1].split(')')[0]
	# print("popup_url:", popup_url) 

	time.sleep(2)
	return driver.current_url

# function to get next post
def next_post():
	try:
		# nex = driver.find_element(By.NAME,"coreSpriteRightPaginationArrow")
		nex = driver.find_element("css selector","button[type='Next']").click()
		return nex
	except selenium.common.exceptions.NoSuchElementException:
		return 0

# Function to save content of the current post
def save_content(class_name,img_name):
	time.sleep(0.5)
	
	pic = driver.find_element(By.XPATH,class_name) #CLASS_NAME
	print("pic in save_content", pic)
	# try:
	# 	pic = driver.find_element(By.XPATH,class_name) #CLASS_NAME
	# 	# pic = driver.find_element(By.XPATH, ("//img alt[@]"))
	# 	print("pic:", pic)


	# except selenium.common.exceptions.NoSuchElementException:
	# 	print("Either This user has no images or you haven't followed this user or something went wrong")
	# 	return
	
	# img_src = pic.get_attribute('img alt')
	# print("img src", img_src)
	html = pic.get_attribute('innerHTML')
	print("html", html)
	soup = bs(html,'html.parser')
	print("soup", soup)
	link = soup.find('video')
	print("link video", link)
	
	if link:
		link = link['src']
		print("Link src:", link)
	else:
		# link = soup.find('img alt')['src']
		link = pic
		print("Link img:", link)
	response = requests.get(link)
	
	with open(img_name, 'wb') as f:
		f.write(response.content)
	
	time.sleep(0.9)

def img_src_alt(img_cnt):
	WebDriverWait(driver, 3)
	first_image = driver.find_element(By.CSS_SELECTOR,"div[class='_aagv']").get_attribute("src") #img
	print("first_image", first_image)
	first_image_alt = driver.find_element(By.CSS_SELECTOR,"div[class='_aagv']").get_attribute("alt")
	print("first_image_alt", first_image_alt)

	if img_cnt <= 1:
		comment = driver.find_element(By.CSS_SELECTOR, 'h1[class = "_ap3a _aaco _aacu _aacx _aad7 _aade"]')
		print("Comment:", comment)
		account = driver.find_element(By.CSS_SELECTOR, "a[class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp xqnirrm xj34u2y x568u83']").text
		print("account",account)
		likes = driver.find_element(By.CSS_SELECTOR,"span[class='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs']")
		print("likes",likes)
		time = driver.find_element(By.CSS_SELECTOR,"time[class='x1p4m5qa']").get_attribute("datetime")
		print("DateTime:", time)
		# tags = driver.find_elements(By.CSS_SELECTOR, 'h1[class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd]')
		
		# l = elem.get_attribute('innerHTML')
		# html = bs(l,'html.parser')
		# tags = html.find_all('a')
		# print("tags", tags)


	return (first_image, first_image_alt, account, likes, comment, time)


def vid_src_alt(img_cnt):
	WebDriverWait(driver, 3)

	# vid_src = driver.find_element(By.CSS_SELECTOR, 'div[class = "x5yr21d x1uhb9sk xh8yej3"]').get_attribute('src')
	vid_src = driver.find_element(By.CSS_SELECTOR, 'video[class= "x1lliihq x5yr21d xh8yej3"]').get_attribute('src')
	print("vid_src", vid_src)


	if img_cnt <= 1:
		comment = driver.find_element(By.CSS_SELECTOR, 'h1[class= "_ap3a _aaco _aacu _aacx _aad7 _aade"]').text
		print("Comment", comment)
		account = driver.find_element(By.CSS_SELECTOR, "a[class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp xqnirrm xj34u2y x568u83']").text
		print("account",account)
		likes = driver.find_element(By.CSS_SELECTOR,"span[class='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs']").text
		print("likes",likes)
		time = driver.find_element(By.CSS_SELECTOR,"time[class='x1p4m5qa']").get_attribute("datetime")
		print("DateTime:", time)
		# tags = driver.find_elements(By.CSS_SELECTOR, 'h1[class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd]')

		
		# l = elem.get_attribute('innerHTML')
		# html = bs(l,'html.parser')
		# tags = html.find_all('a')
		# print("tags", tags)
	
	return (vid_src, account, likes, comment, time)

# Function to save multiple posts
# def save_multiple(img_name,elem,last_img_flag = False):
	# time.sleep(3)
	# l = elem.get_attribute('innerHTML')
	# html = bs(l,'html.parser')
	# biglist = html.find_all('ul')
	# print("biglist", biglist)
	# biglist = biglist[0]
	# list_images = biglist.find('li')
	# if last_img_flag:
	# 	user_image = list_images[-1]
	# else:
	# 	user_image = list_images[(len(list_images)//2)]
	# video = user_image.find('video')
	# if video:
	# 	link = video['src']
	# else:
	# 	link = user_image.find('img alt')['src']
	# response = requests.get(link)
	# with open(img_name, 'wb') as f:
	# 	f.write(response.content)
 
def save_PostContent(hashtag, img_name):
	WebDriverWait(driver, 3)

	img_url = driver.current_url
	img_call = img_url.split('/')[-2]
	print(img_call)

	img_src = []
	img__alt = []
	accounts = []
	video_src = []
	post_like = []
	comments = []
	datetime = []
	img_file = []

	if driver.find_element(By.CSS_SELECTOR,"svg[aria-label='Carousel']") is not None:
		img_cnt = 1
		if driver.find_element(By.CSS_SELECTOR, 'div[class = "x5yr21d x1uhb9sk xh8yej3"]') is not None:
			vid_src = vid_src_alt(img_cnt)[0]
			video_src.append(vid_src)
			# with open(hashtag + '/cnt_'+str(img_cnt)+img_call, 'wb') as f:
			# 	f.write(vid_src)
			img_cnt +=1

			# driver.find_element(By.CSS_SELECTOR,"svg[aria-label='Carousel']").click()
			driver.find_element(By.CSS_SELECTOR,"div[class='x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy x1ypdohk']").click()
		else:
			src, alt, account, likes, comment, time = img_src_alt(img_cnt)
			img_cnt +=1
			img_src.append(src)
			jpg = urllib.request.urlretrieve(img_src, '{}.jpg'.format(img_call))
			print("jpg path", jpg)
			img_file.append(jpg)
			with open(hashtag + '/cnt_'+str(img_cnt)+img_call, 'wb') as f:
				f.write(jpg)
			img__alt.append(alt)
			accounts.append(account)
			post_like.append(likes)
			comments.append(comment)
			datetime.append(time)
			# tags.append(tag)

			# driver.find_element(By.CSS_SELECTOR,"svg[aria-label='Carousel']").click()
			driver.find_element(By.CSS_SELECTOR,"div[class='x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy x1ypdohk']").click()
	else:
		img_cnt = 1
		if driver.find_element(By.CSS_SELECTOR, 'div[class = "x5yr21d x1uhb9sk xh8yej3"]') is not None:
			vid_src, account, likes, comment, time = vid_src_alt(img_cnt)
			video_src.append(vid_src)
			mp4 = urllib.request.urlretrieve(img_src, '{}.mp4'.format(img_call))
			print("mp4 path", mp4)
			img_file.append(mp4)
			with open(hashtag + '/cnt_'+str(img_cnt)+img_call, 'wb') as f:
				f.write(mp4)
			accounts.append(account)
			post_like.append(likes)
			comments.append(comment)
			datetime.append(time)
			# tags.append(tag)
		else:
			src1, alt1, account, likes, comment, time = img_src_alt(img_cnt)
			img_src.append(src1)
			jpg = urllib.request.urlretrieve(img_src, '{}.jpg'.format(img_call))
			print("jpg path", jpg)
			img_file.append(jpg)
			with open(hashtag + '/cnt_'+str(img_cnt)+img_call, 'wb') as f:
				f.write(jpg)
			img__alt.append(alt1)
			accounts.append(account)
			post_like.append(likes)
			comments.append(comment)
			datetime.append(time)
			# tags.append(tag)
	
	#create data dictionary to save content as dataframe
 	# new_content = {"URL":driver.current_url, "img_name":img_name, "img_src":img_src, "img__alt":img__alt, "accounts":accounts, "like_count":post_like, "initial_comment": comments, "datetime": datetime, "comment_tags":tags, "video_src":video_src}
	# df = pd.DataFrame(new_content)
 
    #create a series for each list to concat them all together
	# this is done because the lists are different lengths
	s1 = pd.Series(driver.current_url, name='URL')
	s2 = pd.Series(img_name, name='img_name')
	s3 = pd.Series(img_src, name='img_src')
	s4 = pd.Series(img__alt, name='img__alt')
	s5 = pd.Series(accounts, name='accounts')
	s6 = pd.Series(post_like, name='like_count')
	s7 = pd.Series(comments, name='initial_comment')
	s8 = pd.Series(datetime, name='datetime')
	s9 = pd.Series(img_file, name='post_file')
	s10 = pd.Series(video_src, name='video_src')
	s11 = pd.Series(hashtag + '/'+img_call, name='file_path')
	df = pd.concat([s1,s2, s3,s4,s5,s6,s7,s8,s9,s10,s11], axis=1)
	#append df to existing csv (create one before running)
	df.to_csv('content.csv', mode='a', index=True, header=False)
	print("Data appended successfully.")

	# with open('content.csv', 'a') as f:
	# 	writer_object = writer(f)
	# 	writer_object.writerow(new_content)
	# 	f.close()



# function to check if the post is nested
def nested_check():

	try:
		time.sleep(1)
		# nes_nex = driver.find_element(By.CSS_SELECTOR,"button[type='Next']")
		nes_nex = driver.find_element(By.CSS_SELECTOR,"svg[aria-label='Carousel']")
		print(nes_nex)
		return nes_nex
	
	except selenium.common.exceptions.NoSuchElementException:
		return 0


def download_allposts(hashtag):

	# open First Post
	# print(" URL:", url)
	first_post()
    
	# user_name = url.split('/')[-1]
	# ht = url.split('/')[-1]
	
	print("New URL:", driver.current_url)
	#make sure you're in the correct folder anytime
	parent_path = os.getcwd()

	# check if folder corresponding to hashtag exists in your dir
	if(os.path.isdir(hashtag) == False):
		# Create folder  
		os.mkdir(str(hashtag))
	# Check if Posts contains multiple images or videos
	# multiple_images = nested_check()

	if nested_check() != 0:
		print("Post has multiple images")
		nescheck = nested_check()
		count_img = 1
		images = []
		
		while nescheck:
			WebDriverWait(driver, 1.5)
			elem_img = driver.find_element(By.CLASS_NAME,'_aagv').get_attribute('src') #_aagw
			print("elem_img", elem_img)
			images.append(elem_img)  #added this to save the image
			# save_content() #added this to save the image

			# Function to save nested images
            # save_multiple(hashtag +'/'+'image'+str(count_img), elem_img)
			count_img += 1
			save_PostContent(hashtag, hashtag +'_post_'+str(count_img))
			nescheck.click()
			# nescheck = nested_check()

		# pass last_img_flag True
		# save_multiple(hashtag +'/'+'content1.' +
		# 			str(count_img), elem_img, last_img_flag=1)


	else:
		# this goes to the function above, which uses BS to look through the html and find the source image and other things
        # making my own function here for testing
		# save_content('_aagv', hashtag+'/'+'content1') #_aagw
		elem_img = driver.find_element(By.CLASS_NAME,'_aagv').get_attribute('src')
		save_PostContent(hashtag, hashtag +'_post_'+str(count_img))
		# with open(ht+".csv", 'wb') as f:
		# 	f.write()
	c = 2
	
	while(True):
		next_el = next_post()
		
		if next_el != False:
			next_el.click()
			time.sleep(3)
			
			try:
				multiple_images = nested_check()
				
				if multiple_images:
					nescheck = multiple_images
					count_img = 0
					
					while nescheck:
						elem_img = driver.find_element(By.CLASS_NAME,'rQDP3')
						save_PostContent(hashtag, hashtag+'/'+'_post_' +
									str(c)+'_imgage'+str(count_img))
						count_img += 1
						nescheck.click()
						nescheck = nested_check()
					save_PostContent(hashtag, hashtag+'_image'+str(c))

					# save_content(hashtag+'/'+'content'+str(c) +
					# 			'.'+str(count_img), elem_img, 1)
				else:
					# save_content('_97aPb', hashtag+'/'+'content'+str(c))
					save_PostContent(hashtag, hashtag+'_image'+str(c))
			
			except selenium.common.exceptions.NoSuchElementException:
				print("finished")
				return
		
		else:
			break
		
		c += 1
		driver.close()

########
#Test from https://medium.com/analytics-vidhya/web-scraping-instagram-with-selenium-python-b8e77af32ad4
# https://medium.com/@srujana.rao2/scraping-instagram-with-python-using-selenium-and-beautiful-soup-8b72c186a058
# here we can download images, just not their comments or information just yet.

# support for extra info: 
# https://www.youtube.com/watch?v=r5sLtPl_rAc
# https://github.com/MohammadHosein21/Instagram-Bot-with-selenium-and-beautifulsoup/blob/main/Bot.py
# https://www.geeksforgeeks.org/download-instagram-posts-using-python-selenium-module/
# Instaloader: https://python.plainenglish.io/scrape-everythings-from-instagram-using-python-39b5a8baf2e5

########### 


## try to get posts
def post_urls(hashtag):
	posts = []
	links = driver.find_elements(By.TAG_NAME, "a")
	for link in links:
		post = link.get_attribute('href')
		if '/p/' in post:
			posts.append(post)
	print(posts)
	return posts

def scroll(hashtag):
	time.sleep(10)
	scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown = document.body.scrollHeight;return scrolldown;")
	match = False
	postUrls = []
	postUrls.append(post_urls(hashtag))
	while(match == False):
		last_count = scrolldown
		# print("postUrls", postUrls)
		time.sleep(2)
		scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
		if last_count == scrolldown:
			match = True
	driver.close()
	postUrls = pd.DataFrame(postUrls)
	postUrls.to_csv(hashtag + 'post_urls.csv', index=False, header=False)


def post_metadata():
	# main_comment = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1/text()')))
	# main_comment = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
    main_comment = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1')))
    print("main_comment", main_comment)
	# time = driver.find_element(By.XPATH, '//*[@id="mount_0_0_D1"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[2]/div/span[2]/div/h1')
	# time = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'time')))
	# print("time", time)
    number_comments = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mount_0_0_Xn"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/div[3]/div/div[3]/a/span')))
	# print("number_comments", number_comments)
    likes = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, '<span class="x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj" style="line-height: 18px;"><span class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs">283</span> likes</span>')))
	# print("likes", likes) 
 




def post_info(df, hashtag):
	df['img_urls'] = ""
	df['img_jpg'] = ""
	df['vid_mp4'] = ""

	print("made it to post_info()")
	# os.mkdir(hashtag) 
	posts = df[0].tolist()
	print("posts list", posts)
	# posts = df.tolist()
	# download_url = ''
	for idx, post in enumerate(posts):
		print("post", post)
		driver.get(post)
		print("driver.current_url", driver.current_url)
		# shortcode = driver.current_url
		shortcode = post.split("/")[-2 ]
		# shortcode = driver.current_url.split("/")[-2]
		print("shortcode", shortcode)
		
		# cGPTtry()
		# post_metadata()
		
		time.sleep(3)
		if driver.find_element(By.CSS_SELECTOR, "img[style='object-fit: cover;']") is not None:
			print("we have an image")
			time.sleep(3)
			download_url = driver.find_element(By.CSS_SELECTOR, "img[style='object-fit: cover;']").get_attribute('src')
			print("download_url: ", download_url)
			time.sleep(3)
			jpg = urllib.request.urlretrieve( download_url, '{}.jpg'.format(shortcode))
			print("jpg path", jpg)
			time.sleep(3)
			comment = driver.find_element(By.XPATH, '//span[contains(@class, "x193iq5w")]')
			# find_element(By.XPATH,  '//*[@id="mount_0_0_l9"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/span/div/span')
			# comment = driver.find_element(By.CSS_SELECTOR, "span[style='line-height: 18px;']").get_attribute('$0')
			print("comment", comment)
			# hashtags_used = driver.find_element(By.CSS_SELECTOR, "span[style='line-height: 18px;']").get_attribute('a')
			# print("hashtags_used", hashtags_used)


			df.loc[df.index[idx], 'img_urls'] = download_url
			df.loc[df.index[idx], 'comments'] = comment
			df.loc[df.index[idx], 'img_jpg'] = jpg[0]
			df.loc[df.index[idx], 'vid_mp4'] = ""

			# article = driver.find_elements(By.XPATH, '//div[@id="react-root"]//article')  #[-1] 
			# print("article", article)
			# comments = driver.find_elements(By.XPATH, './div/section[2]/following-sibling::div/ul/ul')
			# print("comments", comments)

			# image_count_in_post = 0
			# while article.find_element(By.XPATH, './/*[contains(@class, "coreSpriteRightChevron")]') is not None:
			# 	image_count_in_post += 1
			# 	next_image_arrow = article.find_element(By.XPATH, './/*[contains(@class, "coreSpriteRightChevron")]')
			# 	next_button = driver.find_element(By.XPATH, '//a[contains(@class, "coreSpriteRightPaginationArrow")]')
			# 	urllib.request.urlretrieve( next_button, '{}' +image_count_in_post +'.jpg'.format(shortcode))

			# pd.concat([df['img_urls'].reset_index(drop = True), download_url])
			# pd.concat([df['img_jpg'].reset_index(drop = True), jpg])
			# pd.concat([df['vid_mp4'].reset_index(drop = True), ""])

		else:
			download_url = driver.find_element(By.CSS_SELECTOR,"video[type='video/mp4']").get_attribute('src')
			print("we have a video")
			vid = urllib.request.urlretrieve(download_url, '{}.mp4'.format(shortcode))
			print("vid path", vid)
			# pd.concat([df['img_urls'].reset_index(drop = True), download_url])
			# pd.concat([df['vid_mp4'].reset_index(drop = True), vid])
			# pd.concat([df['img_jpg'].reset_index(drop = True), ""])
			df.loc[df.index[idx], 'img_urls'] = download_url
			df.loc[df.index[idx], 'img_jpg'] = ""
			df.loc[df.index[idx], 'vid_mp4'] = vid[0]
		time.sleep(5)
	# print(posts)
	print("df: ", df)	
	df.to_csv(hashtag + '/_info.csv')

# Do something similar for the post comment, account holder etc




if __name__ == "__main__":
    # # driver = webdriver.Chrome() #PATH
	'''
	if needed:
	instaloader; https://proxyscrape.com/blog/how-to-scrape-instagram-using-python
	instascrape - https://github.com/chris-greening/instascrape ; https://dev.to/chrisgreening/scraping-an-instagram-location-tag-with-instascrape-554f
	scrapify - https://scrapfly.io/docs/sdk/python
	'''
	path()
	username = "lwddissertation"
	password = "Sandia005!"
	# hashtag = "femicidioemergencianacional" 	
	hashtag = "niunamenos"

    # url = 'https://instagram.com//explore/tags/' + hashtag + "/" #assign urlurl = 'https://www.instagram.com/explore/search/keyword/?q=' + hashtag
	url = 'https://www.instagram.com/explore/search/keyword/?q=' + hashtag


    #### works?
	# url_name(url)
	# login(username, password, url)
	# scroll(hashtag)
	# testlinks = post_urls(hashtag)
    ####
	login(username, password, url)
	download_allposts(hashtag)
	# url_name(url)
	# scroll()
    #download_allposts(hashtag)
	# # testInfo = post_urls(hashtag)
	# testInfo = pd.read_csv('femicidioemergencianacionalpost_urls.csv')
	# testInfo = pd.read_csv('niunamenospost_urls.csv', header=None).head()
	# print(testInfo)
	# post_info(testInfo, hashtag)


    # TEST
	# import instaloader
	# L = instaloader.Instaloader()
	# profile_femcdioMX = instaloader.Profile.from_username(L.context, "feminicidio_mexico")
	# [L.download_post(prof, target=profile_femcdioMX.username) for prof in profile_femcdioMX.get_posts()]