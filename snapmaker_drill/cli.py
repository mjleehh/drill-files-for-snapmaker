#!/usr/bin/env python3

from pathlib import Path

import typer

from snapmaker_drill.parser import ExcellonFileParser
from snapmaker_drill.writer import GcodeWriter


def main(
        safe_height: float = typer.Option(25.0, help='travel height above work origin in mm'),
        spindle_power: int = typer.Option(100, help='percentage of maximum spindle power'),
        drill_file: str = typer.Argument(..., help='Excellon .drl file to convert'),
):
    """
    Convert Excellon drill files to gcode that can be used with the Snapmaker 2.0 CNC family.

    Based on drl2gcode (https://github.com/jes/drl2gcode) by James Stanley
    which is based on
    drl2gcode (https://git.nexlab.net/machinery/drl2gcode) by Franco Lanza.

    Licenced under LGPL
    """

    result = ExcellonFileParser(in_file_path=drill_file).parse()
    for tool_job in result.values():
        GcodeWriter(tool_job, spindle_power=spindle_power, safe_height=safe_height).write(Path(drill_file).stem)


def cli():
    typer.run(main)
