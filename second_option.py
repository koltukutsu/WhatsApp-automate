import pywhatkit as pw
# yeah, it is really that simple

ITEMS = {
    {
        "phone": "",
        "message": ""
    }
}

HOUR = 16
MINUTE = 10
counter = 0

for item in ITEMS:
    phone = item["phone"]
    message = item["message"]
    
    counter += 1
    if counter == 19:
        MINUTE += 1

    second = counter * 2
    pw.sendwhatmsg(phone, message, HOUR, MINUTE, second)
