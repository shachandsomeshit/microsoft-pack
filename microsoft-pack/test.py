Key_ =  '   5435844                                                                                    5435844                                                                                 '
Key_ = ""
for i in Key:
    try:
        int(i)
        Key_ += i
    except (ValueError):
        continue
print(Key_)