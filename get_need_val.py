def get_value(val_in):
    val_out = [v for v in val_in if v.isnumeric()]
    val_out = ''.join(val_out)
    return val_out

def get_str(val_in):
    val_out = [v for v in val_in if not(v.isnumeric())]
    val_out = ''.join(val_out)
    return val_out