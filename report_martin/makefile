##
## macrodefinitions 
##
LATEX        = pdflatex
BIBTEX       = bibtex
SRC          = report 
## MAKEINDEX    = makeindex
REMOVE       = *.tex~ *.aux *.glo *.gls *.cb *.dvi *.log *.toc *.lof *.bbl *.blg *.ilg *.cb? *.idx *.lof *.ilg *.nls *.nlo *.out *.pdfsync *.nav *.snm *.acn *.lot *.xdy

##
## rules
##
all : 
	$(LATEX)  $(SRC)
##	$(MAKEINDEX) $(SRC).nlo -s nomencl.ist -o $(SRC).nls
	$(BIBTEX) $(SRC)||true
	$(LATEX)  $(SRC) 
	$(LATEX)  $(SRC)

clean :
	rm -f $(REMOVE)
