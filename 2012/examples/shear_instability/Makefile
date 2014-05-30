clean:
	rm -rf  *.vtu *.log *.node *.ele *.face *.vtu matrixdump* *.pyc *.msh fluidity.* *.dat *.perioidised.flml *_np4.flml *.halo *.stat

input: clean
	gmsh -2 tank_low_res.geo
	gmsh -2 tank.geo
	python gn2.py
	gmsh -2 tank_int.geo
	gmsh -2 tank_fixed_mesh_60000.geo

run:
	low_res
	travelling_wave
	high_res
	fixed_mesh


low_res:
	${BINPREFIX}periodise shear_low_res.flml
	${BINPREFIX}fluidity -v2 -l shear_low_res_periodised.flml

travelling_wave:
	${BINPREFIX}periodise travelling_wave.flml
	${BINPREFIX}fluidity -v2 -l travelling_wave_periodised.flml

high_res:
	${BINPREFIX}periodise shear_low_res.flml
	${BINPREFIX}fluidity -v2 -l shear_high_res_periodised.flml

fixed_mesh:
	${BINPREFIX}periodise shear_fixed_mesh.flml
	mpirun -n 4 ${BINPREFIX}flredecomp -i 1 -o 4 shear_fixed_mesh_periodised shear_fixed_mesh_periodised_decomped_np4
	mpirun -n 4 ${BINPREFIX}fluidity -v2 -l shear_fixed_mesh_periodised_decomped_np4.flml