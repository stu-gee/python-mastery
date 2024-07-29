def parse_line(line:str):
    try:
        name, val = line.split('=')
    except ValueError:
        return None
    
    return(name, val)


