# puran
#december 06 2023
#mizuki akiyama :D 
## create a graphic image of an avatar using cmu graphics in python to demonstrate understanding of python and how it can play a role in graphic design


from cmu_graphics import *
from cmu_graphics.shape_logic import opacityTest


#background 
Circle(200,200,200, fill='lavenderBlush') #background circle


##bow background
Polygon(140,15,200,45,140,75, fill='mediumVioletRed') #bow right
Polygon(250,15,190,45,250,75, fill='mediumVioletRed') #bow left
Rect(180,30,30,30, fill='paleVioletRed') #middle






#ponytail thing :( 

Oval(100,200,80,200, fill='hotPink', rotateAngle=10)
Oval(100,300,75,180, fill='hotPink', rotateAngle=-10)
Oval(60,240,25,150, fill='lavenderBlush', rotateAngle=0)



#bow :DDD 

Rect(60,130,50,50, fill='slateBlue', rotateAngle=90) #bow
Rect(110,80,50,50, fill='slateBlue', rotateAngle=90)
Rect(95,110,30,35, fill='darkSlateBlue', rotateAngle=45) 

Oval(90,145,20,30, fill='darkSlateBlue', rotateAngle=45, opacity=80) #left shade
Oval(128,110,20,30, fill='darkSlateBlue', rotateAngle=45, opacity=80) #right shade


#hair
Circle(200,195,110, fill='pink')
Oval(285,180,70,120, fill='pink', rotateAngle=-12)
Oval(285,185,63,120, fill='lavenderBlush', rotateAngle=-5) 



#body parts

Oval(200,215,200,150, fill='bisque') #head


Rect(185,210,40,160, fill='bisque') #neck
Rect(185,289,40,10, fill=RGB(245, 193, 176)) #neck shadow
Oval(205,302,40,25, fill=RGB(245, 193, 176)) #neck shadow oval

Oval(200,400,260,130, fill='white') #shirt


#mouth
Oval(205,250,30,60, fill=RGB(255, 130, 170)) 
Rect(190,220,30,30, fill='bisque')



#more hair...  bangs

Oval(125,180,70,160, fill='pink', rotateAngle=20) #left 
Oval(125,180,57,145, fill='bisque', rotateAngle=20) 
Oval(120,180,55,155, fill='pink', rotateAngle=20)

Oval(200,150,100,140, fill='pink') #front :)
Oval(210,170,60,130, fill='bisque')
Oval(205,150,80,140, fill='pink', rotateAngle=-20) 

Oval(210,150,70,100, fill='white', rotateAngle=0, opacity=80) #shading middle
Oval(210,140,90,90, fill='pink', rotateAngle=0) #overlap top



Oval(250,180,50,120, fill='bisque', rotateAngle=-5) #right
Oval(260,175,55,125, fill='pink', rotateAngle=-20)
Oval(280,180,63,150, fill='pink', rotateAngle=-10)




#side hair ....

Oval(110,250,40,140, fill='pink') #left
Oval(110,270,40,140, fill='pink', rotateAngle=-10)
Oval(110,335,55,100, fill='pink', rotateAngle=10)
Oval(130,365,45,65, fill='white', rotateAngle=20)

Oval(115,325,45,60, fill='white', rotateAngle=-10, opacity=80)##highlights
Oval(115,320,45,50, fill='pink', rotateAngle=-10)



Oval(290,250,40,140, fill='pink') #right
Oval(290,270,40,140, fill='pink', rotateAngle=10)
Oval(290,335,55,100, fill='pink', rotateAngle=-10)
Oval(270,365,45,65, fill='white', rotateAngle=-20)

Oval(290,325,45,60, fill='white', rotateAngle=-10, opacity=80)##highlights
Oval(290,320,45,50, fill='pink', rotateAngle=-10)


#hair but it's highlight shading and lighter actually

Oval(120,180,60,120, fill='white', rotateAngle=20, opacity=80) #left
Oval(110,210,50,75, fill='pink', rotateAngle=20) #overlay bottom
Oval(135,145,50,50, fill='pink', rotateAngle=20) #overlay top

Oval(270,170,70,130, fill='white', rotateAngle=-20, opacity=80) #right
Oval(260,140,70,80, fill='pink', rotateAngle=-20) #overlay top
Oval(285,220,50,70, fill='pink', rotateAngle=-20) #overlay bottom





#shirt :)
Polygon(230,310,190,350,300,350, fill='slateBlue') #right
Polygon(250,320,190,350,300,350, fill='darkSlateBlue')


Polygon(210,350,100,350,180,310, fill='slateBlue') #left
Polygon(210,350,100,350,160,320, fill='darkSlateBlue')


Rect(150,350,20,100, fill='slateBlue') #strap left
Rect(150,350,10,100, fill='darkSlateBlue') #strap left shading
Rect(140,350,10,100, fill='lavender') #left shirt shading

Rect(240,350,20,100, fill='slateBlue') #strap right
Rect(240,350,10,100, fill='darkSlateBlue') #strap right shading
Rect(230,350,10,100, fill='lavender') #right shirt shading



#ribbon
Rect(178,360,20,60, fill='darkSlateBlue', rotateAngle=20) #left
Rect(210,360,20,60, fill='darkSlateBlue', rotateAngle=-20) #right
Rect(191,350,25,20, fill='darkSlateBlue') #bow middle


#eyes
Oval(160,220,30,50, fill='mediumVioletRed') #left eye
Oval(160,230,25,30, fill='paleVioletRed')

Oval(240,220,30,50, fill='mediumVioletRed') #right eye
Oval(240,230,25,30, fill='paleVioletRed')


Label(")", 150,190, rotateAngle=260, size=50, fill=RGB(125, 22, 67))

Label(")", 245,190, rotateAngle=-80, size=50, fill=RGB(125, 22, 67))




#border
Circle(200,200,250, fill=None, border='white', borderWidth=50) #circle border

cmu_graphics.run()