# Circles and Rectangles
*(3:22 in video)*

Let's add in some shapes!
# Circles
To draw a circle, you need to give the x,y coordinates of the centre and the radius.

```Circle(centerX, centerY, radius)```

for example

```Circle(75, 300, 50)```

will draw a circle with centre at (75,300) and a radius of 50.

![Try it yourself](tutImages/runSml2.png) 
### Take care with syntax!  You must use correct capitalisation with your commands.

## Add Some Colour
Your circle will be filled with black if you don't add a fill colour property like this:

```Circle(centerX, centerY, radius, fill='colour')```

For example

```Circle(75, 300, 50, fill = 'orangeRed')```

will draw an orange circle at (75,360)

![Try it yourself](tutImages/runSml2.png) 
Draw a circle using the code above, then draw a different size and colour circle on the right hand side of the canvas.

### Run and Stop

Click the green Run button at the top to see your creation.

Click the Stop button when you've finished.

If you change your code, you will need to click Run again to see your updates.

---
# Rectangles
To draw a rectangle you must give the left, top coordinates, followed by the width and height:

```Rect(left, top, width, height)```

For example

```Rect(75,20,80,40, fill ='gold')```

![Try it yourself](tutImages/runSml2.png) 
Draw the rectangle above, then draw a different size and colour rectangle on the right hand side of the canvas.