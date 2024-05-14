




# import required modules
from selenium import webdriver
import time, urllib.request
from bs4 import BeautifulSoup as bs
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests


import pandas as pd
import os


# import PIL  
# from PIL import Image  


#get URl path
def path():
    global driver

    driver = webdriver.Chrome()
	# return driver


def login(username, password, url):
    global driver
    driver = webdriver.Chrome()

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
	

# function to get first post
def first_post():
	time.sleep(3)
	#div[class="_aagw"] is the correct version, the second pic variable helps when you've been tesing instagram too many times
	pic = driver.find_element(By.CSS_SELECTOR,'div[class="_aagw"]').click()
	# pic = driver.find_element(By.CSS_SELECTOR,'span[class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"]').click()
	print("opened first post")
	# print("first_post pic:",pic)
	print("first_post url", driver.current_url)

	time.sleep(2)
	return driver.current_url

# function to get next post
def next_post():
	time.sleep(1.5)
	try:
		# nex = driver.find_element(By.NAME,"coreSpriteRightPaginationArrow")
		# nex = driver.find_element("css selector","button[type='Next']").click()

		# nex = driver.find_element(By.CSS_SELECTOR,"button[class='_abl-'] > div[class='_abm0']")
		# nex = driver.find_element(By.XPATH,"_abm0")
		# nex = driver.find_element("css selector","svg[class='x1lliihq x1n2onr6 x175jnsf']")

		# nex = driver.find_element(By.CSS_SELECTOR,"div[class='_abm0']")
		nex = driver.find_element(By.CSS_SELECTOR,"div[class='_abm0'] > span[style='display: inline-block; transform: rotate(90deg);'] > svg > path[d='M21 17.502a.997.997 0 0 1-.707-.293L12 8.913l-8.293 8.296a1 1 0 1 1-1.414-1.414l9-9.004a1.03 1.03 0 0 1 1.414 0l9 9.004A1 1 0 0 1 21 17.502Z']")
		# nex = driver.find_element(By.CSS_SELECTOR,"*[class='x1lliihq x1n2onr6 x175jnsf']")
		
		return nex
	except selenium.common.exceptions.NoSuchElementException:
		return 0
	

# function to check if the post is nested
def nested_check():

	try:
		time.sleep(1)
		nes_nex = driver.find_element(By.CSS_SELECTOR,"div[class=' _9zm2']")
		# nes_nex = driver.find_element(By.CSS_SELECTOR,"div[class='x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy x1ypdohk']")
		print("Nested Post")
		return nes_nex
	
	except selenium.common.exceptions.NoSuchElementException:
		return 0
	
def video_check():
	print("checking for video")
	try:
		vid = driver.find_element(By.CSS_SELECTOR, 'div[class = "x5yr21d x1uhb9sk xh8yej3"]')
		return vid
	except selenium.common.exceptions.NoSuchElementException:
		print("Did not find video")
		return None

def download_img(hashtag, img_src, img_cnt, img_call):
	img_Data = requests.get(img_src).content
	with open(hashtag + "/" + img_call + "_"+str(img_cnt)+"_.jpg", 'wb') as handler:
		handler.write(img_Data)
		

def img_src_alt(hashtag, img_cnt, img_call):
	WebDriverWait(driver, 3)
	print('located image')
	# current_url = driver.current_url
        # get the 'main' page content to make our lives better
	html = driver.page_source
	# print(html)
	soup = bs(html, 'html.parser')
	img_source = soup.findAll('div', class_="_aagv")[-1].find('img')['src']
	img_source_alt = soup.findAll('div', class_="_aagv")[-1].find('img')['alt']
	# first_image = driver.find_element(By.CSS_SELECTOR, 'div[class="_aagv"], [style="padding-bottom: 120.208%;"] > img').get_attribute("src") #img
	# first_image = driver.find_element(By.CSS_SELECTOR, 'li[class="_acaz"] > div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"] > div[class = "x1qjc9v5 x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xdt5ytf x2lah0s xk390pu xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xggy1nq x11njtxf"] > div > div[class="_aagu _aato"] > div[class="_aagv"] > img').get_attribute("src") #img
	print("image source", img_source)
	download_img(hashtag, img_source, img_cnt, img_call)
	# first_image_alt = driver.find_element(By.CSS_SELECTOR,"div._aagv > img.alt").text
	# img_source_alt = soup.find('div', class_="_aagv", style="padding-bottom: 120.208%;").find('img')['alt']
	print("image_alt", img_source_alt)
	
	if img_cnt <= 1:
		comment = driver.find_element(By.CSS_SELECTOR, 'h1[class = "_ap3a _aaco _aacu _aacx _aad7 _aade"]').text
		print("Comment:", comment)
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


	return (img_source, img_source_alt, account, likes, comment, time)


def vid_src_alt(hashtag, img_cnt, img_call):
	WebDriverWait(driver, 3)

	# vid_src = driver.find_element(By.CSS_SELECTOR, 'div[class = "x5yr21d x1uhb9sk xh8yej3"]').get_attribute('src')
	vid_src = driver.find_element(By.CSS_SELECTOR, 'video[class= "x1lliihq x5yr21d xh8yej3"]').get_attribute('src')
	print("vid_src", vid_src)
	thumbnail_src = driver.find_element(By.CSS_SELECTOR, 'div[class = "_aagv"] > img').get_attribute("src") #img
	print("thumbnail_src", thumbnail_src)
	download_img(hashtag, thumbnail_src, img_cnt, img_call)


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
	
	return (vid_src, thumbnail_src, account, likes, comment, time)


def save_carousel_post(hashtag, img_name):
	WebDriverWait(driver, 3)

	img_url = driver.current_url
	img_call = img_url.split('/')[-2]
	print("img_call", img_call)

	img_src = []
	img__alt = []
	accounts = []
	post_like = []
	comments = []
	datetime = []
	img_file = []
	video_src = []


	# if nested_check() != 0:
	# if driver.find_element(By.CSS_SELECTOR,"svg[aria-label='Carousel']") is not None:
	# if driver.find_element(By.CSS_SELECTOR,"div[class=' _9zm2']") is not None:
	print("found carousel")
	if video_check() != None:
	# if driver.find_element(By.CSS_SELECTOR, 'div[class = "x5yr21d x1uhb9sk xh8yej3"]') is not None:	
		print("a video starts off the carousel")
		img_cnt =1
		vid_src, thumbnail_src, account, likes, comment, time = vid_src_alt(hashtag, img_cnt, img_call)
		accounts.append(account)
		post_like.append(likes)
		comments.append(comment)
		datetime.append(time)
		vid_src = vid_src.split("blob:")[-1]
		video_src.append(vid_src)
		img_src.append(thumbnail_src)
		mp4 = urllib.request.urlretrieve(vid_src, hashtag + '/{}.mp4'.format(img_call))
		img_file.append(mp4[0])
			# with open(hashtag + '/cnt_'+str(img_cnt)+img_call, 'wb') as f:
			# 	f.write(mp4[0])			# with open(hashtag + '/cnt_'+str(img_cnt)+img_call, 'wb') as f:
			# mp4.save(hashtag+'/cnt_'+str(img_cnt)+img_call+'.mp4')
		img_cnt += 1
		print("image count", img_cnt)

			# nested_check().click()        
		driver.find_element(By.CSS_SELECTOR,'button[class = "_afxw _al46 _al47"], div[class=" _9zm2"]').click()
		# driver.find_element(By.CSS_SELECTOR,"div[class='x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy x1ypdohk']").click()

	elif video_check() == None:
		print("an image starts off the carousel")
		img_cnt =1
		src, alt, account, likes, comment, time = img_src_alt(hashtag, img_cnt, img_call)
		img_src.append(src)
		img__alt.append(alt)
		accounts.append(account)
		post_like.append(likes)
		comments.append(comment)
		datetime.append(time)
		img_cnt +=1
		print("image count", img_cnt)
		# jpg = urllib.request.urlretrieve(src, hashtag + '/{}.jpg'.format(img_call))
		# print("jpg path", jpg)
		# img_file.append(jpg[0])
		


			# jpg[0].save(hashtag+'/cnt_'+str(img_cnt)+img_call+'.jpg')
			# with open(hashtag + '/cnt_'+str(img_cnt)+img_call, 'wb') as f:
			# 	f.write(jpg[0])

			# tags.append(tag)
   
			# nested_check().click()        
		driver.find_element(By.CSS_SELECTOR,'button[class = "_afxw _al46 _al47"], div[class=" _9zm2"]').click()
		# driver.find_element(By.CSS_SELECTOR,"div[class='x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy x1ypdohk']").click()

	else:
		print("did not find anything in post")
		
    #save everything to csv
	s1 = pd.Series(driver.current_url, name='URL')
	s2 = pd.Series(img_name, name='hashtag')
	s3 = pd.Series(img_src, name='img_src')
	s4 = pd.Series(img__alt, name='img__alt')
	s5 = pd.Series(accounts, name='accounts')
	s6 = pd.Series(post_like, name='like_count')
	s7 = pd.Series(comments, name='initial_comment')
	s8 = pd.Series(datetime, name='datetime')
	s9 = pd.Series(img_file, name='post_file')
	s10 = pd.Series(video_src, name='video_src')
	s11 = pd.Series(hashtag + '/'+img_call + ".jpg", name='file_path')
	df = pd.concat([s1,s2, s3,s4,s5,s6,s7,s8,s9,s10, s11], axis=1)
	#append df to existing csv (create one before running)
	df.to_csv('content.csv', mode='a', header=False)
	print("Data appended successfully.")
	

def save_sngl_content_post(hashtag, img_name):
	WebDriverWait(driver, 3)

	img_url = driver.current_url
	img_call = img_url.split('/')[-2]
	print("img_call - single", img_call)

	img_src = []
	img__alt = []
	accounts = []
	post_like = []
	comments = []
	datetime = []
	img_file = []
	video_src = []
	img_cnt = 1
		# if driver.find_element(By.CSS_SELECTOR,"svg[aria-label='Carousel']") is not False:
		# if driver.find_element(By.CSS_SELECTOR, 'div[class = " _9zm2"]') is not None:
	if video_check() is not None:
		print("getting single video post")
		vid_src, thumbnail_src, account, likes, comment, time = vid_src_alt(hashtag, img_cnt, img_call)
		accounts.append(account)
		post_like.append(likes)
		comments.append(comment)
		datetime.append(time)
		img_src.append(thumbnail_src)
		vid_src = vid_src.split("blob:")[-1]
		video_src.append(vid_src)
		mp4 = urllib.request.urlretrieve(vid_src, hashtag + '/{}.mp4'.format(img_call))
		print("mp4 path", mp4)
		img_file.append(mp4[0])
			# img_cnt += 1

			# with open(hashtag + '/cnt_'+str(img_cnt)+img_call, 'wb') as f:
				# f.write(mp4)
			# mp4[0].save(hashtag+'/cnt_'+str(img_cnt)+img_call+'.mp4')


			# tags.append(tag)
	else:
		print("getting single image post")
		src1, alt1, account, likes, comment, time = img_src_alt(hashtag, img_cnt, img_call)
		img_src.append(src1)
		img__alt.append(alt1)
		accounts.append(account)
		post_like.append(likes)
		comments.append(comment)
		datetime.append(time)
		jpg = urllib.request.urlretrieve(src1, hashtag + '/{}.jpg'.format(img_call))
		print("jpg path", jpg[0])
		img_file.append(jpg[0])
			# with open(hashtag + '/cnt_'+str(img_cnt)+img_call, 'wb') as f:
			# 	f.write(jpg[0])
			# jpg[0].save(hashtag+'/cnt_'+str(img_cnt)+img_call+'.jpg')	
    #save everything to csv
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
	df = pd.concat([s1,s2, s3,s4,s5,s6,s7,s8,s9,s10, s11], axis=1)
	#append df to existing csv (create one before running)
	df.to_csv('content.csv', mode='a', header=False)
	print("Data appended successfully.")
	

def download_allposts(hashtag):

	# open First Post
	# print(" URL:", url)
	parent_path = os.getcwd()

	# images = driver.find_elements(By.CLASS_NAME,'_aagv')
	# image_keys = driver.find_elements(By.CLASS_NAME,'x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x4gyw5p _a6hd')
	# for image in images:
	# 	for key in image_keys:
	# 		key = key.get_attribute('href')
	# 		print("key in image keys", key)
	# 		image = image.get_attribute('src')
	# 		print("image src in images", image)
	# 		imgkit.from_url(image, "/"+ hashtag+ "/" + str(key)+".jpg")
	# 		print("saved jpg")
	
	
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
	multiple_images = nested_check()
	
    # if nested chexk exists, then the are multiple images in the post
	if multiple_images:
		print("Post has multiple images/videos")
		post_count = 1
		nescheck = nested_check()
		count_img = 0
		imagesrc = []
		

        #figure out why this is happening!!
		while nescheck:
			WebDriverWait(driver, 1.5)
			elem_img = driver.find_element(By.CLASS_NAME,'_aagv').get_attribute('src') #_aagw
			print("elem_img", elem_img)
			imagesrc.append(elem_img)  #added this to save the image
			# save_content() #added this to save the image

			# Function to save nested images
            # save_multiple(hashtag +'/'+'image'+str(count_img), elem_img)
			count_img += 1
			# next_post()
			# save_PostContent(hashtag, hashtag +'_imgcnt_'+str(count_img))
			save_carousel_post(hashtag, hashtag +'_imgcnt_'+str(count_img))
			print("added multiple image post")
			nescheck.click()
			nescheck = nested_check()
			post_count +=1
   

		# pass last_img_flag True
		# save_multiple(hashtag +'/'+'content1.' +
		# 			str(count_img), elem_img, last_img_flag=1)


	else:
		# this goes to the function above, which uses BS to look through the html and find the source image and other things
        # making my own function here for testing
		# save_content('_aagv', hashtag+'/'+'content1') #_aagw
		print("We have one image/video")
		post_count = 1
		# elem_img = driver.find_element(By.CLASS_NAME,'_aagv').get_attribute('src')
		save_sngl_content_post(hashtag, hashtag +'_imgcnt_'+str(post_count))
        # save_PostContent(hashtag, hashtag +'_postcnt_'+str(post_count))
		print('added single image post')
		post_count +=1
		# next_post().click()

		# with open(ht+".csv", 'wb') as f:
		# 	f.write()
	c = 2
	
	# while(True):
	while(c <= 8):
		print("current post count", post_count)
		next_el = next_post()
		
		if next_el != False:
		# if next_el != 0:
			next_el.click()
			print("onto the next_el")
			
			time.sleep(3)
			
			# try:
			multiple_images = nested_check()
			
			if multiple_images:
				print('next post has multiple images/vids')
				nescheck = multiple_images
				count_img = 0
					
				while nescheck:
					# elem_img = driver.find_element(By.CLASS_NAME,'_aagv').get_attribute('src') #_aagw
					# print("next post elem_img", elem_img)
					# elem_img = driver.find_element(By.CLASS_NAME,'rQDP3')
					save_carousel_post(hashtag, hashtag+'/'+'_post_' +
								str(c)+'_imgage'+str(count_img))						
                       # save_PostContent(hashtag, hashtag+'/'+'_post_' +
									# str(c)+'_imgage'+str(count_img))
					count_img += 1
						# nescheck.click()
					nescheck = nested_check()
					# save_PostContent(hashtag, hashtag+'_image'+str(c))
					# post_count +=1

					# save_content(hashtag+'/'+'content'+str(c) +
					# 			'.'+str(count_img), elem_img, 1)
			else:
				# elem_img = driver.find_element(By.CLASS_NAME,'_aagv').get_attribute('src') #_aagw
				# print("single post - next post elem_img", elem_img)
					# save_content('_97aPb', hashtag+'/'+'content'+str(c))
				save_sngl_content_post(hashtag, hashtag+'_image'+str(c))
					# save_PostContent(hashtag, hashtag+'_image'+str(c))
				print("saved single post")
				post_count +=1
				next_post().click()

			
			# except selenium.common.exceptions.NoSuchElementException:
			# 	print("finished")
				# return
		
		else:
			break
		
		c += 1
	driver.close()
	return




if __name__ == "__main__":
	# path()
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
 