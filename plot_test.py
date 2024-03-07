import matplotlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.lang import Builder
from kivy.config import Config
import random
import pandas as pd
import numpy as np

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']


from data_config import CsvReader

class MyRootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(MyRootWidget, self).__init__(**kwargs)
        self.fig, self.ax = plt.subplots(2,1)
       
        # self.data_counter = 0
        self.view_span = 30

        # GDPデータ読み込み
        self.get_gdp_data()
        self.ct = self.data_count

        Clock.schedule_interval(self.update_02, 0.1)
        

        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(self.fig))
        # self.update_legend()


    def get_gdp_data(self):
        ins = CsvReader()
        df = ins.get_gdp_df()
        self.data_length = len(df)
        self.data_count = self.data_length - self.view_span
        self.x_axis = df['年']
        self.y_japan = df['日本']
        self.y_china = df['中国']
        self.y_us = df['アメリカ']

        # print(y)

    # argsはClock描画用の引数として渡される
    def update_02(self, *args):
        
        if self.ct > self.data_length:
            pass            
        else:
            
            x = self.x_axis[self.data_count:self.ct]
            y1 = self.y_japan[self.data_count:self.ct]
            y2 = self.y_china[self.data_count:self.ct]
            y3 = self.y_us[self.data_count:self.ct]

            self.ax[0].set_title('GDP Between JP and CN AND US')

            width = 0.6
            # x = np.arange(len(labels))
            self.ax[0].set_xlabel('年')
            JP = self.ax[0].plot(x, y1, marker='o', linestyle='--', label='JP', color='springgreen')
            CN = self.ax[0].plot(x, y2, marker='o', linestyle='--', label='CN', color='r')
            US = self.ax[0].plot(x, y3, marker='o', linestyle='--', label='US', color='b')

            
            # self.ax[0].bar_label(JP, labels=y1)
            # self.ax[0].bar_label(CN, labels=y2, padding=10)
            # self.ax[0].bar_label(US, labels=y3, padding=10)

            if self.ct == self.data_count:
                self.ax[0].legend(loc='upper left',fontsize=20)
                # print("日本語日本語日本語", self.ax[0].legend_ is not None) # デバッグ出力
            
            # 1年ずつ推移
            self.ct += 1
            
            self.fig.canvas.draw_idle()
            return True
        # self.canvas.draw()

    def update_legend(self):
        if self.ax[0].legend_ is not None:
            self.ax[0].draw_artist(self.ax[0].legend_)
        else:
            print("Legend not found") # デバッグ出力
        self.fig.canvas.draw_idle()

    # def update_01(self, *args):
    #     if self.i > 20:
    #         pass
    #     else:
    #         ax[0].barh(self.line, self.cards, color='r')
    #         ax[0].barh(self.line, self.cards_02, color='b', left=self.cards)
    #         ax[1].plot(self.line, self.cards, linestyle='--', marker='o',color='r')
    #         ax[1].plot(self.line, self.cards_02, linestyle='--', marker='o', color='b')
    #         self.i += 1
    #         self.line.append(self.i)
    #         self.cards.append(random.randint(12, 16))
    #         self.cards_02.append(random.randint(12, 16))
            
    #     canvas.draw_idle()


class MyApp(App):
    def build(self):
        Builder.load_file('plot.kv')
         # ウィンドウサイズを設定
        Config.set('graphics', 'width', '1400')
        Config.set('graphics', 'height', '1200')
        Config.write()
        return MyRootWidget()

MyApp().run()