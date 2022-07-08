TEX=pdflatex
SRC=$(wildcard *.tex)
OBJ=$(SRC:.tex=.pdf)

all: $(OBJ)
	@make clean

%.pdf: %.tex
	$(TEX) $< -output-format=pdf

clean: 
	rm -fv *.aux *.log *.toc *.blg *.bbl *.out *.bcf

.PHONY: all clean
