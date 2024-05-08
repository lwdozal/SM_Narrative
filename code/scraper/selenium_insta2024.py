




# import required modules
from selenium import webdriver
import time, urllib.request
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


import pandas as pd
import os


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




if __name__ == "__main__":
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
 