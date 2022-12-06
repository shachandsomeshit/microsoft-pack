import tkinter as tk
from tkinter import filedialog

input_ = input("text:")
orginal_site_key = input("orginal key:")
site_key = input("key:")

Token = input_.replace(orginal_site_key, site_key)
print(Token)