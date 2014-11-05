PDFS=diamond.pdf

default: $(PDFS)

.SUFFIXES: .tex .pdf

input:
	echo "Building PDFs"
	pdflatex -shell-escape diamond.tex

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.pdf

