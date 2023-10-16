from tkinter import Tk, ttk
import tkinter as tk
import sys
import json

class My_App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Генератор конфига для YaMusicRPC by ShiftyX1')
        self.geometry("1200x400")
        self.resizable(False, False)
        self.setUI()


    def setUI(self):
        
        opts = { 'ipadx': 5, 'ipady': 5, 'sticky': 'nswe'  }
        exit_button = ttk.Button(self, text='Выход', command=self.app_exit)
        exit_button.grid(row=10, column=0, **opts)

        self.bar2 = ttk.LabelFrame(self, text='Настройки')
        self.bar2.grid(row=1, column=0, **opts)

        self.entry_YaMusicAuth_label = ttk.Label(self.bar2, text='Токен Яндекс Музыки ')
        self.entry_YaMusicAuth_label.grid(row=1, column=0, **opts)

        self.entry_YaMusicAuth = ttk.Entry(self.bar2)
        self.entry_YaMusicAuth.grid(row=1, column=1, **opts)

        self.entry_update_delay_label = ttk.Label(self.bar2, text='Задержка обновления RPC: ')
        self.entry_update_delay_label.grid(row=2, column=2, **opts)

        self.entry_update_delay = ttk.Entry(self.bar2)
        self.entry_update_delay.grid(row=1, column=4, **opts)

        self.entry_start_delay_label = ttk.Label(self.bar2, text='Задержка старта работы RPC: ')
        self.entry_start_delay_label.grid(row=1, column=5, **opts)

        self.entry_start_delay = ttk.Entry(self.bar2)
        self.entry_start_delay.grid(row=1, column=6, **opts)

        self.button_generate = ttk.Button(self.bar2, text='Сгенерировать конфиг', command=self.generate_cfg)
        self.button_generate.grid(row=8, column=0, **opts)

        self.label_zatychka = ttk.Label(self.bar2, text='ГОТОВО :) Можете запускать RPC', foreground='#f5f5f5')
        self.label_zatychka.grid(row=8, column=1, **opts)

    def app_exit(self):
        self.destroy()
        sys.exit()

    def generate_cfg(self):
        config = dict(token=self.entry_YaMusicAuth.get(), update_delay=int(self.entry_update_delay.get()), start_delay=int(self.entry_start_delay.get()), rpc_connect=1163158250309566584)
        
        with open('config.txt', 'w') as outfile:
            json.dump(config, outfile)

        with open('config.json', 'w') as outfile:
            json.dump(config, outfile)
        
        opts = { 'ipadx': 5, 'ipady': 5, 'sticky': 'nswe'  }
        self.label_done = ttk.Label(self.bar2, text='ГОТОВО :) Можете запускать RPC', foreground='#008000')
        self.label_done.grid(row=8, column=1, **opts)


root = My_App()
root.mainloop()