import flet as ft

def get_city():
        city = "São Paulo"
        return city

def cidade(page: ft.Page):
    # Application colors
    BG = "#809BCE"
    FG = "#95B8D1"
    FWG = "#B8E0D2"

    # Get city input
    cidade = ft.Ref[ft.TextField]()
    print(cidade)

    # City selection screen
    select_city_screen = ft.Container(
        width=350,
        height=730,
        bgcolor=FG,
        border_radius=20,
        content=ft.Column(
            controls=[
                ft.Container(
                        margin=ft.margin.only(top=50, left=20),
                        content=ft.Icon(ft.icons.ARROW_BACK, color="white"),
                        on_click=lambda _: page.go('/')
                ),
                ft.Container(
                    padding=ft.padding.only(top=180),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value="Selecione sua cidade",
                                color="white",
                                size=28,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ]
                    )
                ),
                ft.Container(
                    on_click=get_city(),
                    padding=ft.padding.only(top=20),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[ft.TextField(
                                ref=cidade,
                                label="Cidade",
                                color="white",
                                prefix_icon=ft.icons.HOUSE,                            
                                border_color="white",
                                border_radius=20,
                                width=290,
                            )   
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=20),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton(
                                width=290,
                                height=40,
                                text="Selecionar",
                                bgcolor="white",
                                color=FG,
                            )
                        ]
                    )
                ),
            ]
        )
    )
    return select_city_screen, get_city
