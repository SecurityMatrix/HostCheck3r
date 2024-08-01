import requests
import os 
import colorama
from colorama import Fore, Style
colorama.init()
print(rf"""
{Fore.RED} __                      _ _                        _        _      
{Fore.RED}/ _\ ___  ___ _   _ _ __(_) |_ _   _    /\/\   __ _| |_ _ __(_)_  __
{Fore.RED}\ \ / _ \/ __| | | | '__| | __| | | |  /    \ / _` | __| '__| \ \/ /
{Fore.RED}_\ \  __/ (__| |_| | |  | | |_| |_| | / /\/\ \ (_| | |_| |  | |>  < 
{Fore.RED}\__/\___|\___|\__,_|_|  |_|\__|\__, | \/    \/\__,_|\__|_|  |_/_/\_\.
{Fore.RED}                               |___/                                
{Fore.BLUE}Facebook Page ==> https://www.facebook.com/profile.php?id=61562060042117
{Fore.BLUE}Facebook Group ==> https://www.facebook.com/groups/1165397914702265
{Fore.BLUE}Youtube Channel ==> https://www.youtube.com/@Security_Matrix
{Fore.RESET}
""")
def is_website_up(url):
    try:
        response = requests.head(url, timeout=3)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

def check_websites_from_file(file_path):
    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f.readlines()]
    
    for url in urls:
        if url.startswith('http://'):
            full_url = url
        elif url.startswith('https://'):
            full_url = url
        else:
            full_url = f'http://{url}'
            if not is_website_up(full_url):
                full_url = f'https://{url}'
        print(f"{full_url}: {is_website_up(full_url)}")

file_path = input(f"{Fore.GREEN} Enter the path to the text file: ")
check_websites_from_file(file_path)
