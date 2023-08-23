# lib/deli_counter.py

def line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."
    
    formatted_line = ", ".join([f"{index+1}. {name}" for index, name in enumerate(katz_deli)])
    return f"The line is currently: {formatted_line}"

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    return f"Welcome, {name}. You are number {position} in line."

def now_serving(katz_deli):
    if not katz_deli:
        return "There is nobody waiting to be served!"
    
    serving = katz_deli.pop(0)
    return f"Currently serving {serving}."
