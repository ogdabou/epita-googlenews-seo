#!/usr/bin/env python
import os
import sys
import nltk


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seo_site.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    nltk.data.path.append("nltk_data/")
