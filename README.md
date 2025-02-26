# drill4snap

**DISCLAIMER: Take great care and check your gcode files before using them! No responsibility is taken by the developer of this software!**

![file_preview](docs/header_image.jpg)

Convert Excellon drill files to GCode that can be used with the CNC/milling ability of Snapmaker devices.

Provides a small command line tool to generate one gcode file for every drill size in the drill file. These files can
be used either directly via a USB stick or loaded into the Luban software for execution.

## About

### Motivation

Although the Snapmaker should accept normal Marlin GCode, newer versions of the firmware come with a custom header 
comment. My firmware version refused to even display files that do not contain this header. The header contains
device information and the preview image encoded as a base 64 PNG image.

### Features

Small CLI tool that provides a quick way to convert Drill produced by tools such as Kicad into usable GCode.

- produces standard GCode (should work on devices other than Snapmaker too)
- preview images display required drill size for each file
- supports switching between relative and absolute coordinates (all converted into absolute coordinates)
- supports both mm and inches (switching mid-file is also supported since it is theoretically allowed)
- rejects files containing non drilling operations to protect tools from damage
- calculates required work volume and time estimate per tool run


### Limitations

Only a tiny subset of the Excellon file format is supported, since the scope of this tool is drilling only. Also note
that patterns and other more complex operations are not supported although they may be used in drilling operations.

Some other limitations:

- only tested for newest Snapmaker firmware on Snapmaker 2.0 A350
- not tested for GRBL based devices
- only tested for files produced by Kicad

## Usage

1. Install via pip:

```shell
pip install drill4snap
```

2. Generate you drill file from Kicad using the plot suboption:

![Kicad drill file options](docs/kicad_generate_drill_file.png)

3. Generate the CNC files for Snapmaker using the `drill4snap` command:

```shell
drill4snap --device s2m my_drill_file.drl
```

This will produce a CNC file with the drill diameter as postfixed for every tool in the drill file:

```
my_drill_file_0.95.cnc
my_drill_file_1.0.cnc
my_drill_file_2.3.cnc
```
4. Use either Luban or the device screen to position the tool head at the work origin and then setting the work origin.

![luban set origin](docs/set_origin.png)

5. Load the gcode files into Luban workspace or transfer them using a USB storage:

![Luban load GCode panel](docs/load_panel.png)

6. Using Luban you can now start the Job using ''

![job running](docs/running_job.png)

Let the Snapmaker do the work and enjoy!

## Credits

Based on drl2gcode (https://github.com/jes/drl2gcode) by James Stanley
which is based on
drl2gcode (https://git.nexlab.net/machinery/drl2gcode) by Franco Lanza.

Licensed under LGPL
