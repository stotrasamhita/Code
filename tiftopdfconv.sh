#! /bin/bash

# Required packages:
# pdftk (combining docs)
# libtiff-tools (converting tiff to pdf via tiff2pdf)

# convert tiff files to pdf using tiff2pdf:
echo "Making pdf directory, 'pdf_output'"
mkdir pdf_output

echo "*****************************"
echo "Begin converting tiff to pdf:"
for f in *.tif; do
	echo "Processing file $f"
	tiff2pdf -o pdf_output/output.pdf $f
	pdftk pdf_output/combined.pdf pdf_output/output.pdf cat output pdf_output/combined_mid.pdf
	mv pdf_output/combined_mid.pdf pdf_output/combined.pdf
done
echo "Finished converting tiff to pdf."

echo "*****************************"
#echo "Begin combining pdf docs."
#echo "Combining 1 and 2."
#pdftk pdf_output/1.pdf pdf_output/2.pdf cat output pdf_output/combined.pdf

#for a in `seq 3 34`; do
#	echo "Completing unit $a of 34"
#	pdftk pdf_output/combined.pdf pdf_output/$a.pdf cat output pdf_output/combined_mid.pdf
#	mv pdf_output/combined_mid.pdf pdf_output/combined.pdf