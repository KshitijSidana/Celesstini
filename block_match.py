import cv2
import glob
import numpy as np
imgs = []
d = []
size = ()
def rmse(a,b):
	return ((a**2 + b**2)/2)**0.5

def min_error(imgl, imgr , w , x , y):
	global size
	tmp = 0
	ep = -1
	val = imgl[x][y]

	for x1 in range (x-w,x+w):
		if (x1 < size[0]):
			e = rmse(imgl[x][y],imgr[x1][y])
			if ep == -1:
				ep = e
			else:
				if e<ep:
					ep = e
					tmp = x
	return ep,x1			  

def disp( imgl, imgr, window ):
	w = window/2 #half window width
	global size
	global d
	size = np.shape(imgl) # height , width
	d = np.zeros(size)
	for x in range (0,size[0]):
		for y in range (0,size[1]):
			ep,x1=min_error(imgl, imgr,w,x,y)
			d_shift = x1-x
			d[x][y] = (d_shift/w)*255*ep/100;

def read ():	
	global imgs
	for img in glob.glob("/home/kshitij/Documents/celestini/MiddEval3/trainingQ/*/im*.png"):
	    cv_img = cv2.imread(img)
	    cv_img = cv2.cvtColor(cv_img,cv2.COLOR_BGR2GRAY)
	    imgs.append(cv_img)
    #print(np.shape(imgs))
	disp (imgs[0],imgs[1],window=20)


if __name__ == '__main__':
	read()
	cv2.imshow ('disp',d)
