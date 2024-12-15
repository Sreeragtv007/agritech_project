

def ocr_converter(text):
    new_list = text.split("\n")
    data = [item for item in new_list if item.strip()]

    print(data)

    dict = {}

    for item in data:
        
        try:

            if "lati" in item:
                print(item)
                dict['latitude'] = item.split(":")[1]
            elif "long" in item:
                dict['longitude'] = item.split(":")[1]
            elif "ele" in item:
                dict['elevation'] = item.split(":")[1]
            elif "accu" in item:
                dict['accuracy'] = item.split(":")[1]
            elif "time" in item:
                dict['time'] = item.split(":")[1]
            elif "id" in item:
                dict['farmerid'] = item.split(":")[-1]
            elif "farmer name" in item:
                dict['farmername'] = item.split(":")[1]
            elif "crop" in item:
                dict['cropname'] = item.split(":")[1]
        except Exception as e:
            print(e)
            return False
    return dict

    # print(dict)

    # ['latitude: 17.821182', 'longitude: 75.014548', 'elevation: 537.0544 m', 'accuracy: 1.4m', 'time: 11-04-2024 01:39 p', 'note: farmer id : 41730', 'farmer name : archana pr', 'crop name: banana g9 ti']
