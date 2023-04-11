# drill4snap

**DISCLAIMER: Take great care and check your gcode files before using them! No responsibility is taken by the developer of this software!**

Convert Excellon drill files to GCode that can be used with the Snapmaker 2.0 CNC family.

Provides a small command line tool to generate one gcode file for every drill size in the drill file. These files can
be used either directly via a USB stick or loaded into the Luban software for execution.

### Motivation

Although the Snapmaker should accept normal Marlin GCode, newer versions of the firmware come with a custom header 
comment. My firmware version refused to even display files that do not contain this header. The header contains
device information and the preview image encoded as a base 64 PNG image.

### Credits

Based on drl2gcode (https://github.com/jes/drl2gcode) by James Stanley
which is based on
drl2gcode (https://git.nexlab.net/machinery/drl2gcode) by Franco Lanza.

Licensed under LGPL
