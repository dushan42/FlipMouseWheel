import winreg

with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Enum\HID') as key:
    subKeyCount, _, _ = winreg.QueryInfoKey(key)
    for i in range(subKeyCount):
        subKeyName = winreg.EnumKey(key, i)
        with winreg.OpenKey(key, subKeyName) as subKey:
            subSubKeyCount, _, _ = winreg.QueryInfoKey(subKey)
            for j in range(subSubKeyCount):
                subSubKeyName = winreg.EnumKey(subKey, j)
                with winreg.OpenKey(subKey, f'{subSubKeyName}\Device Parameters', 0, winreg.KEY_READ | winreg.KEY_SET_VALUE) as dpKey:
                    _, valueCount, _ = winreg.QueryInfoKey(dpKey)
                    for k in range(valueCount):
                        valueName, valueData, valueType = winreg.EnumValue(dpKey, k)
                        if valueName == 'FlipFlopWheel' and valueData == 0:
                            print('Setting FlipFlopWheel on ', subKeyName, subSubKeyName)
                            try:
                                winreg.SetValueEx(dpKey, valueName, 0, valueType, 1)
                            except Exception as e:
                                print(e)
                                
