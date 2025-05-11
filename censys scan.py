import tkinter as tk
from tkinter import messagebox
import webbrowser
from bs4 import BeautifulSoup
import requests

# Function to open a URL in the default web browser
def open_url(url):
    webbrowser.open(url)

# Function to check if a URL is online by pinging the /settings endpoint
def check_url(url, label_ip):
    try:
        response = requests.get(url + "/settings")
        if response.status_code == 200:
            label_ip.config(fg="green")
        else:
            label_ip.config(fg="red")
    except requests.exceptions.RequestException as e:
        label_ip.config(fg="red")

# Load the HTML content from the file
with open('scan11052025.txt', 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all search results
results = soup.find_all('div', class_='SearchResult result')

# Initialize a list to store IPs with the specified ports
ip_list = []

# Iterate through each result
for result in results:
    # Extract the IP address
    ip_address = result.find('a', class_='SearchResult__title-text').text.strip()
    
    # Remove the bracket bit for the domain name if present
    if '(' in ip_address:
        ip_address = ip_address.split(' ')[0]
    
    # Find all service ports for the current result
    services = result.find_all('div', class_='service SearchResult__metadata-value')
    
    # Check if any of the services have port 11470 or 12470
    for service in services:
        if '11470' in service.text:
            ip_list.append(f"{ip_address}:11470 (http)")
            break
        elif '12470' in service.text:
            ip_list.append(f"{ip_address}:12470 (https)")
            break

# Create the main window
root = tk.Tk()
root.title("IP Address Links")

# Create a label to display instructions
label = tk.Label(root, text="Select an option for each IP address:")
label.pack(pady=10)

# Create buttons for each IP address with the specified ports and protocols
for ip in ip_list:
    ip_address, port_protocol = ip.split(" ")
    url = f"http://{ip_address}" if "http" in port_protocol else f"https://{ip_address}"
    
    frame = tk.Frame(root)
    frame.pack(pady=5)
    
    label_ip = tk.Label(frame, text=ip)
    label_ip.pack(side=tk.LEFT, padx=5)
    
    button_open = tk.Button(frame, text="Open URL", command=lambda url=url: open_url(url))
    button_open.pack(side=tk.LEFT, padx=5)
    
    button_check = tk.Button(frame, text="Check URL", command=lambda url=url, label_ip=label_ip: check_url(url, label_ip))
    button_check.pack(side=tk.LEFT, padx=5)

# Run the Tkinter event loop
root.mainloop()
