#!/usr/bin/env python3

import flet
from flet import (
    Column,
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerUploadEvent,
    FilePickerUploadFile,
    Page,
    ProgressRing,
    Ref,
    Row,
    Text,
    Theme,
    icons,
)
from typing import Dict

def main(page: Page):
    page.title = "UltraTrace"
    # page.bgcolor = "#FFFFFF"
    page.fonts = {"Noto Sans": "https://fonts.google.com/download?family=Noto%20Sans"}
    page.theme = Theme(font_family = "Noto Sans")
    page.theme = Theme(color_scheme_seed="blue")

    prog_bars: Dict[str, ProgressRing] = {}
    files = Ref[Column]()
    upload_button = Ref[ElevatedButton]()

    def file_picker_result(e: FilePickerResultEvent):
        upload_button.current.disabled = True if e.files is None else False
        prog_bars: Dict[str, ProgressRing] = {}
        prog_bars.clear()
        files.current.controls.clear()
        if e.files is not None:
            for f in e.files:
                prog = ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(Row([prog, Text(f.name)]))
        page.update()

    def on_upload_progress(e: FilePickerUploadEvent):
        prog_bars[e.file_name].value = e.progress
        prog_bars[e.file_name].update()

    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

    def upload_files(e):
        uf = []
        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                uf.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(uf)

    # hide dialog in a overlay
    page.controls.append(
        file_picker
    )

    page.add(
        ElevatedButton(
            "Open a recording...",
            icon=icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files(allow_multiple=False)
        )
    )
    page.update()

flet.app(target=main)