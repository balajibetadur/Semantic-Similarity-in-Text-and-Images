# import the necessary packages

#to calculate the similarity between two images
from skimage.measure import compare_ssim as ssim
#to show images
import matplotlib.pyplot as plt
#to read images
import cv2


#read the images from the folder images

p1 = cv2.imread("images/1.png")
p2 = cv2.imread("images/2.png")
p3 = cv2.imread("images/3.png")
p4 = cv2.imread("images/4.png")
p5 = cv2.imread("images/5.png")
p6 = cv2.imread("images/6.png")
p7 = cv2.imread("images/7.png")
p8 = cv2.imread("images/8.png")
p9 = cv2.imread("images/9.png")
p10 = cv2.imread("images/10.png")



# convert the images to grayscale
# p1 = cv2.cvtColor(p1, cv2.COLOR_BGR2GRAY)
# p2 = cv2.cvtColor(p2, cv2.COLOR_BGR2GRAY)
# p3 = cv2.cvtColor(p3, cv2.COLOR_BGR2GRAY)
# p4 = cv2.cvtColor(p4, cv2.COLOR_BGR2GRAY)
# p5 = cv2.cvtColor(p5, cv2.COLOR_BGR2GRAY)
# p6 = cv2.cvtColor(p6, cv2.COLOR_BGR2GRAY)
# p7 = cv2.cvtColor(p7, cv2.COLOR_BGR2GRAY)
# p8 = cv2.cvtColor(p8, cv2.COLOR_BGR2GRAY)
# p9 = cv2.cvtColor(p9, cv2.COLOR_BGR2GRAY)
# p10 = cv2.cvtColor(p10, cv2.COLOR_BGR2GRAY)



# initialize the figure
fig = plt.figure("Images")

#list of all the images
images = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

# loop over the images
plt.suptitle(" All images")
for (i,  image) in enumerate(images):
	# show the image
	ax = fig.add_subplot(2, 5, i + 1)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

# compare the images


pair=[]#list of paired images to compare
avg=[]#list to store average score of similarity values for all images
scores=[]#list to add scores of similarity value
for i in images:
	h=[]
	o=[]
	sum=0
	for j in range(0,len(images)):

		#similarity between two images is calculated 
		s=ssim(i,images[j],multichannel=True)#multichannel is True to calculate colour images to calculate in multi dimensions

		#s value is rounded to 2 decimal points
		s=round(s,2)

		#s value is added to sum to compute average later
		sum+=s
		#thershold s value is 0.15
		if s>0.15:
			#if s is more than thershold then image is grouped

			h.append(j)#adding images to group

			o.append(s)#adding s value to add to score list
			
	avg.append(sum)
	scores.append(o)
	

	pair.append(h)

#avg is sorted to find the minimum avg value
avg2=sorted(avg)
#finds min in list
min=avg2[0]
for i in avg:
	if i==min:
		ind=avg.index(i)
		u_img=images[ind]
		# show the image
		ax = fig.add_subplot(1,1,1 )
		ax.set_title('unique image')
		plt.imshow(u_img, cmap = plt.cm.gray)
		plt.axis("off")
		
	# show the figure
		plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 1 matches")
for (i,  image) in enumerate(pair[0]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[0]), i+1 )
	j+=1
	ax.set_title(scores[0][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 2 matches")
for (i,  image) in enumerate(pair[1]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[1]), i+1 )
	j+=1
	#ax.set_title(name)
	ax.set_title(scores[1][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 3 matches")
for (i,  image) in enumerate(pair[2]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[2]), i+1 )
	j+=1
	#ax.set_title(name)
	ax.set_title(scores[2][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 4 matches")
for (i,  image) in enumerate(pair[3]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[3]), i+1 )
	j+=1
	#ax.set_title(name)
	ax.set_title(scores[3][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 5 matches")
for (i,  image) in enumerate(pair[4]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[4]), i+1 )
	j+=1
	#ax.set_title(name)
	ax.set_title(scores[4][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 6 matches")
for (i,  image) in enumerate(pair[5]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[5]), i+1 )
	j+=1
	#ax.set_title(name)
	ax.set_title(scores[5][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 7 matches")
for (i,  image) in enumerate(pair[6]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[6]), i+1 )
	j+=1
	#ax.set_title(name)
	ax.set_title(scores[6][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 8 matches")
for (i,  image) in enumerate(pair[7]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[7]), i+1 )
	j+=1
	#ax.set_title(name)
	ax.set_title(scores[7][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 9 matches")
for (i,  image) in enumerate(pair[8]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[8]), i+1 )
	j+=1
	#ax.set_title(name)
	ax.set_title(scores[8][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()

fig = plt.figure("Matched Images")
plt.suptitle("Image 10 matches")
for (i,  image) in enumerate(pair[9]):
	
	# show the image
	ax = fig.add_subplot(1, len(pair[9]), i+1 )
	j+=1
	#ax.set_title(name)
	ax.set_title(scores[9][i])
	plt.imshow(images[image], cmap = plt.cm.gray)
	plt.axis("off")
	
# show the figure
plt.show()
