
DIRS=placeholders\
	 examples\
	 running_visualisation\
	 gmsh/gmsh_tutorial_presentation\
	 numerics\
	 diamond\
	 fluidity\
	 intro\
	 header\
	 simulation_breaks\
	 parallel\

FILES=	./Piggott-FluidityTraining-051114.pdf\
	./IntroToFEM/IntroToFEMJRP.pdf\
	./numerics/numerics.pdf\
	\
	./intro/intro_day2.pdf\
	./fluidity/fluidity.pdf\
	./gmsh/gmsh_tutorial_pres.pdf\
	./diamond/diamond.pdf\
	./running_visualisation/running_visualisation.pdf\
	./parallel/parallel.pdf\
	\
	./intro/intro_day3.pdf\
	./examples/examples_combined.pdf\
	./simulation_breaks/simulation_break.pdf

default:
	for dir in $(DIRS); do \
		cd $$dir; \
		echo "Making in $$dir"; \
		make; \
		cd ../;\
	done ;
	/usr/bin/pdftk $(FILES) cat output AMCG_Fluidity_Training_2014.pdf
