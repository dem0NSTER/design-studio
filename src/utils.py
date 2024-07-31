from datetime import datetime


def write_log(e: str, __name_: str, func_name: str) -> None:
    """
    type e: str (exeption)
    type __name_: str (__name__)
    type func_name: str
    rtype: None
    """
    with open("log.txt", "a") as file:
        file.write(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M')}: (func: {__name_}: {func_name}) {e};\n\n")
