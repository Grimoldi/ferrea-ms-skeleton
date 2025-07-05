from models.probes import Entity, HealthProbe, HealthStatus


def check_health() -> HealthProbe:
    """From all the registered datasources, try to fetch the data.

    Args:
        datasources (list[ApiService]): the list of all datasources configured.

    Returns:
        HealthProbe: the health probe instance.
    """
    ...


def check_readiness() -> HealthProbe:
    """Just return if the web server is running.

    Returns:
        HealthProbe: the health probe instance.
    """
    ...
