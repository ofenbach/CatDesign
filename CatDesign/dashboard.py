import random

from nicegui import ui
from CatDesign.cat_design import CatDesign

class Dashboard:
    def __init__(self):
        self.ui = ui
        self.cat = CatDesign()
        self.generate_dashboard()

    def generate_dashboard(self):
        self.ui.label('Health Dashboard').style('font-size: 24px; font-weight: bold; margin-bottom: 20px;')
        self.generate_heart_rate_chart()
        self.generate_oxygen_level_chart()

    def generate_heart_rate_chart(self):
        # Generate heart rate data for the last 24 hours (random values between 60 and 100)
        heart_rate_data = [random.randint(60, 100) for _ in range(24)]
        labels = [f"{hour}:00" for hour in range(24)]  # Hourly labels for the x-axis

        self.ui.label('Heart Beats Per Minute (Last 24 Hours)').style('font-size: 18px; font-weight: bold; margin-top: 20px;')
        self.cat.bar_chart(heart_rate_data, labels, css='height: 400px; width: 100%; margin-bottom: 20px;')

    def generate_oxygen_level_chart(self):
        # Generate oxygen level data for the last 24 hours (random values between 94 and 100)
        oxygen_level_data = [random.randint(94, 100) for _ in range(24)]
        labels = [f"{hour}:00" for hour in range(24)]  # Hourly labels for the x-axis

        self.ui.label('Blood Oxygen Level (Last 24 Hours)').style('font-size: 18px; font-weight: bold; margin-top: 20px;')
        self.cat.line_chart(oxygen_level_data, labels, css='height: 400px; width: 100%; margin-bottom: 20px;')

if __name__ in {'__main__', '__mp_main__'}:

    Dashboard()
    ui.run()
