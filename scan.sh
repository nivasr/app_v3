#fileName, fileMode, Resolution, topLeftX, topLeftY, bottomRightX, bottomRightY
fileName=$1
format=$2
scanMode=$3
resolution=$4
unit=$5
l=$6
t=$7
width=$8
height=$9

if [ -z "$l" ] || [ -z "$t" ] || [ -z "$width" ] || [ -z "$height" ] ; then
    echo "calling scanimage --format=tiff --mode=$scanMode --resolution=${resolution}dpi > ${fileName}.tiff";
    scanimage --format=tiff --mode=$scanMode --resolution=${resolution}dpi > ${fileName}.tiff;
else
    echo "calling scanimage --format=tiff --mode=$scanMode -l $l -t $t -x $width -y $height --resolution=${resolution}dpi > ${fileName}.tiff";
    scanimage --format=tiff --mode=$scanMode -l $l -t $t -x $width -y $height --resolution=${resolution}dpi > ${fileName}.tiff;
fi

#tiff2pdf -o ${fileName}.pdf ${fileName}.tiff

#http://www.imagemagick.org
#if ["$format" != "jpg"] && ["$format" != "png"] && ["$format" != "pdf"] && ["$format" != "tiff"]; then
#    #not a known format, default to pdf
#    format= "pdf"
#fi
echo "[scan.sh] converting to " $format
convert ${fileName}.tiff ${fileName}.${format}
