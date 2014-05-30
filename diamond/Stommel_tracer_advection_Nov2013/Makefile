input:
	gmsh -2 -o Stommel2_adapt.msh src/Stommel2_adapt.geo
	gmsh2triangle --2d Stommel2_adapt.msh
	gmsh -2 -o Stommel2_A.msh src/Stommel2_A.geo
	gmsh2triangle --2d Stommel2_A.msh

clean:
	rm -f *.node *.ele *.edge *.msh *.vtu *.log* *.err* *.stat *dump*
