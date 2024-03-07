import matplotlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import random

fig, ax = plt.subplots(2,1)


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
        Clock.schedule_interval(self.update_02, 0.1)

        return box
    

    # def get_graph_data(self):
    #     self.data_set_01 = [1,2,3,4,5]
    #     self.data_set_02 = [5,4,3,2,1]
    
    # argsはClock描画用の引数として渡される
    def update_02(self, *args):
        if self.i > 6:
            pass
        else:
            self.data_set_01 = [1,2,3,4,5,6]
            y = self.data_set_01[0:self.i]
            ax[0].bar(self.line, y, color='r')
            
        
            self.i += 1
            self.line.append(self.i)
            
                
        canvas.draw_idle()

         
    def update_01(self, *args):
        if self.i > 20:
            pass
        else:
            ax[0].barh(self.line, self.cards, color='r')
            ax[0].barh(self.line, self.cards_02, color='b', left=self.cards)
            ax[1].plot(self.line, self.cards, linestyle='--', marker='o',color='r')
            ax[1].plot(self.line, self.cards_02, linestyle='--', marker='o', color='b')
            self.i += 1
            self.line.append(self.i)
            self.cards.append(random.randint(12, 16))
            self.cards_02.append(random.randint(12, 16))
            
        canvas.draw_idle()

   
MyApp().run()