
function alignment_based_on_dots(atlas,img,map_dots,img_dots,name)
%clear; close all;
imgAtlas =imread(atlas) ; %imgSlice xxx.png
imgSlice= imread(img); % imgAtlas unit8
imgSlice=imresize(imgSlice,2)
t = fitgeotrans(map_dots,2*img_dots,'lwm',12);
Fix = imref2d(size(imgSlice));
AlignAtlasSlice = imwarp(imgAtlas,t,'OutputView',Fix);
set(0,'DefaultFigureVisible', 'off')
x=figure(2);
y=imshowpair(1+imgSlice,uint8(imcomplement(AlignAtlasSlice)),'blend');
saveas(x,name) %'finaltest.jpg'
