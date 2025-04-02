# builtin

import os
import html
from pathlib import PurePath
import random
import re
from typing import Optional
import urllib.parse
# pip
from mkdocs.config.base import Config
from mkdocs.config.config_options import Type, ListOfItems
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin, get_plugin_logger
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

LOGGER = get_plugin_logger(__name__)

class VariableRandomizerConfig(Config):
    prefix = Type(str, default="rand_")

class VariableRandomizerPlugin(BasePlugin[VariableRandomizerConfig]):
    def __init__(self):
        pass        
    
    def on_nav(self, nav, config: MkDocsConfig, files: Files):
        pass

    def on_page_markdown(self, markdown, page: Page, config: MkDocsConfig, files: Files) -> str:
        pass

    def on_page_content(self, html, page: Page, config: MkDocsConfig, files: Files) -> str:
        return html.replace(self.config.prefix, "PREFIX")

    def on_post_page(self, output: str, page: Page, config: MkDocsConfig) -> str:
        return output

