def cross_point(x1, y1, vx1, vy1, x2, y2, vx2, vy2, ):
    '''
    define line A and line B, write a function which can return the point two lines cross.
    dot_1 = (x1, y1)
    dot_2 = (x2, y2)
    vec_1 = (vx1, vy1)
    vec_2 = (vx2, vy2)
    line1 = [(x1, y1), (x1 + vx1, y1 + vy1)], line2 = [(x2, y2), (x2 + vx2, y2 + vy2)]
    '''
    if vx1 == 0:# 如果斜率為0
        k1 = None
        b1 = 0
    else:
        k1=vy1*1.0/vx1
        b1=(y1 + vy1)*1.0-(x1 + vx1)*k1*1.0
    if vx2 == 0:
        k2 = None
        b2 = 0
    else:
        k2=vy2*1.0/vx2
        b2=(y2 + vy2)*1.0-(x2 + vx2)*k2*1.0
    
    if k1 == k2:
        print("parallel")
        return None
    elif k1 == None:# 如果Line1斜率不存在，則取Line1上的點帶入Line2的公式
        x= x1 + vx1
        k1 = k2
        b1 = b2
    elif k2 == None:
        x=x2 + vx2
    else:
        x=(b2-b1)*1.0/(k1-k2)
    y=k1*x*1.0+b1*1.0
    return (x,y)

def cross_point_dot(x1, y1, vx1, vy1, x2, y2, x3, y3, ):
    '''
    this function is same as above. But in this case, one of lines has starting point and ending point.
    If the point two line cross out of the line, function should return None.
    '''
    p = cross_point(x1, y1, vx1, vy1, x2, y2, x3 - x2, y3-y1)
    if x2 <= p[0] <= x3 or x3 <= p[0] <= x2:
        return p
    else:
        return None

# Test Case
assert cross_point(2 ,1 ,0 ,1 ,-1 ,1 ,1 , -1) == (2, -2)
assert cross_point_dot(2 ,1 ,0 ,1 ,-1 ,1 ,3 , -3) == (2, -2)
assert cross_point_dot(2 ,1 ,0 ,1 ,-1 ,1 ,1 , -1) == None
print("Done!")