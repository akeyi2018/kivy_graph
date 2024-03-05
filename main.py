
# import os
# os.environ["KIVY_NO_CONSOLELOG"] = "1"
import datetime

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from data_config import Config

#Build our app

class Matty(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.create_blood()

        box=self.ids.box
        box.add_widget(FigureCanvasKivyAgg(self.plt.gcf()))

    def get_json_data(self):
        ins = Config({})
        data = ins.get_json_info()
        # リストの最初の要素を使用して、すべてのキーを抽出します。
        keys = data[0].keys()

        # 各キーに対して、リストを作成し、そのキーの値をリストに追加します。
        data_by_key = {key: [item[key] for item in data] for key in keys}
        return data_by_key


    def create_blood(self):
      
        data = self.get_json_data()

        # Example blood pressure data sets
        blood_pressure_data_set1 = data['high']
        blood_pressure_data_set2 = data['low']
        weight_data = data['weight']

        

        

        # Create a list of dates from the start_date to the end_date
        dates = [datetime.datetime.strptime(date_string, "%Y-%m-%d").date() for date_string in data['date']]

        # Plot the first set of blood pressure data
        plt.plot_date(dates, blood_pressure_data_set1, marker='o', linestyle='--', label='High Blood Pressure')

        # Annotate the plotted values
        for date, value in zip(dates, blood_pressure_data_set1):
            plt.annotate(str(value), (date, value), textcoords="offset points", xytext=(-10,10), ha='center')

        # Plot the second set of blood pressure data
        plt.plot_date(dates, blood_pressure_data_set2, marker='o', linestyle='--', label='Low Blood Pressure')

        #   # Annotate the plotted values
        for date, value in zip(dates, blood_pressure_data_set2):
            plt.annotate(str(value), (date, value), textcoords="offset points", xytext=(-10,10), ha='center')

        #   # Add annotations for normal values
        plt.axhline(y=130, color='r', linestyle='--', label='Normal Upper Limit: 130')
        plt.axhline(y=80, color='b', linestyle='--', label='Normal Lower Limit: 80')
        
        plt.legend(loc='upper left')

        # Set labels and title
        plt.title('Blood Pressure Measurements')
        plt.xlabel('Measurement Number')
        plt.ylabel('Blood Pressure (mmHg)')
        
        plt.ylim(70, 180)

        ax2 = plt.gca().twinx()

        ax2.plot_date(dates, weight_data, marker='o', linestyle='--', label='weight', color='g')
        for date, value in zip(dates, weight_data):
            ax2.annotate(str(value), (date, value), textcoords="offset points", xytext=(15,-10), ha='center')
        
        ax2.axhline(y=70, color='g', linestyle='--', label='Normal weight: 70')

        # ax2.legend()
        ax2.legend(loc='upper right')

        # ax2.set_ylabel('Weight (kg)')
        ax2.set_ylabel('Weight (kg)', rotation=90, labelpad=15)
        ax2.yaxis.set_label_position('right')
        ax2.set_ylim(65,85)


        # Format the x-axis to display dates
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gcf().autofmt_xdate()

        self.plt = plt

    def saveit(self):
        td = datetime.date.today().strftime("%Y-%m-%d_%H_%M_%S")
        self.plt.savefig(f'graph_{td}.png') 
        print('finish Save it to PNG.')
   
    def create_data(self):
        # get data
        data = {
            "dt": datetime.date.today().strftime("%Y-%m-%d"),
            "high": int(self.ids.bld_high_in.text),
            "low": int(self.ids.bld_low_in.text)
        }
        ins = Config(data)
        ins.add_new_data()
        print('finish add new data')


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Blue"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Light"
        Builder.load_file('mappy.kv')
        return Matty()

MainApp().run()