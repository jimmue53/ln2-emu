def chillparse(instring):
    if (instring == 'version'):
        return ('out' , 'version', 0 , 'V 5.11')
    if (instring == 'status'):
        return('out' , 'status' , 0 , 5)
    split1 = instring.partition('_')
    return split1
    
if __name__ == "__main__":
    print( chillparse('version') )
    print( chillparse('status') )
    print( chillparse('out_sp_05 1') )
    print( chillparse('in_pv_00') )