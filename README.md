# Magic-Clothe
Have you heard of "Adrishya Choga" or "invisibility cloak" in Harry Potter movies. Magic Clothe does same with the color range of your choice.
 


Recording video key points : 
--------------------------
> record for atleast 10 seconds just background in beginning of video.
> then place object and use cloth of which lower and upper bounds are set.

Working of project :
------------------
1.During working of program first the background is saved as 
background.

2.Now after object is placed and cloth placed over it,the color is segmented out and named as mask1(white for cloth area and black for rest).

3.After performing erosion and dilation on mask1 we calculate bitwise not and get mask2(black for cloth and white for rest).

4.Now we add background using mask1 so at place of cloth we load background and save as res1.

5.Similarly we calculate sum of img(frame of video recorded presently) and mask2 that loads the other background presently as res2.

6.Now we add them both to get the final resultant image.

  
     

