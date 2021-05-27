#robot bounded by circle after given instructions as L R G - g for go ahead
class robotBound:
    def isRobotBounded(self, instructions):
        
        #initial point or origin
        x = 0
        y = 0
        direction = 0
        
        #[0,1]-> NORTH :::: [1, 0]-> EAST :::: [0, -1]-> SOUTH :::: [-1, 0]-> WEST
        coordinates=[[0,1],[1,0],[0,-1],[-1,0]]
        
        for i in instructions:
            if i == "L":
                direction=(direction+3)%4 #at every 4 steps NEWS resets to 0. reset call for %4
            elif i == "R":
                direction=(direction+1)%4
            else:
                x += coordinates[direction][0]
                y += coordinates[direction][1]
        
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or direction != 0

instructions="GGGLGLGLGGL"
answer=robotBound().isRobotBounded(instructions)
print(answer)