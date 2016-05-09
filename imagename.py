import os
from os import rename

root = "/home/bruce/Res/merged_images"				
for foldername in os.listdir(root):

	if foldername.startswith('.') == False:
		
		for filename in os.listdir(root+'/'+foldername):
			if filename.endswith("Blog.jpg"):
				newname = filename[:-9]
				rename(os.path.join(root,foldername,filename), os.path.join(root,foldername,newname))
		print foldername, " done" 


		        


