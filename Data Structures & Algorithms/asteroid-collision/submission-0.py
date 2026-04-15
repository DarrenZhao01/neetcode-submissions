class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1]

                if diff < 0: # asteroids bigger than top of stack
                    stack.pop()
                elif diff > 0: # top of stack bigger, no don't add the asteroid
                    asteroid = 0

                else:   # if they both collide with the same magnitude, 
                        # top of the stack is gone and don't add the asteroid
                    asteroid = 0
                    stack.pop()
                        
            if asteroid:
                stack.append(asteroid)
            
        return stack
