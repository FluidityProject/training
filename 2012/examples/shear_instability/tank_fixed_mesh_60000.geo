Point(1)={-100,10,0};
Point(2)={100,10,0};
Point(3)={100,0,0};
Point(4)={100,-10,0};
Point(5)={-100,-10,0};
Point(6)={-100,0,0};

Line(1)={1,2};
Line(2)={2,3};
Line(3)={3,4};
Line(4)={4,5};
Line(5)={5,6};
Line(6)={6,1};

Line(7)={3,6};

Line Loop(1)={1,2,3,4,5,6};

Plane Surface(1)={1};

Periodic Line (2)= {-6};
Periodic Line (3)= {-5};


Physical Surface(1)={1};


Field[1]=MathEval;
Field[1].F='0.01*(0.1*y)*(0.1*y)+0.3';

Background Field=1;

Physical Line(1)={1};
Physical Line(2)={2};
Physical Line(3)={3};
Physical Line(4)={4};
Physical Line(5)={5};
Physical Line(6)={6};

