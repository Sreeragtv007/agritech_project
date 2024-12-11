



def ocr_converter(text):
    new_list = text.strip().split("\n")
    data = [item for item in new_list if item.strip()]
    info_dict = {}


    for item in data:
        if "latitude:" in item:
            info_dict['latitude'] = item.split(":")[1].strip(",")
        elif "Longitude:" in item:
            info_dict['longitude'] = item.split(":")[1].strip()
        elif "Accuracy:" in item:
            info_dict['accuracy'] = item.split(":")[1].strip()
        elif "Azimuth:" in item:
            info_dict['azimuth'] = item.split(":")[1].strip()
        elif "Pitch:" in item:
            info_dict['pitch'] = item.split(":")[1].strip()
        elif "Time:" in item:
            info_dict['time'] = item.split(":")[1].strip()
        elif "Farmer ID:" in item:
            info_dict['farmer_id'] = item.split(":")[2].strip()
        elif "Farmer Name:" in item:
            info_dict['farmer_name'] = item.split(":")[1].strip()
        elif "Crop Name:" in item:
            info_dict['crop_name'] = item.split(":")[1].strip()
            
    return info_dict