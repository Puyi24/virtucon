from tkinter import *
from PIL import Image, ImageTk
import analysis_tools as at
import os
from pathlib import Path


class WorkerSelect:
    def __init__(self, master):
        self.workers = at.extract_api()
        self.user_input = StringVar()
        self.worker_entry = Entry(textvariable=self.user_input).pack()
        self.worker_button = Button(text='Enter Worker ID',
                                    command=self.get_worker,
                                    bg='#4285F4', fg='white',
                                    height=2, width=15).pack()
        self.output = Label(bg='#BCC6CC')
        self.worker_img = ImageTk.PhotoImage(Image.new(mode='RGB', size=(0, 0)))
        self.worker_img_label = Label(borderwidth=0, width=288, height=162)

    def get_worker(self):
        self.worker_img_label.pack_forget()
        try:
            worker_id = int(self.user_input.get())
        except ValueError:
            self.output['text'] = "Please use numbers only."
            self.output.pack()
        else:
            worker = at.worker_by_id(self.workers, worker_id)
            if worker:
                self.output.pack_forget()
                self.output['text'] = at.worker_str(worker)
                self.worker_img = self.resize_worker_img(worker)
                self.worker_img_label['image'] = self.worker_img
                self.worker_img_label.pack()
                self.output.pack()
            else:
                self.output['text'] = "Worker ID does not exist."
                self.output.pack()

    def resize_worker_img(self, worker):
        original_img = Image.open(at.get_img_path(worker))
        resized_img = original_img.resize((288, 162))
        return ImageTk.PhotoImage(resized_img)


class MainWindow:

    def __init__(self, master):
        self.tab_icon = Image.open('assets/tab_icon.png')
        master.configure(bg='#BCC6CC')
        window_icon = ImageTk.PhotoImage(self.tab_icon)
        master.wm_iconphoto(False, window_icon)
        master.title('Virtucon Industries')
        master.geometry('500x500+300+100')
        #root.maxsize(500, 300)
        self.main_logo = ImageTk.PhotoImage(Image.open('assets/logo.jpg'))
        self.logo_label = Label(master, image=self.main_logo, borderwidth=0).pack()



def main():
    root = Tk()
    mw = MainWindow(root)
    ws = WorkerSelect(root)
    root.mainloop()


if __name__ == "__main__":
    main()
