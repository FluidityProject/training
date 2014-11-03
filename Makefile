
DIRS=placeholders\
	 examples\
	 running_visualisation\
	 gmsh/gmsh_tutorial_presentation\
	 numerics\
	 diamond\
	 fluidity\
	 intro\
	 header

FILES=	./intro/intro.pdf\
	./IntroToFEM/IntroToFEMJRP.pdf\
	./DavidsFEMDaySlides.pdf \
	./numerics/numerics.pdf\
	\
	./intro/intro_day2.pdf\
	./fluidity/fluidity.pdf\
	./diamond/set_up.pdf\
	./gmsh_tutorial_pres.pdf\
	./running_visualisation/running_visualisation.pdf\
	\
	./intro/intro_day3.pdf\
	./examples/examples_combined.pdf\


default:
	for dir in $(DIRS); do \
		cd $$dir; \
		echo "Making in $$dir"; \
		make; \
		cd ../;\
	done ;
	/usr/bin/pdftk $(FILES) cat output AMCG_Fluidity_Training_2014.pdf
