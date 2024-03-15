# All Shapes
*(14:02 in video)*

Here is a list of all the shapes code and properties

### Circles
``` Circle( centreX, centreY, radius)```


```Circle(75, 360, 5) ```

### Ovals
```Oval(centerX, centerY, width, height)```

```Oval(100, 100, 120, 150)```
### Stars
```Star(centerX, centerY, radius, points)```

Stars can have a special property called Roundness which can be anything from 0 to 100.  

```Star(350, 200, 50, 5, fill='dodgerBlue', roundness=10)```
### Rectangles
Here is the code for a rectangle:

```Rect(left, top, width, height)```

Like other shapes, rectangles can also have fills and gradients.  

### Polygons
Here is the code for a regular polygon:

```RegularPolygon(centerX, centerY, radius, points)```
### Polygons (Any Shape)
To make any shape, you just make a list of the x,y coordinates of the corners. You can have as many as you need. 

```Polygon(x1,y1,x2,y2,x3,y3,x4,y4,x,y5)```
### Lines
```Line(x1, y1, x2, y2)```
This draws a line from the point (x1, y1) to the point (x2, y2). 

Lines have some special properties including: 

- dashes (either True or False)
- lineWidth (any number bigger than 0)
  
```Line(100, 300, 300, 100, fill='limeGreen', lineWidth=5, dashes=True)```
### Labels
Labels are a way of drawing text.

```Label(value, centerX, centerY)```

value is the text drawn by the Label. It is a string and should be enclosed in quotes

Labels have lots of extra properties we can use. Here is a list of all of them, followed by an example:

>-    size: A number bigger than 0.
>-    bold: Either True or False
>-    italic: Either True or False
>-    font: Any of the following values:  'arial', 'monospace', 'caveat', 'cinzel', 'montserrat', 'grenze',     'sacramento', 'orbitron'

```Label('WOOHOO!',250,250, fill='white', font='monospace', size=60, bold=True)```
### Colours
If you want some colour in your shapes, you need to add on a fill colour property like this:

```Circle( centreX, centreY, radius, fill='colour')```

For colour, you can choose from any of these colour words 
https://academy.cs.cmu.edu/docs/builtInColors 

### Background Colour
app.background = 'colour'

```app.background = 'limegreen'```
### RGB Colours
Instead of the colour names, you can also use rgb colours.

The RGB color value is a mix of three colour components. R is red, G is Green, and B is blue. Each of the color components (R, G, B) is a value between 0 and 255 as integers.

```Circle( centreX, centreY, radius, fill=rgb(255,0,0)```
would make a red circle because there is no green or blue in it. 

### Gradients
Gradients are when one colour blends into another colour.  If you don't say where to start, it will go from the centre to the outside of the shape. Gradients can have more than 2 colours if you choose.

```Circle(200,200,150,fill=gradient('red','yellow','blue','green',start='bottom-right'))```

If you don't specify a start point, the gradient will go from the centre.

### Opacity Property
Opacity is how 'see through' a shape is, and can have values 0 to 100.

```Rect(230,130, 150,100, fill='saddleBrown',opacity=60)```

### Border and borderWidth Property
You can add a border around any shape by using:

fill='innerColor', border='borderColor', borderWidth=2

```Circle(300, 300, 50, fill='limeGreen', border='dodgerBlue', borderWidth=20)```
 

### rotateAngle Property
This rotates any shape.  The number we use is the number of degrees that we want to rotate the shape clockwise.  Its value can be 0 to 360

```Rect(250, 250, 100, 100, fill=gradient('violet', 'indigo', start='left'), rotateAngle=270)```
### All Properties 
Here is a list of all the properties in this unit:

>-    fill: A color name inside quotes ''.
>-    border: A color name inside quotes ''.
>-    borderWidth: Any number bigger than 0.
>-    dashes: Either True or False.
>-    opacity: A number between 0 and 100.
>-    rotateAngle: Any number.
>-    roundness (*Only for Stars*): A number between 0 and 100.
>-    lineWidth (*Only for Lines*): Any number bigger than 0.
>-    size (*Only for Labels*): Any number bigger 0.
>-    bold (*Only for Labels*): Either True or False.
>-    italic (*Only for Labels*): Either True or False.
>-    font (*Only for Labels*): Any of the provided fonts. 

