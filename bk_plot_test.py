import matplotlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import random

fig, ax = plt.subplots()
canvas = FigureCanvasKivyAgg(fig)


class MyApp(App):
    def build(self):
        box = BoxLayout()
        self.i = 1
        self.ch1 = random.randint(15, 20)
        self.ch2 = random.randint(12, 16)
        self.line = [self.i]
        self.cards = [self.ch1]
        self.cards_02 = [self.ch2]
        box.add_widget(canvas)
        # for ct in range(100):
        #     self.update()
        # plt.show()
        Clock.schedule_interval(self.update, 0.1)
        return box
         
    def update(self, *args):
        plt.ylim(0,50)
        if self.i >= 20:
            pass
        else:
            plt.plot(self.line, self.cards, linestyle='--', marker='o',color='r')
            plt.plot(self.line, self.cards_02, linestyle='--', marker='o', color='b')
            self.i += 1
            self.line.append(self.i)
            self.cards.append(random.randint(12, 16))
            self.cards_02.append(random.randint(12, 16))
        canvas.draw_idle()


MyApp().run()