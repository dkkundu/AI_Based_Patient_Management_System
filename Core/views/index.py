"""Core > views > index.py"""
# PYTHON IMPORTS
import logging
# DJANGO IMPORTS
from django.views.generic import TemplateView
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


logger = logging.getLogger(__name__)


class IndexView(UserPassesTestMixin, LoginRequiredMixin, TemplateView):
    """Landing page view"""
    template_name = 'index.html'