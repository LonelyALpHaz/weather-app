import flet as ft
import requests

api_key = "0c33e0a7fefd189dc02f05997704299f"

city = "Campina Grande"

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

tempCelsius = (weather_data.json()["main"]["temp"] - 32) / 1.8 
fellslikeCelsius = (weather_data.json()["main"]["feels_like"] - 32) / 1.8
minCelsius = (weather_data.json()["main"]["temp_min"] - 32) /1.8
maxCelsius = (weather_data.json()["main"]["temp_max"] - 32) / 1.8

#print(weather_data.json())

def main(page: ft.Page):

    BG = "#809BCE" #2B2D42 #809BCE
    FG = "#95B8D1"
    FWG = "#B8E0D2"
    TEAL = "#D6EADF"
    BL = "#252323"

    page.title = "Weather App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    first_screen = ft.Container(
        width=350,
        height=730,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[BG, FG, FWG]
        ),
        border_radius=20,
        padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
        content=ft.Column(
            controls=[ft.Row(alignment="SpaceBetween",
                controls=[
                    ft.Container(content=ft.Icon(ft.icons.MENU_ROUNDED, color="White")),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.icons.SEARCH, color="White"),
                            ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED, color="White")
                            ]
                        )
                    ]
                ),
                ft.Container(height=20),
                ft.Text(
                    value="Seja bem vindo!",
                    weight=ft.FontWeight.BOLD,
                    size=30,
                    color="White",
                ),
                ft.Text(
                    value=f"Hoje o clima está {'ENSOLARADO!'}",
                    color="White",
                ),
                ft.Container(
                    padding=ft.padding.only(top=20, left=70),
                    content=ft.Image(
                        width=150,
                        height=150,
                        src="assets/weather_icons_dovora_interactive/PNG/512/day_clear.png"
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=10, left=50),
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.LOCATION_PIN, color="white"),
                            ft.Text(
                                value=f"{city}",
                                weight=ft.FontWeight.BOLD,
                                size=20
                            )
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=5, left=75),
                    content=ft.Text(
                        value=f"Temperatura: {tempCelsius} ºC",
                        weight=ft.FontWeight.W_500,
                        size=15,
                    ),
                ),
                ft.Container(
                    width=310,
                    height=200,
                    border_radius=20,
                    margin=ft.margin.only(top=25),
                    bgcolor="#25232300",
                    content=ft.Container(
                        padding=ft.padding.only(left=20, bottom=7),
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    value=f"Mínima: {minCelsius} ºC   |",
                                    weight=ft.FontWeight.W_600,
                                    size=15,
                                ),
                                ft.Text(
                                    value=f"Máxima: {maxCelsius} ºC",
                                    weight=ft.FontWeight.W_600,
                                    size=15,
                                )
                            ]
                        )
                    )
                )
            ]
        )
    )

    page.add(first_screen)

if __name__ == "__main__":
    ft.app(target=main)
