from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuration settings for the application.

    This class uses Pydantic's BaseSettings to manage application settings. The settings
    can be configured through environment variables, and default values are provided.

    Attributes:
        app_name (str): The name of the application. Default is "Blockchain API".
    """

    app_name: str = "Blackchain API"


settings = Settings()
