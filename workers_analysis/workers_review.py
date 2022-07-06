"""
This program opens a GUI application which gets a worker ID from the user,
and prints the worker's photo and essential details
"""


from tkinter import *
from PIL import Image, ImageTk
import analysis_tools as at


class MainWindow:
    """"
    This class sets the window display
    """
    def __init__(self, master):
        self.tab_icon = Image.open('assets/tab_icon.png')
        master.configure(bg='#BCC6CC')
        window_icon = ImageTk.PhotoImage(self.tab_icon)
        master.wm_iconphoto(False, window_icon)
        master.title('Virtucon Industries')
        master.geometry('800x750+560+100')
        master.minsize(800, 750)
        master.maxsize(800, 750)
        self.main_logo = ImageTk.PhotoImage(Image.open('assets/logo.jpg'))
        self.logo_label = Label(image=self.main_logo, borderwidth=0).pack(pady=20)


class WorkerSelect:
    """
    This class sets the input and output Interface
    """
    def __init__(self, master):
        self.workers = at.extract_api()
        self.user_input = StringVar()
        self.worker_entry = Entry(textvariable=self.user_input).pack()
        self.worker_button = Button(text='Enter Worker ID',
                                    command=self.get_worker,
                                    bg='#4285F4', fg='white',
                                    height=2, width=15).pack(pady=10)
        self.output = Label(fg='#00008B', bg='#BCC6CC', wraplength=400,
                            font=('Myriad', 16, 'bold'), justify='left')
        # setting an empty image object for later usage:
        self.worker_img = ImageTk.PhotoImage(Image.new(mode='RGB', size=(0, 0)))
        self.worker_img_label = Label(borderwidth=0, width=384, height=216)


    def get_worker(self):
        """
        This function gets the user input via the entry and button objects set in the class initializing method,
        and prints an output accordingly via the label and image objects.
        if the user's input is a valid worker ID, his photo and details will be presented.
        if his input is not consisted by numbers, or a number which doesn't relate to any worker ID,
        a suitable message will be presented.
        :return: none
        """
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
                self.worker_img_label.pack(pady=10)
                self.output.pack(pady=20)
            else:
                self.output['text'] = "Worker ID does not exist."
                self.output.pack()

    def resize_worker_img(self, worker):
        """
        resizing a worker's image to the size used by the application
        :param worker: dictionary of the worker whose image is needed
        :return: worker's resized image
        :rtype: ImageTk PhotoImage object
        """
        original_img = Image.open(at.get_img_path(worker))
        resized_img = original_img.resize((384, 216))
        return ImageTk.PhotoImage(resized_img)


def main():
    root = Tk()
    mw = MainWindow(root)
    ws = WorkerSelect(root)
    root.mainloop()


if __name__ == "__main__":
    main()
