function [] = addNoise( rootFolder, distination )
% This function will read all images in your subfolders and create 
% several versions of the original images and save into the distination 
% folder.

% This function takes the 
%     1. rootFolder: root path of your images 
%     2. distination: result folder you want your new images be
% as input.

% note to use absolute value for the directory paths, 
% no need to create the dist folder manually, just provide a new path is enough
% example: addNoise('/home/bruce/Res/merged_images', '/home/bruce/Res/new_images')

    %create the distination folder first
    mkdir(distination);
    
    folders = dir(rootFolder);
    [folderLength, ~] = size(folders);

    sum = 0;
    %iterate all subfolders (starts from 4 bcz 1,2,3 are '.','..' and '.D*')
    for i = 4:folderLength
        
        folderPath = [rootFolder, '/', folders(i).name];
        disp(folderPath);
        
        images = dir(fullfile(folderPath,'*.jpg'));
        nbrOfImages = length(images);
        sum = sum + nbrOfImages;
        disp(['processing ' num2str(nbrOfImages) ' images']);
        
        %make sure to create the subfoldr first
        mkdir([distination, '/', folders(i).name]);
        for j = 1:nbrOfImages

            disp(['finished ' num2str(j) 'images, total: ' num2str(nbrOfImages) ' images in current folder']);

            currentImagePath = [folderPath, '/', images(j).name];
            currentImage = imread(currentImagePath);
            
            [~, name, ~] = fileparts(currentImagePath);
            dis = [distination, '/', folders(i).name, '/', name];
            
            %add gaussian nosie
            im1 = imnoise(currentImage, 'gaussian', 0, 0.008);
            im2 = imnoise(currentImage, 'gaussian', 0, 0.008);
            im3 = imnoise(currentImage, 'gaussian', 0, 0.008);
            
            imwrite(im1,[dis, '_gus1.jpg']);
            imwrite(im2,[dis, '_gus2.jpg']);
            imwrite(im3,[dis, '_gus3.jpg']);
            %add speckle noise
            im4=imnoise(currentImage,'speckle',0.008);
            im5=imnoise(currentImage,'speckle',0.008);
            im6=imnoise(currentImage,'speckle',0.008);
            
            imwrite(im4,[dis, '_spk1.jpg']);
            imwrite(im5,[dis, '_spk2.jpg']);
            imwrite(im6,[dis, '_spk3.jpg']);
            %add poisson
            im7 = imnoise(currentImage,'poisson');
            
            imwrite(im7,[dis, '_pos.jpg']);
            
            %smooth the image with gaussian filter
            %conv2 is only for gray scale image so i find the built-in
            %function to add the gaussian filter
            im8 = imgaussfilt(currentImage);
            
            imwrite(im8,[dis, '_smt.jpg']);
            
        end
        
        
    end;
        
    disp(sum);

end

