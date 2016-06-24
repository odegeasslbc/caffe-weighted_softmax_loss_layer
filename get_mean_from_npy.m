function [ newmean ] = get_mean_from_npy( path )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

tarainmean = readNPY(path);
b = tarainmean(1,:,:);
g = tarainmean(2,:,:);
r = tarainmean(3,:,:);

b = reshape(b,[256,256]);
g = reshape(g,[256,256]);
r = reshape(r,[256,256]);

nnb = b';
nng = g';
nnr = r';

newmean=zeros(256,256,3);

for i = 1:256
   for j = 1:256
       newmean(i,j,1)=nnb(i,j);
   end
end
for i = 1:256
   for j = 1:256
       newmean(i,j,2)=nng(i,j);
   end
end
for i = 1:256
    for j = 1:256
        newmean(i,j,3)=nnr(i,j);
    end
end

newmean = single(newmean);

end

