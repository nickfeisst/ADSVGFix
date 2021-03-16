# ADSVGFix

A Python script to convert an SVG file, exported from Affinity Designer, to use millimetres instead of pixels.

The script requires a width, height, and DPI value, as well as an input and output file path (they can be the same if you feel confident enough to overwrite your file). It adds/replaces the width, height, and viewBox attributes of the root svg element.

Example usage:

```Shell
python3 ADSVGFix.python 30.48 128.5 96 InputFile.svg OutputFile.svg
```

Example shell script for processing multiple files:

```Shell
#!/bin/sh
# chmod 755 process.sh
# command + path to script
fix="python3 ../../ADSVGFix/ADSVGFix.python"

# input parameter array
pa[0]="30.48 128.5 96 ./FaderProcessor-Dark.svg ../res/FaderProcessor-Dark.svg"
pa[1]="30.48 128.5 96 ./FaderProcessor-Light.svg ../res/FaderProcessor-Light.svg"

# process the files
for i in "${pa[@]}"
do
	echo $fix $i;
	echo $(eval $fix $i)
done
```
