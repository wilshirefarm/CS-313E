def moveTower(height, fromPole,toPole,withPole):

    if height == 1:
        moveDisk(fromPole,toPole)
    else:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moeTower(height-1,withPole,toPole,fromPole)
