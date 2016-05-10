import os
from os import rename

root = "/home/bruce/Res/new_images"
dis = "/home/bruce/Res/ttt"				
for foldername in os.listdir(root):

	if foldername.startswith('.') == False:
		nbr = 0	
		for filename in os.listdir(root+'/'+foldername):
			#print nbr
			#if not any(value in filename for value in ("gus1.jpg","gus2.jpg","gus3.jpg","spk1.jpg","spk2.jpg","spk3.jpg","pos.jpg","smt.jpg")):
			if filename.endswith('_org_org.jpg'):
				newname = filename[:-12] + "_org.jpg"
				rename(os.path.join(root,foldername,filename), os.path.join(root,foldername,newname))
			#nbr += 1
			#newname = filename[:-8] + ".jpg"
			#rename(os.path.join(root,foldername,filename), os.path.join(root,foldername,newname))  
			
		print foldername, " done" 

