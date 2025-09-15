is_power = False
speed = 0

def turn_on_power():
    global is_power
    is_power = True
    return is_power

def turn_off_power():
    global is_power, speed
    is_power = False
    speed = 0
    return is_power

def set_speed(new_speed):
    global speed, is_power
    store_speed = new_speed
    if is_power and new_speed > 0:
        store_speed = new_speed
    speed = store_speed
    return speed

def accelerate():
    global is_power,speed
    if not is_power:
        return
    if speed > 0 and speed <= 20:
        speed += 1
        return speed
    elif speed > 20 and speed <= 30:
        speed += 2
        return speed
    elif speed > 30 and speed <= 40:
        speed += 3
        return speed
    elif speed > 40:
        speed += 4
        return speed

def decelerate():
    global is_power,speed
    if not is_power:
        return
    if speed > 0 and speed <= 20:
        speed -= 1
        return speed
    elif speed > 20 and speed <= 30:
        speed -= 2
        return speed
    elif speed > 30 and speed <= 40:
        speed -= 3
        return speed
    elif speed > 40:
        speed -= 4
        return speed

