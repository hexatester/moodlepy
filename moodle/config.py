from dacite import Config

DACITE_CONFIG = Config(type_hooks={
    str: str,
    int: int,
})
