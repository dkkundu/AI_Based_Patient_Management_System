"""Core > views > __init__.py"""
from .index import IndexView
from .registration import SignupView, LoginView
from .user import UserListView, UserDetailView, UserUpdateView, UserCreateView
from .home import HomePageView
from .change_password import dr_change_password

# update the following list to allow classes to be available for import
# this is very useful especially when using from .file import *
__all__ = [
    IndexView, SignupView, LoginView, UserListView, UserDetailView,
    UserUpdateView, UserCreateView,
    HomePageView, dr_change_password
]