# Extension (OPTIONAL)

"""
Classes - An Introduction to Custom Types

A very important question in Python programming that we haven't
covered in this unit is how we can create our own type of objects.
This introductory activity to custom objects and types might look 
a bit intimidating on first glance (based on its length). But 
this is only because it is written as a self-contained introduction
that takes one step at a time (and nothing for granted).

Don't do this activity just for getting 1.5 marks (hopefully you
have reached your full workshop marks anyway some time ago). If 
you just do it for marks it will probably feel lengthy (like most
things that you just do for marks... or any other reward for that
matter). Do this last workshop activity of FIT1045/53 if/when you
are eager to learn more about Python. Stay curious.


1. Motivation

The built-in types like int, float, bool, list, str principally
allow us to represent all sorts of things. But relying only on them
can become pretty cumbersome, and we often would like to group
related values in one object.

For instance, we could represent circles in the plane by three
float values representing the x and y coordinates of the centre 
and the radius like this
>>> cx1, cy1, r1 = 2.0, 2.0, 1.0
>>> cx2, cy2, r2 = 2.0, 0.0, 0.9
>>> cx3, cy3, r3 = 0.0, 2.0, 3.0

and then define a function

circles_intersect(cx1, cy1, r1, cx2, cy2, r2) that

returns True if and only if the point (x, y) is contained in the
circle defined by cx, cy, and r:
>>> circles_intersect(cx1, cy1, r1, cx2, cy2, r2)
False
>>> circles_intersect(cx1, cy1, r1, cx3, cy3, r3)
True

This is quite a long parameter list that makes programs that use
this function hard to read and error-prone. For instance, while
developing this worksheet, the author made the following mistake
(and not for didactic reasons):

circles_intersect(cx1, cy1, r1, cx2, cx2, r2)

Things could also easily get worse. Imagine for instance we need 
a function that determines whether two ellipses interesect. This 
would result in a function with 10 parameters: 2 focus points and 
1 radius per ellipse!

In such situations we would much prefer to have objects that
group the related information. To start, we could use tuples
to represent points as a single object. With this we could write
>>> c1, r1 = (2.0, 2.0), 1.0
>>> c2, r2 = (2.0, 0.0), 0.9
>>> c3, r3 = (0.0, 2.0), 3.0

and use a four-parameter function definition instead:
>>> circles_intersect2(c1, r1, c2, r2)
False
>>> circles_intersect2(c1, r1, c3, r3)
True

>>> circle_contains2(c1, r1, (1.5, 2.0))
True
>>> circle_contains2(c1, r1, (1.0, 1.0))
False

However, the centre c and the radius r are also related and
simply adding r to the tuple would result in an unintuitive 
conventation that is hard to memorise and read. For instance,
it will be difficult to decide which of the following 
Boolean expressions correctly captures the concepts that
two circles intersect:
- euclidean_distance(c1[0], c1[1], c2[0], c2[1]) <= c1[2] + c2[2]
- euclidean_distance(c1[1], c1[2], c2[1], c2[2]) <= c1[0] + c2[0]


2. A First Look at Classes (and how to not use them)

It would be much better to have a specific type of objects
for representing circles that provides the three involved
values under descriptive attribute names like this
>>> c1 = Circle((2.0, 2.0), 1.0)
>>> c2 = Circle((2.0, 0.0), 0.9)
>>> c3 = Circle((0.0, 2.0), 3.0)
>>> c1
Circle((2.0, 2.0), 1.0)
>>> c1.centre
(2.0, 2.0)
>>> c1.radius
1.0

Since Python does not provide Circle as built-in object type,
we have to create it. This can be done via a class definition
like the following:

>>> class Circ:
...     pass

This class definition creates a function-like object (more 
precisely a 'type' object that can be called like a function) with
the name 'Circ' that can be used to create objects of a brand-new
Circ type (this abbreviation is not a nice name, we just use it
for this first attempt of defining a class to not clash with
our final Circle class defined further below):
>>> Circ
<class '__main__.Circ'>
>>> c = Circ()

Great! We have just created not only our first custom type, but
also one object with that type. Unfortunately, using the empty 
class definition above results in very boring objects with no 
attributes or methods. It turns out, we could add attributes to
the object by simply assigning them:
>>> c.centre = (0.0, 0.0)
>>> c.radius = 1.0
>>> c.centre 
(0.0, 0.0)
>>> c.radius
1.0

This way we could create our desired circle objects but this is 
not very convenient. The key to making this whole exercise useful
is to add methods to our objects, which, as it turns out, can be
done by equipping our 'Circ' type with function attributes (recall
'Circ' was this interesting function-like object we got through 
our class definition). One way to do this (that we should not use 
other than in very specific circumstances) is to assign functions 
attributes directly to 'Circ'.


3. From Functions to Methods

Let's say we have the following function:
>>> from math import pi
>>> def circumference(circle):
...     return 2*pi*circle.radius

Given that our circle object 'c' has the attribute radius, we can
call this function with the expected outcome
>>> circumference(c)
6.283185307179586

What is more interesting is what happens if we add this function
as attribute to the Circ type object:
>>> Circ.circumference = circumference

It turns out, the circumference function is now avaiable as method
of our object 'c' (which as we recall is of type 'Circle').
>>> c.circumference()
6.283185307179586

Note how the function, which actually takes one input argument (circle)
turned into a zero argument method. What happens when we call
circumference as a method on some circle object c is that the object c
itself is used as the function argument.

What happens if the function that we use as a method takes more than
one argument? Let's find this out by defining another potentially
useful function---one that we can use to more conveniently initialise
Circ objects.
>>> def init_circle(circle, centre, radius):
...    circle.centre = centre
...    circle.radius = radius
>>> Circ.init = init_circle
>>> c2 = Circ()
>>> c2.init((2.0, 1.0), 0.9)
>>> c2.centre
(2.0, 1.0)
>>> c2.radius
0.9

Ok. So method calls work by using the object as the first argument
to the underlying function that defines the method.


4. Magic Methods and How to Really Initialise Objects

The above init method could be taken as a first attempt to improve
our so far embarassingly inconvenient process of creating useful
Circle objects (namely those that have an actual centre and radius
attribute). However, used as above this is still not very convincing.
Our actual goal was to be able to this

c1 = Circle((2.0, 2.0), 1.0)

and be done with creating a circle object. So somehow we have to
modify the way in which Circle can be called (we need it to take
two parameters instead of none) and what it does (it should initialise
the created object instead of just spitting out a naked one that
we have to finish ourselves). Enter one of the most characteristic 
features of the Python language: the 'magic method'. 

Magic methods (or 'special methods' as they are more modestly called
in the Python documentation) are methods with specific names that 
begin with and end with two underscores '__'. The most important 
special method is the one called '__init__'. This method is precisely
what we are looking for: it determines the definition of the 'Circle'
function/callable object. 

Luckily, we have already defined a function to initialise circles.
So we can directly move ahead and use it to demonstrate the effect
of defining an __init__ method:
>>> Circle.__init__ = init_circle
>>> c1 = Circle((2.0, 2.0), 1.0)
>>> c1.centre
(2.0, 2.0)
>>> c1.radius
1.0
>>> c1.circumference()
6.283185307179586

Beautiful! We finally got there. Before we go ahead and put everything
together, let us define one more special method: the '__repr__' method.
So far we couldn't inspect our circle objects very easily after they
are created (try evaluating just c1 in the shell). To get a informative
(string) representation for circles we can define a '__repr__'. The 
following function will do:
>>> def circle_as_string(circle):
...     return 'Circle({}, {})'.format(circle.centre, circle.radius)
>>> Circle.__repr__ = circle_as_string
>>> c1
Circle((2.0, 2.0), 1.0)


5. Defining Classes - The Actual Way To Do It

As indicated above, binding previously defined 'free' functions to type 
objects is not the usual way to create methods on the corresponding objects.
Instead, we can create methods much more directly through class definitions.
We can do this by using the by now familiar indentation syntax to indicate
what function definitions are part of the class definition:

class Circle:

    def __init__(self, centre=(0.0, 0.0), radius=1.0):
        self.centre = centre
        self.radius = radius

    def __repr__(self):
        return 'Circle({}, {})'.format(self.centre, self.radius)

    def circumference(self):
        return 2*self.radius*pi

This binds the functions defined inside the class definition directly to 
the Circle type. You can see two things: Firstly, the special methods are 
defined in this way exactly as regular methods. Secondly, when defining 
functions (to be methods) directly inside a class definition, we 
like to call the first parameter self. This is a pure conventation. We 
could have called it 'circle' instead, but that would confuse other Python
programmers when they read our class definition.

With this we can directly write as desired:
>>> c1 = Circle((2.0, 2.0), 1.0)
>>> c2 = Circle((2.0, 0.0), 0.9)
>>> c3 = Circle((0.0, 2.0), 3.0)

and defining a suitable function circles_intersect3(circle1, circle2) we
get the long awaited much less error prone calls:
>>> circles_intersect3(c1, c2)
False
>>> circles_intersect3(c1, c3)
True

In fact, we can now do better than that and directly define the intersects
function as method of the Circle class. You will do that in the following
task part of this activity.


6. Useful Circle Methods (0.5 marks)

In fact, there is a number of useful methods to add to our Circle class. 
Let's start with a method 'diameter' for converting the internally stored 
radius to the diameter. Finding an expressing the formula for this in 
Python is something that you can do without any mental effort. The only
challenge here is to use it do define a method. Do this by augmenting the
class definition of Circle given in the workshop template. Then you can 
call the new method as desired:
>>> c1.diameter()
2.0
>>> c2.diameter()
1.8
>>> c3.diameter()
6.0

Next, let's add a method to compute the area. I'm sure, I don't have to
remind you of the formula to compute the area of a circle, but I do it 
anyway: the area of a circle is the square of its radius times pi. Again,
the only challenge is to define is as a method:
>>> c1.area()
3.141592653589793
>>> c2.area()
2.5446900494077327
>>> c3.area()
28.274333882308138

Now it's time for creating methods that take a parameter. Create a method
contains_point(point) that returns True if and only if the circle contains
the given input point (represented by a two-element tuple):
>>> c1.contains_point((0.0, 0.0))
False
>>> c2.contains_point((0.0, 1.0))
False
>>> c3.contains_point((-1.0, 0.0))
True

Next, let's finally add the method intersects(other) that returns True if
and only if the circle intersects another circle other.
>>> c1.intersects(c2)
False
>>> c1.intersects(c3)
True
>>> c2.intersects(c3)
True

Perhaps we have squeezed out enought of the circle example and should
move on. Now it is time to write your first class from scratch. Our
will be to come up with a better representation of points: vector objects.


7. Vectors and Operator Magic (0.5 marks)

So far we have represented points simply by Python pairs (tuples with
two elements). This grouped the two-coordinates x and y into one object,
and simplified function definitions, e.g., for computing the distance
between two points, by giving a clear and reduced form of the parameter
list. On the other hand, it left us stuck with the methods of the tuple
type, althopugh there are plenty of potetentially useful methods that
could be defined for a more specific point type.

Let's explore this design possibility. We will change our view on points
slighlty by identifying them with the 2d-vectors pointing to them from
the origin of the coordinate system.

Write a class Vector for vector objects that have two float attributes
x and y. As with the Circle class, make sure objects of type Vector
can be initialised conveniently by a suitable __init__ method and have
a readable string representation in the shell (by defining __repr__):
>>> a = Vector(3.0, 4.0)
>>> b = Vector(-1.0, 1.0)
>>> a.x, a.y
(3.0, 4.0)
>>> b.x, b.y
(-1.0, 1.0)
>>> a
Vector(3.0, 4.0)
>>> b
Vector(-1.0, 1.0)

Now we can add methods that are specific to vectors to our objects by
adding them to the class definition. Let's start with a method for
computing the (Euclidean) norm of a vector, i.e., the square-root
of the sum of its squared components:
>>> a.norm()
5.0
>>> b.norm()
1.4142135623730951

An extremely useful operation defined on two vectors is the dot product.
In the next section, we will make plenty of use of this. For now, let's
define a method 'dot' for our vector objects that takes as input a 
second vector and that computes the dot-product, i.e., the sum of the
products of the two vector's x-components and y-components:
>>> a.dot(b)
1.0
>>> a.dot(Vector(2.0, 1.0))
10.0

The dot product and the norm operation together can be used to compute
the cosine of the angle between two vectors:
>>> c = Vector(0.0, 3.0)
>>> from math import acos # the arc cosine function
>>> from math import pi
>>> acos(b.dot(c) / (b.norm()*c.norm()))*180/pi
45.00000000000001

(This should be 45 degrees if it weren't for rounding errors on my 
machine.)

We could now go ahead and define other binary operations involving
vectors either as method or as 'free' functions. For instance, for the
finding the sum of two vectors we could define and use the following
function:
>>> def vector_sum(a, b):
...     return Vector(a.x+b.x, a.y+b.y)
>>> vector_sum(a, b)
Vector(2.0, 5.0)

However, there is a much nicer way to implement and use the sum and
other binary operations in Python: we can 'overload' the standard
arithmethic operators +, -, *, / to work with our new Vector class! This
will allow us to write very intuitive Python expressions that look 
more or less like we would write them on paper. For instance for adding
and subtracting vectors we can just write:
>>> a + b
Vector(2.0, 5.0)
>>> a - b
Vector(4.0, 3.0)

The way to make this operator overloading work is again by defining certain 
special 'magic' methods. In this case, we need to define the methods
'__add__(self, other)' and '__sub__(self, other)'. By adding the methods
'__mul__(self, scalar)' and '__truediv__(self, scalar)', we can also
use the standard operators '*' and '/' to multiplu or divide vectors by
scalar values:
>>> a*0.5
Vector(1.5, 2.0)
>>> a/2
Vector(1.5, 2.0)

One little problems remains here: we would also like to evaluate expressions
where the scalar is the left-operand of a product:
>>> 0.5*a
Vector(1.5, 2.0)

However, this will not work directly because Python will by default use
the '__mul__'-method of the left operand (which is a standard Python
numeric object that does not provide a multiplication method with objects of 
our custom 'Vector' type). To allow to resolve such expressions, we have
to specify a method for multiplying 'from the right', which can be done
by defining '__rmul__(self, scalar)'.

Equipped with all these operations and the knowledge of how to compute the
cosine between two vectors, we can now close this section by writing a method
for finding the orthogonal projection of one vector onto another one. The
orthogonal projection of a vector v onto another vector w is the point on the
line described by w that is closest to v. Since this point p lies on the line
described by w, it is given as a multiple (scaled version) of w. With a bit
of math (which skip here) we can convince ourselves that the factor with
which we have to scale w is the cosine of the angle between v and w times
the ratio of the norm of v to the norm of w. 

Recalling the formula for the cosine from above (dot product divided by
the two norms), it will be easy for you to write a method 
'projection(self, other)' that computes the projection of the vector self onto 
the vector other. Here are some input/output examples:

>>> a.projection(Vector(1.0, 0.0))
Vector(3.0, 0.0)
>>> a.projection(Vector(2.0, 0.0))
Vector(3.0, 0.0)
>>> a.projection(Vector(0.0, 1.0))
Vector(0.0, 4.0)
>>> a.projection(b)
Vector(-0.4999999999999999, 0.4999999999999999)

(Again, these rounding errors always pester our test cases)

8. Triangles: putting our new object skills to work (0.5 marks)

I hope the vector type defined in the last section already felt useful to
you in a vacuum, but let's demonstrate this in a last practical example,
which will also allow us to define one more class. For that we'll do a bit 
more geometry and investigate triangles.

Start by defining a class Triangle with three attributes a, b, and, c, each 
of which being a point on the plane. To keep things simple for the user's 
of our class we want to allow the creation of triangle objects with simple 
coordinate pair objects (as we have done for the circles), but we want to
convert those and store 'internally' as vector objects. That is, we want
the following behaviour:
>>> t1 = Triangle((0.0, 0.0), (1.0, 1.0), (2.0, 0.0))
>>> t2 = Triangle((0.0, 1.0), (0.0, 2.0), (1.0, 0.0))
>>> t1
Triangle((0.0, 0.0), (1.0, 1.0), (2.0, 0.0))
>>> t2
Triangle((0.0, 1.0), (0.0, 2.0), (1.0, 0.0))
>>> t1.a, t1.b, t1.c
(Vector(0.0, 0.0), Vector(1.0, 1.0), Vector(2.0, 0.0))

I recommend sketching these two triangles on a piece of paper to be 
able to better follow along the remainig computations.

Because we use our 'Vector' type to represent the vertices of a triangle
we can directly perform a lot of useful calculations with them. For instance
for obtaining the base length of our triangles (the distance between points
c and a) we can simply compute the norm of the difference vectors between
c and a as follows:
>>> base1 = t1.c - t1.a
>>> base2 = t2.c - t2.a
>>> base1, base2
(Vector(2.0, 0.0), Vector(1.0, -1.0))
>>> base1.norm(), base2.norm()
(2.0, 1.4142135623730951)

Moreover, given our projection method we can easily find the point on the base
closest to b:
>>> p1 = t1.a + (t1.b-t1.a).projection(base1)
>>> p1
Vector(1.0, 0.0)
>>> p2 = t2.a + (t2.b-t2.a).projection(base2)
>>> p2
Vector(-0.4999999999999999, 1.5)

The altitude of the triangle is then simple given by vector from this projection
p to the vertex b, and we get the height of the triangle by taking the norm:
>>> (t1.b-p1).norm()
1.0
>>> (t2.b-p2).norm()
0.7071067811865475

Putting these together, write now a method 'area(self)' that computes the area
of the triangle self. Once you have the base length and height of the triangle
this can be done easily, becaue the area of a triangle is equal to 0.5 times
the base length times the hight:
>>> t1.area()
1.0
>>> t2.area()
0.5
"""

from math import pi

def euclidean_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def circle_contains(cx, cy, r, x, y):
    return euclidean_distance(cx, cy, x, y) <=r


def circle_contains2(c, r, p):
    return euclidean_distance(c[0], c[1], p[0], p[1]) <=r


def circles_intersect(cx1, cy1, r1, cx2, cy2, r2):
    return euclidean_distance(cx1, cy1, cx2, cy2) <= r1 + r2 


def circles_intersect2(c1, r1, c2, r2):
    return euclidean_distance(c1[0], c1[1], c2[0], c2[1]) <= r1 + r2 


def circles_intersect3(c1, c2):
    return euclidean_distance(c1.centre[0], c1.centre[1], c2.centre[0], c2.centre[1]) <= c1.radius + c2.radius 


class Circle:
    """
    Represents a circle of certain radius around some centre.
    """

    def __init__(self, centre=(0.0, 0.0), radius=1.0):
        self.centre = centre
        self.radius = radius


    def __repr__(self):
        return 'Circle({}, {})'.format(self.centre, self.radius)


    def circumference(self):
        return 2*self.radius*pi


if __name__=='__main__':
    import doctest
    doctest.testmod()
