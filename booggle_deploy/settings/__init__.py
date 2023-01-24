from decouple import config


try:
    print(f"printing **before** {config('SETTINGS_PATH')}")

    if config('SETTINGS_PATH') == "prod":
        print("prod.py settings activated!")
        from .prod import *
except:
    print("SETTINGS_PATH not equal to prod..")
    print("dev.py settings activated!")
    from .dev import *