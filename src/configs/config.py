from pathlib import Path

from dynaconf.typed import Annotated, DictValue, Dynaconf, Options
from dynaconf.typed.validators import Validator

config_dir = Path(__file__).parent



class FerreaApp(DictValue):
    """Settings for the app itself."""

    name: str
    debug: bool = False
    oas_path: str | None = None


class FerreaSettings(Dynaconf):
    """Overall settings for the webserver."""

    ferrea_app: FerreaApp = FerreaApp()  # type: ignore

    dynaconf_options = Options(
        envvar_prefix="FERREA",
        settings_files=["settings.toml", ".secrets.toml"],
        root_path=config_dir,
    )


settings = FerreaSettings(_debug_mode=False)
