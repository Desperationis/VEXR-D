pdflatex -output-directory output/ -halt-on-error main.tex
cp Cites.bib output/
cd output/
biber main
cd ../
pdflatex -output-directory output/ -halt-on-error main.tex
