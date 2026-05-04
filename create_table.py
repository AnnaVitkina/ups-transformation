"""
Excel workbook generation — compatibility shim.

The implementation lives in ``transformation_to_excel``. Pipeline code may import
this module as ``create_table``; prefer importing ``transformation_to_excel`` directly.
"""

from transformation_to_excel import (
    create_metadata_sheet,
    load_extracted_data,
    main,
    save_to_excel,
)

__all__ = [
    'create_metadata_sheet',
    'load_extracted_data',
    'main',
    'save_to_excel',
]
