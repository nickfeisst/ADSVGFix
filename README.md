# ADSVGFix

A Python script to convert an SVG file, exported from Affinity Designer, to use millimetres instead of pixels.

The script requires a width, height, and DPI value, as well as an input and output file path (they can be the same if you feel confident enough to overwrite your file). It adds/replaces the width, height, and viewBox attributes of the root svg element.

Example usage:

'python3 ADSVGFix.python 30.48 128.5 96 InputFile.svg OutputFile.svg'
