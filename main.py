import flet as ft
from token_api import get_weather_data
from city import cidade, get_city
from datetime import datetime
import threading
import time

# Convert api data from fahrenheit to celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

# Dinamicaly update the clock
def update_date_time():
    global current_date, current_time
    while True:
        current_date_time = datetime.now()
        current_date = current_date_time.strftime("%d/%m")
        current_time = current_date_time.strftime("%H:%M")
        time.sleep(1)

def main(page: ft.Page):

    # Go back
    page.go("/")


    # Data converted to celsius
    weather_data, weather_png, weather_hint, city = get_weather_data(get_city())
    tempCelsius = convert_to_celsius(weather_data["main"]["temp"])
    fellslikeCelsius = convert_to_celsius(weather_data["main"]["feels_like"])
    minCelsius = convert_to_celsius(weather_data["main"]["temp_min"])
    maxCelsius = convert_to_celsius(weather_data["main"]["temp_max"])
    humidity = weather_data["main"]["humidity"]

    # Application colors
    BG = "#809BCE"
    FG = "#95B8D1"
    FWG = "#B8E0D2"
    #BL = "#252323"

    page.title = "Weather App"
    
    # First screen and top icons
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
                            ft.Container(on_click=lambda _: page.go("select_city_screen"), content=ft.Icon(ft.icons.SEARCH, color="white")),
                            ft.Container(content=ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED, color="white")),
                            ]
                        )
                    ]
                ),
                # Welcome mensage
                ft.Container(height=10),
                ft.Container(
                    padding=ft.padding.only(left=20),
                    content=ft.Text(
                        value="Seja bem vindo!",
                        weight=ft.FontWeight.BOLD,
                        size=35,
                        color="white",
                    )
                ),
                # Weather disclaimer
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value=f"Hoje o clima está {weather_hint}",
                                color="white",
                                weight=ft.FontWeight.W_700,
                                size=15,
                            )
                        ]
                    )
                ),
                # Clock and date information
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value=f"{current_time} | {current_date}",
                                weight=ft.FontWeight.W_800,
                                size=40,
                                color="white",
                            )
                        ]
                    )
                ),
                # Weather png and temperature
                ft.Container(
                    padding=ft.padding.only(top=20),
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                width=140,
                                height=140,
                                src=f"{weather_png}"
                            ),
                            ft.Text(
                                value=f" {tempCelsius:.0f} ºC",
                                size=55,
                                weight=ft.FontWeight.BOLD,
                                color="white"
                            )
                        ]
                    )
                ),
                # City selected information
                ft.Container(
                    padding=ft.padding.only(top=20),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
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
                # Weather card information
                ft.Container(
                    width=310,
                    height=170,
                    border_radius=20,
                    bgcolor="#25232300",
                    content=ft.Container(
                        padding=ft.padding.only(top=25, right=5, bottom=110),
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                value=f"Mínima: {minCelsius:.0f} ºC   |   Máxima: {maxCelsius:.0f} ºC",
                                                weight=ft.FontWeight.W_600,
                                                size=18,
                                                color="white",
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    padding=ft.padding.only(top=10, right=10),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                value=f"Sensação térmica: {fellslikeCelsius:.0f} ºC",
                                                weight=ft.FontWeight.W_600,
                                                size=18,
                                                color="white",
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    padding=ft.padding.only(top=10, right=10),
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(
                                                value=f"Umidade: {humidity}%",
                                                weight=ft.FontWeight.W_600,
                                                size=18,
                                                color="white",
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                )
            ]
        )
    )

    container = ft.Container(
        width=350,
        height=730,
        bgcolor=BG,
        border_radius=20,
        content=ft.Stack(
            controls=[
                first_screen,
            ]
        )
    )

    pages = {
        "/":ft.View(
            "/",
            [
                container
            ],
        ),
    }

    def route_change(route):
        page.views.clear()
        page.views.append(pages[page.route])

    page.on_route_change = route_change
    page.go(page.route)

    page.add(first_screen)

if __name__ == "__main__":

    current_date = ""
    current_time = ""

    thread = threading.Thread(target=update_date_time)
    thread.daemon = True
    thread.start()

    ft.app(target=main)
