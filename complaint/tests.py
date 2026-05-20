import win32com.client

try:

    outlook = win32com.client.gencache.EnsureDispatch(
        "Outlook.Application"
    )

    print("Outlook Connected")

except Exception as e:

    print(f"error",e)

import struct
print(struct.calcsize("P") * 8)