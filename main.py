import flet 
from flet import Page, icons, IconButton, Text, Row

def main(page:Page):
    page.title="Counter App"
    page.vertical_alignment="center"

    text_zone = Text(value=0, text_align="center")
    
    def add_func(e):
        text_zone.value += 1
        text_zone.update()

    def minus_func(e):
        text_zone.value -= 1 
        text_zone.update()

    add_btn = IconButton(icon=icons.ADD, on_click=add_func)
    minus_btn = IconButton(icon=icons.REMOVE, on_click=minus_func)

    page.add(
        Row(
            controls=[
                minus_btn,
                text_zone,
                add_btn,
            ],
            alignment="center",
            vertical_alignment="center"
        )
    )
    page.update()


flet.app(target=main)