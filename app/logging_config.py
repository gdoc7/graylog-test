# # logging_config.py
# import logging
#
# from pygelf import GelfUdpHandler
#
#
# def setup_gelf_logging():
#     logging.basicConfig(level=logging.INFO)
#     logger = logging.getLogger()
#     logger.addHandler(
#         GelfUdpHandler(host="127.0.0.1", port=12201, include_extra_fields=True)
#     )
#     return logger
#
#
# gelf_logger = setup_gelf_logging()
