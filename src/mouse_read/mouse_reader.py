#       Bit 7       Bit 6        Bit 5        Bit 4        Bit 3      Bit 2        Bit 1       Bit 0 
#Byte 1  Y overflow  | X overflow | Y sign bit | X sign bit | Always 1 | Middle Btn | Right Btn | Left Btn
#Byte 2  X movement
#Byte 3  Y movement


def to_signed(n):
    return n - ((0x80 & n) << 1)

mouse = file('/dev/input/mice')  
while True:  
    status, dx, dy = tuple(ord(c) for c in mouse.read(3))

    dx = to_signed(dx)
    dy = to_signed(dy)

    leftButton = ((status & 0x01) == 1)
    rightButton = ((status & 0x02) == 2)
    middleButton = ((status & 0x04) == 4)

    print "  Left button: %r" % leftButton
    print " Right button: %r" % rightButton
    print "Middle button: %r" % middleButton
    print "           dX: %d" % dx
    print "           dY: %d" % dy
    print "       Status: %#02x" % status
    print "--------------------------------"
#    print "%#02x %d %d" % (status, dx, dy)
