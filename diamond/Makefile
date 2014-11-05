PDFS=diamond.pdf

default: $(PDFS)

.SUFFIXES: .tex .pdf

.tex.pdf:
	echo "Building PDFs"
	pdflatex -shell-escape $<
	if fgrep "Rerun to" $*.log; then $(MAKE) --assume-new $< $@;fi
	if fgrep "There were undefined"  $*.log;\
		then bibtex $*; \
		$(MAKE) NOBIBTEX=true --assume-new $< $@;fi
	pdflatex -shell-escape $<

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.pdf

