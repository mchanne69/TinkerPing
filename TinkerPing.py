import tkinter as tk
from tkinter import ttk
import subprocess
import os, platform
import ipaddress

version ="0.1"

root = tk.Tk()
root.title("TKPing " + version)
root.geometry("567x435")
root.resizable(False, False)


# METHOD: Checks the OS of the platform and returns the name for in conditional checking elsewhere
def identify_os():
    operating_system = platform.system()
    operating_system_release = platform.release()
    print(f"Operating system {operating_system}")
    print(f"Platform Release {operating_system_release}")
    return operating_system


# METHOD: Requires parameter string of the IP address and then return True/False depending on the whether it's valid
def validate_ip_addr(ip_addr):
    try:
        ip = ipaddress.ip_address(ip_addr)
        print(f"{ip} is a valid {ip.version} address.")
        return True
    except ValueError:
        print(f"{ip_addr} is not valid!")
        return False


def call_ping():
    if validate_ip_addr(ipaddr_text.get()):
        if identify_os() == 'Darwin':
            ping_proc = subprocess.Popen(["ping", "-c", "4", ipaddr_text.get()], stdout=subprocess.PIPE)
            dsp_text.insert(tk.END, ping_proc.communicate()[0])
        else:
            print("Error with either IP or unsupported OS")


class App(tk.Tk):
    def __init__(self):
        super().__init__()

ipaddr_text = tk.StringVar()

ctl_frame = ttk.Frame(root)
ctl_frame.grid(row=0, column=0, pady="2", padx="4", sticky="ew")

ctl_frame.columnconfigure(0, weight=1)
ctl_frame.columnconfigure(1, weight=1)

ipaddr_label = ttk.Label(ctl_frame, text="IP Address: ", padding=(5, 0, 5, 0), anchor="w")
ipaddr_label.grid(row=0, column=0)

ipaddr_entry = ttk.Entry(ctl_frame, width=15, textvariable=ipaddr_text)
ipaddr_entry.grid(row=0, column=1)

ping_button = ttk.Button(ctl_frame, text="Start Ping", command=call_ping)
ping_button.grid(row=1, column=0)

quit_button = ttk.Button(ctl_frame, text="Quit", command=root.destroy)
quit_button.grid(row=1, column=1)

sep1 = ttk.Separator(root)
sep1.grid(row=1, column=0, columnspan=2, sticky="EW", pady="4", padx="5")

dsp_frame = ttk.Frame(root)
dsp_frame.grid(row=2, column=0, sticky="EW")
dsp_frame.columnconfigure(0, weight=1)

dsp_text = tk.Text(dsp_frame, bg="grey", height=28)
dsp_text.grid(row=0, column=0, sticky="EW")

root.mainloop()