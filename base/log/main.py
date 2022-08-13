import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(lineno)s:%(message)s",
)

log = logging.getLogger(__name__)

log.info("message")
