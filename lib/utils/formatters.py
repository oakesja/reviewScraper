def TakeFirst(x):
    try:
        return x[0].strip()
    except Exception:
        #TODO add and test logging here
        return None


