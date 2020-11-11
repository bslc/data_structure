all:
	pdflatex --file-line-error --synctex=1 data_structure.tex
	pdflatex --file-line-error --synctex=1 data_structure.tex
	open -a "Skim" data_structure.pdf

data_structure:
	pdflatex --file-line-error --synctex=1 data_structure.tex
	open -a "Skim"  data_structure.pdf

clean: 
	rm *.aux *.log *.out *.pdf
