"""
Date: 2022.07.27 15:38:30
LastEditors: Rustle Karl
LastEditTime: 2022.07.27 15:40:41
"""
from climatecontrol import climate

climate.settings_files.extend(
    [
        "config.yaml",
        "config.toml",
        "config.yml",
    ]
)

print(climate.settings)
