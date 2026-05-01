import requests

def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as time_err:
        print(f"Timeout error occurred: {time_err}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    data = get_data(url)
    if data:
        print(data)

if __name__ == "__main__":
    main()
```

```python
import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self)
        self.url_label["text"] = "Enter URL:"
        self.url_label.pack(side="top")

        self.url_entry = tk.Entry(self)
        self.url_entry.pack(side="top")

        self.get_button = tk.Button(self)
        self.get_button["text"] = "Get Data"
        self.get_button["command"] = self.get_data
        self.get_button.pack(side="top")

        self.data_label = tk.Label(self)
        self.data_label.pack(side="top")

        self.error_label = tk.Label(self, fg="red")
        self.error_label.pack(side="top")

    def get_data(self):
        url = self.url_entry.get()
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.data_label["text"] = str(data)
            self.error_label["text"] = ""
        except requests.exceptions.HTTPError as http_err:
            self.error_label["text"] = f"HTTP error occurred: {http_err}"
        except requests.exceptions.ConnectionError as conn_err:
            self.error_label["text"] = f"Connection error occurred: {conn_err}"
        except requests.exceptions.Timeout as time_err:
            self.error_label["text"] = f"Timeout error occurred: {time_err}"
        except requests.exceptions.RequestException as err:
            self.error_label["text"] = f"Something went wrong: {err}"
        except Exception as e:
            self.error_label["text"] = f"An error occurred: {e}"

root = tk.Tk()
app = Application(master=root)
app.mainloop()
```

```python
import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self)
        self.url_label["text"] = "Enter URL:"
        self.url_label.pack(side="top")

        self.url_entry = tk.Entry(self)
        self.url_entry.pack(side="top")

        self.get_button = tk.Button(self)
        self.get_button["text"] = "Get Data"
        self.get_button["command"] = self.get_data
        self.get_button.pack(side="top")

        self.data_label = tk.Label(self)
        self.data_label.pack(side="top")

        self.error_label = tk.Label(self, fg="red")
        self.error_label.pack(side="top")

        self.loading_label = tk.Label(self, fg="blue")
        self.loading_label.pack(side="top")

    def get_data(self):
        self.loading_label["text"] = "Loading..."
        url = self.url_entry.get()
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.data_label["text"] = str(data)
            self.error_label["text"] = ""
            self.loading_label["text"] = ""
        except requests.exceptions.HTTPError as http_err:
            self.error_label["text"] = f"HTTP error occurred: {http_err}"
            self.loading_label["text"] = ""
        except requests.exceptions.ConnectionError as conn_err:
            self.error_label["text"] = f"Connection error occurred: {conn_err}"
            self.loading_label["text"] = ""
        except requests.exceptions.Timeout as time_err:
            self.error_label["text"] = f"Timeout error occurred: {time_err}"
            self.loading_label["text"] = ""
        except requests.exceptions.RequestException as err:
            self.error_label["text"] = f"Something went wrong: {err}"
            self.loading_label["text"] = ""
        except Exception as e:
            self.error_label["text"] = f"An error occurred: {e}"
            self.loading_label["text"] = ""

root = tk.Tk()
app = Application(master=root)
app.mainloop()
