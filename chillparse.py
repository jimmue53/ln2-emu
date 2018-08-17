import time
t0 = time.clock()
actual_temp = 25.0
power_on = False
booster_on = False



def chillparse(instring):
    """Converts chiller command string to tuple (in_out, cmd_type, cmd_number, arg string)  """
    if (instring == 'version'):
        return ('in' , 'version', 0 , 'V 5.11')
    if (instring == 'status'):
        return ('in' , 'status' , 0 , 5)
    in_out = instring.partition('_')
    cmd_type = in_out[2].partition('_')
    if in_out[0] == 'in' :
        cmd_number = int(cmd_type[2])
        return (in_out[0], cmd_type[0], cmd_number, '')
    elif in_out[0] == 'out' :
        cmd_number = cmd_type[2].partition(' ')
        return (in_out[0], cmd_type[0], int(cmd_number[0]), cmd_number[2])
    else :
        print('chiller command string format error')
        return (in_out[0], in_out[2], 0, 0)

def init_booster() :
   




if __name__ == "__main__":  
    instr = ' '
    while instr != 'q' :
        instr = input("Enter test command string:")
        print(chillparse(instr))

