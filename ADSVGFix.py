import sys
import xml.etree.ElementTree as ET

# note that this script loses the DOCTYPE definition at the top of the file

def usageMessage():
    print("Parameter Error.\nUsage: [script] width height dpi infile outfile")
    print("\twidth = mm\n\theight = mm\n\tdpi = dots per inch\n\tinfile = svg file path\n\toutfile = svg file path")
    quit()

# process the input values
# width
try:
    mmWidth = float(sys.argv[1])
except ValueError:
    print("Could not parse width")
except IndexError:
    usageMessage()
# height
try:
    mmHeight = float(sys.argv[2])
except ValueError:
    print("Could not parse height")
except IndexError:
    usageMessage()
# dpi
try:
    dpi = float(sys.argv[3])
except ValueError:
    print("Could not parse DPI")
except IndexError:
    usageMessage()
# input file
try:
    xmlfile = str(sys.argv[4])
except ValueError:
    print("Could not parse intput file path")
except IndexError:
    usageMessage()
# output file
try:
    xmloutfile = str(sys.argv[5])
except ValueError:
    print("Could not parse output file path")
except IndexError:
    usageMessage()

if mmWidth <= 0. or mmHeight <= 0. or dpi <= 0.:
    print("A parameter value is less than or equal to zero")
    usageMessage()

try:
    tree = ET.parse(xmlfile)
except FileNotFoundError:
    print("Could not open the file");
    usageMessage()

# svg should be the root element
svg = tree.getroot()

# display the values that we will be overwriting
if None != svg.get('width'):
    print('Width: ' + svg.get('width'))
if None != svg.get('height'):
    print('Height: ' + svg.get('height'))
if None != svg.get('viewBox'):
    print('viewBox: ' + svg.get('viewBox'))

# set the correct attributes
svg.set('width', str(mmWidth) + 'mm');
svg.set('height', str(mmHeight) + 'mm');
mmPerInch = 25.4
pixelWidth = mmWidth / mmPerInch * dpi
pixelHeight = mmHeight / mmPerInch * dpi
svg.set('viewBox', '0 0 {:.3f} {:.3f}'.format(pixelWidth, pixelHeight) )

# get rid of ns0 at the start of every element name
ET.register_namespace("", "http://www.w3.org/2000/svg")

# output svg file
tree.write(xmloutfile, "UTF-8", xml_declaration=True, default_namespace=None)
