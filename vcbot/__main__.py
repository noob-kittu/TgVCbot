from vcbot import app
from importlib import import_module
from vcbot.plugins import ALL_MODULES


for module_name in ALL_MODULES:
    imported_module = import_module("vcbot.plugins." + module_name)

app.start()


app.run_until_disconnected()