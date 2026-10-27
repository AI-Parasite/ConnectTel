def create_ticket_id(number: int) -> str:
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number <=0 or number > 999999:
        raise ValueError("Input must be a positive integer between 1 and 999999.")    
    return f"CT-{str(number).zfill(6)}"