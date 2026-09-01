import re
def scrape_directory_phones(directory_text):
    pattern1=re.compile(r'(\d{3})-(\d{3})-(\d{3})')
    pattern2=re.compile(r'(\(d{3})\)\s(\d{3})-(\d{3})')
    pattern3=re.compile(r'(\d{3})(\d{3})(\d{3})')
    records=[]
    for match in pattern1.finditer(directory_text):
        area_code=match.group(1)
        prefix=match.group(2)
        line_number=match.group(3)
    records.append({"ärea_code":area_code,
                    "Prefix":prefix,
                    "Line_number":line_number,
                    "formatted":f"({area_code}) {prefix}-{line_number}"
                    })
    for match in pattern2.finditer(directory_text):
            area_code=match.group(1)
            prefix=match.group(2)
            line_number=match.group(3)
    records.append({"ärea_code":area_code,
                    "Prefix":prefix,
                    "Line_number":line_number,
                    "formatted":f"({area_code}) {prefix}-{line_number}"
                        })
    for match in pattern3.finditer(directory_text):
            area_code=match.group(1)
            prefix=match.group(2)
            line_number=match.group(3)
    records.append({"ärea_code":area_code,
                        "Prefix":prefix,
                        "Line_number":line_number,
                        "formatted":f"({area_code}) {prefix}-{line_number}"
                        })
    return records
directory_text = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234." 
result = scrape_directory_phones(directory_text) 
print(result)