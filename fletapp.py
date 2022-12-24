#!/usr/bin/env python3

import flet
from flet import (
    Card,
    Column,
    Dropdown,
    dropdown,
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerUploadEvent,
    FilePickerUploadFile,
    Icon,
    icons,
    ListTile,
    ListView,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    ProgressRing,
    Ref,
    ResponsiveRow,
    Row,
    Slider,
    Text,
    TextField,
    TextThemeStyle,
    Theme,
)
from typing import Dict


def main(page: Page):
    page.title = "UltraTrace"
    # page.bgcolor = "white"
    page.fonts = {"Noto Sans": "https://fonts.google.com/download?family=Noto%20Sans"}
    page.theme = Theme(font_family="Noto Sans")
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

    # hide dialog in a overlay
    page.controls.append(file_picker)

    # layout for the page
    page.add(
        Row([
            Column([
                Text("File:", style=TextThemeStyle.TITLE_MEDIUM),
                Row([
                    ElevatedButton(
                        content=Icon(icons.ARROW_LEFT)
                    ),
                    TextField(
                        hint_text="File name"
                    ),
                    ElevatedButton(
                        content=Icon(icons.FILE_OPEN),
                        on_click=lambda _: file_picker.pick_files(allow_multiple=False)
                    ),
                    ElevatedButton(
                        content=Icon(icons.ARROW_RIGHT)
                    ),
                ]),
                Text("Frame:"),
                Slider(min=0, max=100, label="{value}%"),
                Text("Layers:", style=TextThemeStyle.TITLE_MEDIUM),
                ListView([
                    Text("Tongue"),
                    Text("Velum")
                ]),
                Text("Traces:", style=TextThemeStyle.TITLE_MEDIUM),
                Row([
                    ElevatedButton(
                        # "Set as default",
                        content=Icon(icons.SETTINGS)
                        # on_click=
                    ),
                    ElevatedButton(
                        # "Select all",
                        content=Icon(icons.SELECT_ALL)
                        # on_click=
                    ),
                    ElevatedButton(
                        # "Copy",
                        content=Icon(icons.COPY)
                        # on_click=
                    ),
                    ElevatedButton(
                        # "Paste",
                        content=Icon(icons.PASTE)
                        # on_click=
                    )
                ]),
                Row([
                    ElevatedButton(
                        # "Recolor",
                        content=Icon(icons.COLORIZE)
                        # on_click=
                    ),
                    ElevatedButton(
                        # "Clear",
                        content=Icon(icons.CLEAR)
                        # on_click=
                    ),
                    ElevatedButton(
                        # "New",
                        content=Icon(icons.PLUS_ONE)
                        # on_click=
                    ),
                    ElevatedButton(
                        # "Rename",
                        content=Icon(icons.EDIT)
                        # on_click=
                    )
                ]),
                Row([
                    ElevatedButton(
                        # "Rewind",
                        content=Icon(icons.FAST_REWIND)
                        # on_click=
                    ),
                    ElevatedButton(
                        # "Stop",
                        content=Icon(icons.STOP)
                        # on_click=
                    ),
                    ElevatedButton(
                        # "Play",
                        content=Icon(icons.PLAY_ARROW)
                        # on_click=
                    ),
                    ElevatedButton(
                        # "Fast forward",
                        content=Icon(icons.FAST_FORWARD)
                        # on_click=
                    )
                ]),
                # Column([
                #     # write a for loop that adds each landmark
                #     ListTile(
                #         title=Text("Tongue"),
                #         trailing=PopupMenuButton(
                #             icon=icons.MORE_VERT,
                #             items=[
                #                 PopupMenuItem(text="Set as default"),
                #                 PopupMenuItem(text="Rename"),
                #             ],
                #         ),
                #         dense=True
                #     ),
                #     TextField(
                #         label="New landmark:",
                #         # on_click add to landmarks dict
                #     )
                # ]),
            ])
        ])
    )
    page.update()


flet.app(target=main)
