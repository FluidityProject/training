input:
	gmsh -2 -o stommel.msh src/stommel.geo
	gmsh2triangle --2d stommel.msh

clean:
	rm -f *.node *.ele *.edge *.msh *.vtu *.log* *.err* *.stat *dump*
