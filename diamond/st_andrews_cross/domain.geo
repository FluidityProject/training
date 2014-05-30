// domain for the st andrews cross validation case

pi = 3.141592653589793;
lx = 15*pi; // x-length of domain
ly = 15*pi; // y-length of domain
el = 0.6;

// box points:
Point (6) = {0, 0, 0, el};
Point (7) = {lx, 0, 0, el};
Point (8) = {lx, ly, 0, el};
Point (9) = {0, ly, 0, el};
// Left hand side
Line (5) = {9, 6};
// Top
Line (6) = {9, 8};
// bottom
Line (7) = {6, 7};
// right hand side
Line (8) = {8, 7};
// Box surface:
Line Loop(17) = {6, 8, -7, -5};
Plane Surface(17) = {17};

// Physical IDs:
//left
Physical Line(1) = {5};
//top:
Physical Line(2) = {6};
//bottom:
Physical Line(3) = {7};
//right
Physical Line(4) = {8};
// Surface
Physical Surface(105) = {17};


