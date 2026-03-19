"""
Royalty ETL — Dynamic Column Mapping
Processes $55M in quarterly royalties across 99 vendor contracts from 6 source systems.
Each source has a completely different column structure. This mapping lets one function
handle all of them without code changes.
"""
from openpyxl import load_workbook, Workbook

column_mappings = {
    'SQL':          [1, 7, 5, 9, 11, 12, 13, 14, 15, 16, 18, 25, 23, 26, 24, 27, 21],
    'AMAZON':       [1, 16, 17, 6, 5, 7, 8, 9, 10, 19, 18, 11, 12, 14, 13, 15, 2],
    'AW WHOLESALE': [27, 31, 1, 5, 7, 8, 12, 13, 28, 30, 29, 14, 21, 22, 23, 24, 20],
    'AW RETAIL':    [27, 31, 1, 5, 7, 8, 12, 13, 28, 30, 29, 14, 21, 22, 23, 24, 20],
    'A&F':          [2, 35, 17, 21, 19, 26, 27, 28, 29, 37, 31, 38, 39, 41, 40, 42, 24],
    'NTD':          [2, 6, 8, 21, 19, 26, 27, 28, 29, 37, 31, 38, 39, 41, 40, 42, 24]
}

OUTPUT_HEADERS = [
    "Date", "Territory", "Customer", "Style #", "Style Name",
    "Demo", "Article", "Units", "Unit Price", "Gross Sales",
    "Discounts", "Net Sales", "Royalty Rate", "Royalty Earned",
    "CMF Rate", "CMF Earned", "Vendor#"
]

def process_sheet(source_name, source_sheet, output_sheet, vendor_list):
    """Process any vendor source using its column mapping."""
    output_sheet.append(OUTPUT_HEADERS + ["Source"])
    mapping = column_mappings[source_name]
    
    for row in source_sheet.iter_rows(min_row=2):
        vendor_num = row[mapping[-1] - 1].value
        if vendor_num in vendor_list:
            data = []
            for idx in mapping:
                cell = row[idx - 1]
                if cell.value is None:
                    data.append("")
                elif cell.is_date:
                    data.append(cell.value.strftime("%Y-%m-%d"))
                else:
                    data.append(cell.value)
            data.append(source_name)
            output_sheet.append(data)
