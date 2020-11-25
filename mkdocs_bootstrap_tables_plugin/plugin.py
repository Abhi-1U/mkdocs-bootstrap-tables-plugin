import os
import sys
import re
from timeit import default_timer as timer
from datetime import datetime, timedelta

from mkdocs import utils as mkdocs_utils
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin, log

class BootstrapTablesPlugin(BasePlugin):
    config_scheme = (
        ('bootstrap-theme', config_options.Type(str, default='')),
    )

    def __init__(self):
        self.enabled = True
        self.total_time = 0
        self.theme=""
    
    def on_config(self, config, **kwargs):
        for config in ['bootstrap-theme']:
            # Check for non-existing config values.
            print("config option:",config)
            if not self.config[config]:
                sys.exit("Config '{}' is missing for {} plugin.".format(config, "BtTable"))
        self.theme=self.config['bootstrap-theme']
    
    def on_post_page(self, output_content, page, config):
        if(self.config):
            output_content = re.sub(r"<table>", "<table class=\" table "+self.theme+"\""+">", output_content)
            output_content = re.sub(r"<th>", "<th scope=\"col\">", output_content)
            return output_content
        else:
            output_content = re.sub(r"<table>", "<table class=\" table "+self.theme+"\""+">", output_content)
            output_content = re.sub(r"<th>", "<th scope=\"col\">", output_content)
            return output_content
