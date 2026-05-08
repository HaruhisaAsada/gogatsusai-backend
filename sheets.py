import os
import logging

import gspread
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()


def append_sale_row(item_name: str, quantity: int, sold_at: str) -> None:
    sheet_id = os.getenv("GOOGLE_SHEETS_ID")
    sheet_name = os.getenv("GOOGLE_SHEET_NAME", "sales_1")
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    if not sheet_id:
        logger.warning("GOOGLE_SHEETS_ID is not set. Skip appending to Sheets.")
        return

    if not credentials_path:
        logger.warning("GOOGLE_APPLICATION_CREDENTIALS is not set. Skip appending to Sheets.")
        return

    gc = gspread.service_account(filename=credentials_path)
    spreadsheet = gc.open_by_key(sheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)
    worksheet.append_row(
        [item_name, quantity, sold_at],
        value_input_option="USER_ENTERED",
    )
