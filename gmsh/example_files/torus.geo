Point(1) = {1.5, 0.0, 0, 0.1};
Point(2) = {1.7, 0.0, 0, 0.1};
Line(1) = {1, 2};
Extrude {{0, 0, 1}, {1, 0, 0}, Pi/2} {
  Line{1};
  Layers{10};
}
Extrude {{0, 0, 1}, {1, 0, 0}, Pi/2} {
  Line{2};
  Layers{10};
}
Extrude {{0, 0, 1}, {1, 0, 0}, Pi/2} {
  Line{6};
  Layers{10};
}
Extrude {{0, 0, 1}, {1, 0, 0}, Pi/2} {
  Line{10};
  Layers{10};
}
Extrude {{0, 1, 0}, {0, 0, 0}, Pi/2} {
  Surface{5, 9, 13, 17};
  Layers{10};
}
Extrude {{0, 1, 0}, {0, 0, 0}, Pi/2} {
  Surface{39, 61, 83, 105};
  Layers{10};
}
Extrude {{0, 1, 0}, {0, 0, 0}, Pi/2} {
  Surface{193, 171, 149, 127};
  Layers{10};
}
Extrude {{0, 1, 0}, {0, 0, 0}, Pi/2} {
  Surface{215, 237, 281, 259};
  Layers{10};
}
//Outer surface
Physical Surface(366) = {206, 118, 30, 336, 272, 294, 96, 184,
                         52, 357, 250, 315, 74, 228, 162, 140};
//Inner surface
Physical Surface(367) = {104, 82, 170, 192, 60, 38, 344, 323,
                         302, 365, 280, 214, 236, 258, 126, 148};
Physical Volume(368) = {9, 12, 11, 10, 14, 16, 15, 13, 3, 2, 1, 4, 7, 6, 8, 5};
