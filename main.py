import flet as ft
from datetime import datetime
import requests

api_key = "0c33e0a7fefd189dc02f05997704299f"

city = "Campina Grande"

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

tempCelsius = (weather_data.json()["main"]["temp"] - 32) / 1.8 
fellslikeCelsius = (weather_data.json()["main"]["feels_like"] - 32) / 1.8
minCelsius = (weather_data.json()["main"]["temp_min"] - 32) / 1.8
maxCelsius = (weather_data.json()["main"]["temp_max"] - 32) / 1.8
humidity = weather_data.json()["main"]["humidity"]

current_date_time = datetime.now()
current_date = current_date_time.strftime("%d/%m")
current_time = current_date_time.strftime("%H:%M")

print(weather_data.json())

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
                    ft.Container(content=ft.Icon(ft.icons.MENU_ROUNDED, color="white")),
                    ft.Row(
                        controls=[
                            ft.Icon(ft.icons.SEARCH, color="white"),
                            ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED, color="white")
                            ]
                        )
                    ]
                ),
                ft.Container(height=10),
                ft.Container(
                    padding=ft.padding.only(left=20),
                    content=ft.Text(
                        value="Seja bem vindo!",
                        weight=ft.FontWeight.BOLD,
                        size=35,
                        color="white",
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=30),
                    content=ft.Text(
                        value=f"Hoje o clima está {'ENSOLARADO'} ☀️",
                        color="white",
                        weight=ft.FontWeight.W_700,
                        size=15,
                    ),
                ),
                ft.Container(
                    padding=ft.padding.only(left=30),
                    content=ft.Text(
                        value=f"{current_time} | {current_date}",
                        weight=ft.FontWeight.W_800,
                        size=40,
                        color="white",
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=20),
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                width=140,
                                height=140,
                                src="assets/weather_icons_dovora_interactive/PNG/512/day_clear.png"
                            ),
                            ft.Text(
                                value=f" {tempCelsius:.0f} ºC",
                                size=55,
                                weight=ft.FontWeight.BOLD,
                                color="white"
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.only(top=20, left=55),
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.LOCATION_PIN, color="white"),
                            ft.Text(
                                value=f"{city}",
                                weight=ft.FontWeight.BOLD,
                                size=20,
                                color="white",
                            )
                        ]
                    )
                ),
                ft.Container(height=10),
                ft.Container(
                    width=310,
                    height=170,
                    border_radius=20,
                    bgcolor="#25232300",
                    content=ft.Container(
                        padding=ft.padding.only(top=25, left=15, bottom=110),
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    value=f"Mínima: {minCelsius:.0f} ºC   |   Máxima: {maxCelsius:.0f} ºC",
                                    weight=ft.FontWeight.W_600,
                                    size=18,
                                    color="white",
                                ),
                                ft.Container(
                                    padding=ft.padding.only(top=10, left=35),
                                    content=ft.Text(
                                            value=f"Sensação térmica: {fellslikeCelsius:.0f} ºC",
                                        weight=ft.FontWeight.W_600,
                                        size=18,
                                        color="white",
                                    )
                                ),
                                ft.Container(
                                    padding=ft.padding.only(top=10, left=70),
                                    content=ft.Text(
                                        value=f"Umidade: {humidity}%",
                                        weight=ft.FontWeight.W_600,
                                        size=18,
                                        color="white",
                                    )
                                )
                            ]
                        )
                    )
                ),
            ]
        )
    )

    page.add(first_screen)

if __name__ == "__main__":
    ft.app(target=main)
