import re
from datetime import datetime


def date_formatter(text):
    regex1 = '(0?[1-9]|[12][0-9]|3[01])[/](0?[1-9]|1[012])[/](((19|20)\d\d)|(\d\d))'  # DD/MM/YYYY,D/M/YY
    regex2 = '(0?[1-9]|[12][0-9]|3[01])[-](0?[1-9]|1[012])[-](((19|20)\d\d)|(\d\d))'  # DD-MM-YYYY,D/M/YY
    regex3 = '(0?[1-9]|[12][0-9]|3[01])[.](0?[1-9]|1[012])[.](((19|20)\d\d)|(\d\d))'  # DD.MM.YYYY,D.M.YY
    # regex4 = '(0?[1-9]|[12][0-9]|3[01])\\(0?[1-9]|1[012])\\(((19|20)\d\d)|(\d\d))'
    regex5 = '(0?[1-9]|1[012])[/](0?[1-9]|[12][0-9]|3[01])[/](((19|20)\d\d)|(\d\d))'  # MM/DD/YYYY,M/D/YY
    regex6 = '(0?[1-9]|1[012])[-](0?[1-9]|[12][0-9]|3[01])[-](((19|20)\d\d)|(\d\d))'  # MM-DD-YYYY,M-D-YY
    regex7 = '(0?[1-9]|1[012])[.](0?[1-9]|[12][0-9]|3[01])[.](((19|20)\d\d)|(\d\d))'  # MM.DD.YYYY,M.D.YY
    # regex8 = '(0?[1-9]|1[012])\\(0?[1-9]|[12][0-9]|3[01])\\(((19|20)\d\d)|(\d\d))'
    regex9 = '((Jan)|(Feb)|(Mar)|(Apr)|(May)|(Jun)|(Jul)|(Aug)|(Sep)|(Oct)|(Nov)|(Dec))\s(0?[1-9]|[12][0-9]|3[01])' \
             ',\s((19|20)\d\d)'  # MMM DD, YYYY
    regex10 = '((January)|(February)|(March)|(April)|(May)|(June)|(July)|(August)|(September)|(October)|(November)|' \
              '(December))\s(0?[1-9]|[12][0-9]|3[01])th,\s((19|20)\d\d)'  # Month DDth, YYYY
    regex11 = '(0?[1-9]|[12][0-9]|3[01])[-]((JAN)|(FEB)|(MAR)|(APR)|(MAY)|(JUN)|(JUL)|(AUG)|(SEP)|(OCT)|(NOV)|(DEC)|' \
              '(Jan)|(Feb)|(Mar)|(Apr)|(May)|(Jun)|(Jul)|(Aug)|(Sep)|(Oct)|(Nov)|(Dec))[-]((19|20)\d\d)'  # DD-MMM-YYYY
    regex12 = '((Jan)|(Feb)|(Mar)|(Apr)|(May)|(Jun)|(Jul)|(Aug)|(Sep)|(Oct)|(Nov)|(Dec))(0?[1-9]|[12][0-9]|3[01])\'\d{2}'  # MMMDD'YY
    regex13 = '(0?[1-9]|[12][0-9]|3[01])((Jan)|(Feb)|(Mar)|(Apr)|(May)|(Jun)|(Jul)|(Aug)|(Sep)|(Oct)|(Nov)|(Dec))\'\d{2}'  # DDMMM'YY

    # regex = [regex1,regex2,regex3,regex4,regex5,regex6,regex7,regex8,regex9,regex10,regex11,regex12,regex13]
    date = re.search(regex1, text)
    if date != None:
        formats = ['%d/%m/%y', '%d/%m/%Y']  # validation string for regex1
        formatted_date = date_time(date.group(), formats)  # method to evaluate possible date formats.
        if formatted_date is not None:
            return formatted_date

    date = re.search(regex2, text)
    if date != None:
        formats = ['%d-%m-%y', '%d-%m-%Y']
        formatted_date = date_time(date.group(), formats)
        if formatted_date is not None:
            return formatted_date

    date = re.search(regex3, text)
    if date != None:
        formats = ['%d.%m.%y', '%d.%m.%Y']
        formatted_date = date_time(date.group(), formats)
        if formatted_date is not None:
            return formatted_date

    # date = re.search(regex4,text)
    # if date != None:
    #     formats = ['%d\%m\%y','%d\%m\%Y']
    #     formatted_date = date_time(date,formats)
    #     if formatted_date != None:
    #         return formatted_date

    date = re.search(regex5, text)
    if date != None:
        formats = ['%m/%d/%y', '%m/%d/%Y']
        formatted_date = date_time(date.group(), formats)
        if formatted_date is not None:
            return formatted_date

    date = re.search(regex6, text)
    if date != None:
        formats = ['%m-%d-%y', '%m-%d-%Y']
        formatted_date = date_time(date.group(), formats)
        if formatted_date is not None:
            return formatted_date

    date = re.search(regex7, text)
    if date != None:
        formats = ['%m.%d.%y', '%m.%d.%Y']
        formatted_date = date_time(date.group(), formats)
        if formatted_date is not None:
            return formatted_date

    # date = re.search(regex8,text)
    # if date != None:
    #     formats = ['%m\%d\%y','%m\%d\%Y']
    #     formatted_date = date_time(date,formats)
    #     if formatted_date != None:
    #         return formatted_date

    date = re.search(regex9, text)
    if date != None:
        formats = ['%b %d, %Y']
        formatted_date = date_time(date.group(), formats)
        if formatted_date is not None:
            return formatted_date

    date = re.search(regex10, text)
    if date != None:
        formats = ['%B %dth, %Y']
        formatted_date = date_time(date.group(), formats)
        if formatted_date is not None:
            return formatted_date

    date = re.search(regex11, text)
    if date != None:
        formats = ['%d-%b-%Y']
        x = list(date.group().lower())
        ind = x.index('-')
        x[ind + 1] = x[ind + 1].upper()
        date = ''.join(x)
        formatted_date = date_time(date, formats)
        if formatted_date is not None:
            return formatted_date

    date = re.search(regex12, text)
    if date != None:
        formats = ['%b%d\'%y']
        formatted_date = date_time(date.group(), formats)
        if formatted_date is not None:
            return formatted_date

    date = re.search(regex13, text)
    if date != None:
        formats = ['%d%b\'%y']
        formatted_date = date_time(date.group(), formats)
        if formatted_date is not None:
            return formatted_date

    return None


def date_time(date, formats):                   #helper methods to validate date formats.
    for format in formats:
        formatted_date = check_date(date, format)
        if formatted_date is not None:
            return formatted_date.date().strftime('%Y-%m-%d')
    return None


def check_date(date, format):
    try:
        return datetime.strptime(date, format)
    except:
        return None
