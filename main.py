import os
import tkinter as tk
from view.main_view import MainView
from controller.meteo_controller import MeteoController


def main():
    airports_filepath = 'airports.json'
    airports = load_airports(airports_filepath)
    plot_airports(airports)

if __name__ == "__main__":
    main()
