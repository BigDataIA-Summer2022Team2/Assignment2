import streamlit_authenticator as stauth
import yaml

name_list = ['meihu','cheng','admin']
username_list = ['meihu','lemon','admin']
passwords = ['meihu','cheng','admin']

hashed_passwords = stauth.Hasher(passwords).generate()

