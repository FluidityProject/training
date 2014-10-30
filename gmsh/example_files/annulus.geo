Point(1) = {2.5, 0, 0, 0.5};
Point(2) = {5.25, 0, 0, 2.0};
Point(3) = {8, 0, 0, 0.5};
Line(1) = {1, 2};
Line(2) = {2, 3};
Extrude {0, 0, 14} {
  Line{1, 2};Layers{15};
}
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/2} {
  Surface{6, 10};Layers{20};
}
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/2} {
  Surface{32, 54};Layers{20};
}
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/2} {
  Surface{98, 76};Layers{20};
}
Extrude {{0, 0, 1}, {0, 0, 0}, Pi/2} {
  Surface{120, 142};Layers{20};
}
// Top
Physical Surface(185) = {93, 49, 159, 115, 71, 27, 180, 137};
// Bottom
Physical Surface(186) = {107, 151, 41, 85, 63, 19, 172, 129};
// Inner wall
Physical Surface(187) = {141, 184, 31, 75};
// Outer wall
Physical Surface(188) = {89, 111, 155, 45};
Physical Volume(189) = {4, 3, 1, 2, 8, 7, 5, 6};
