combine:
	pdftk examples_CFD.pdf examples_GFD.pdf Example_Slides.pdf cat output AMCG_Fluidity_Training_Examples_2012.pdf

default:examplescfd examplesgfd

examplescfd:
	pdflatex examples_CFD
	pdflatex examples_CFD
        
examplesgfd:
	pdflatex examples_GFD
	pdflatex examples_GFD
        
examplesdstl:
	pdflatex examples_DSTL
	pdflatex examples_DSTL
clean:
	rm *.aux *.log *.nav *.out *.snm *.toc
