import flet as ft
import cv2 as cv
from CameraUpdate import Update

def main(page: ft.Page):


    # cap = cv.VideoCapture(1)
    # current_frame = None

    vd_card = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.ListTile(
                    title=ft.Text("Web Cam"),
                    subtitle=ft.Text("live vídeo")
                ),
                ft.Row([
                    Update()
                ])
            ]),padding=20
        )
    )

    def select_action(option):
        if option == 0:
            start_cam()
        elif option == 1:
            ...
        elif option == 2:
            ...
                

    def start_cam():
        

        while True:
            ret,frame = cap.read()

            if not ret:
                break

            cv.imshow('scream',frame)
            # current_frame = frame
            # current_frame.update()
            
            

            if cv.waitKey(1) & 0xff == ord('q'):
                break
            

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="First"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Settings"),
            ),
        ],
        on_change=lambda e: select_action(e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([vd_card ], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )

    

ft.app(target=main)