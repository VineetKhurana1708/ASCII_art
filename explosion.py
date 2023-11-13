import curses
import random
import math
import time

NUM_FRAMES = 150
NUM_BLOBS = 800
PERSPECTIVE = 50.0

frames = [

"""
   .
                                  
                                  
                                                 
                                
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  
                                  
                                                 
                              \\ ~ //
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 

"""
   .
                                  
                                  
                              \\ ~ //                   
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  
                               \\ ~ //
                                / /                   
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """,

"""
   .
                                  ._//
                                 / _~
                                / / \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  ._._//
                                 / _._~
                                / /   \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  ._._._//
                                 / _._._~
                                / /     \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  ._._._._//
                                 / _._._._~
                                / /       \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  ._._._._._//
                                 / _._._._._~
                                / /         \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  ._._._._._._//
                                 / _._._._._._~
                                / /           \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  ._._._._._._._//
                                 / _._._._._._._~
                                / /             \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  ._._._._._._._._//
                                 / _._._._._._._._~
                                / /               \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  ._._._._._._._._._//
                                 / _._._._._._._._._~
                                / /                 \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
"""
   .
                                  ._._._._._._._._._._//
                                 / _._._._._._._._._._~
                                / /                   \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """,
 """
   .
                                  ._._._._._._._._._._._//
                                 / _._._._._._._._._._._~
                                / /                     \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, """
   .
                                  ._._._._._._._._._._._._//
                                 / _._._._._._._._._._._._~
                                / /                       \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, """
   .
                                  ._._._._._._._._._._._._._//
                                 / _._._._._._._._._._._._._~
                                / /                         \\
                                | |
            CCCCCCCCCCCCC   SSSSSSSSSSSSSSS LLLLLLLLLLL             
         CCC::::::::::::C SS:::::::::::::::SL:::::::::L             
       CC:::::::::::::::CS:::::SSSSSS::::::SL:::::::::L             
      C:::::CCCCCCCC::::CS:::::S     SSSSSSSLL:::::::LL             
     C:::::C       CCCCCCS:::::S              L:::::L               
    C:::::C              S:::::S              L:::::L               
    C:::::C               S::::SSSS           L:::::L               
    C:::::C                SS::::::SSSSS      L:::::L               
    C:::::C                  SSS::::::::SS    L:::::L               
    C:::::C                     SSSSSS::::S   L:::::L               
    C:::::C                          S:::::S  L:::::L               
     C:::::C       CCCCCC            S:::::S  L:::::L         LLLLLL
      C:::::CCCCCCCC::::CSSSSSSS     S:::::SLL:::::::LLLLLLLLL:::::L
       CC:::::::::::::::CS::::::SSSSSS:::::SL::::::::::::::::::::::L
         CCC::::::::::::CS:::::::::::::::SS L::::::::::::::::::::::L
            CCCCCCCCCCCCC SSSSSSSSSSSSSSS   LLLLLLLLLLLLLLLLLLLLLLLL

    """, 
]



class SpaceBlob:
    def __init__(self):
        bx = random.uniform(-1, 1)
        by = random.uniform(-1, 1)
        bz = random.uniform(-1, 1)
        br = math.sqrt(bx**2 + by**2 + bz**2)
        self.x = (bx / br) * (1.3 + 0.2 * random.uniform(-1, 1))
        self.y = (0.5 * by / br) * (1.3 + 0.2 * random.uniform(-1, 1))
        self.z = (bz / br) * (1.3 + 0.2 * random.uniform(-1, 1))


def prng():
    return random.uniform(-1, 1)


def generate_frame(i, blobs, minx, maxx, miny, maxy, cols, rows):

    i_post = i - len(frames)
    if i < len(frames): 
        csl_frame = frames[len(frames) -i -1]
    else:
        csl_frame = frames[0]


    # Calculate centering positions
    csl_frame_lines = csl_frame.strip().split("\n")
    csl_frame_height = len(csl_frame_lines)
    csl_frame_width = max(len(line) for line in csl_frame_lines)

    start_row = max((rows - csl_frame_height) // 2, 0)
    start_col = max((cols - csl_frame_width) // 2, 0)

    frame = [[" " for _ in range(cols)] for _ in range(rows)]

    # Overlay the csl_frame onto the initial frame_with_csl
    for idx, line in enumerate(csl_frame_lines):
        frame_with_csl_row = start_row + idx
        if 0 <= frame_with_csl_row < rows:  # Check row is within terminal height
            for jdx, char in enumerate(line):
                frame_with_csl_col = start_col + jdx
                if 0 <= frame_with_csl_col < cols:  # Check col is within terminal width
                    frame[frame_with_csl_row][frame_with_csl_col] = char

   ###CSL FRAME manipulation ends here 
   #####
    if i_post >=0 : 
        for y in range(rows):
            for x in range(cols):
                screen_x = x + minx  # translate to screen coordinates
                screen_y = y + miny
                if i_post == 0:
                    #char = '.' if screen_x == 0 and screen_y == 0 else ' '
                    if screen_x == 0 and screen_y == 0 :
                        char = '.'
                    else : 
                        char = frame[y][x] 
                elif i_post < 1:
                    r = math.sqrt(screen_x**2 + 4 * screen_y**2)
                    if r < i_post * 2 : 
                        char = 'o'
                    else : 
                        char = frame[y][x] 
                else:
                    r = math.sqrt(screen_x**2 + 4 * screen_y**2) * (0.5 + (prng() / 3.0) * math.cos(16 * math.atan2(screen_y * 2 + 0.01, screen_x + 0.01)) * 0.3)
                    v = int(i_post - r)  # Convert to int to use as a string index
                    if v < 0:
                        char = frame[y][x] 
                        #char = "%@W#H=+~-:."[i - 8] if i < 19 else ' '
                    elif v < 20:
                        #char = " .:!HIOMW#%$&@08O=+-"[v]  # Access using integer index
                        char = " .:!CCCCSSSSLLLLL|+-"[v]  # Access using integer index
                    else:
                        char = frame[y][x] 
                if 0 <= y < rows and 0 <= x < cols:
                    frame[y][x] = char

        # Add blobs with perspective effect after the first few frames
        if i_post > 2:
            for blob in blobs:
                bx = blob.x * (i_post - 6)
                by = blob.y * (i_post - 6)
                bz = blob.z * (i_post - 6)
                if bz < 5 - PERSPECTIVE or bz > PERSPECTIVE:
                    continue
                screen_x = int((cols // 2) + bx * PERSPECTIVE / (bz + PERSPECTIVE))
                screen_y = int((rows // 2) + by * PERSPECTIVE / (bz + PERSPECTIVE))
                if 0 <= screen_x < cols and 0 <= screen_y < rows:
                    #char = '.' if bz > 40 else 'o' if bz > -20 else '@'
                    char = '.' if bz > 40 else '*' if bz > -20 else '@'
                    frame[screen_y][screen_x] = char

    return [''.join(row) for row in frame]


def play_animation(stdscr, frames):
    num_rows, num_cols = stdscr.getmaxyx()  # Get the max rows and columns

    frame_number = 0
    for frame in frames:
        stdscr.erase()

        #stdscr.addstr(-1, 0, "Frame: " + str(frame_number))  # Display at the top-left corner
        #frame_number += 0
        for y, row in enumerate(frame):
            if y < num_rows - 1:  # -1 to avoid writing to the bottom edge
                trimmed_row = row[:num_cols - 1]  # Trim row to fit window width
                stdscr.addstr(y, 0, trimmed_row)
        stdscr.refresh()
        time.sleep(0.06)  # Delay to create the animation speed


def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    rows, cols = stdscr.getmaxyx()
    minx, maxx = -cols // 2, cols // 2
    miny, maxy = -rows // 2, rows // 2

    # Generate blobs
    blobs = [SpaceBlob() for _ in range(NUM_BLOBS)]

    # Precompute all frames
    frames = [generate_frame(i, blobs, minx, maxx, miny, maxy, cols, rows) for i in range(NUM_FRAMES)]

    # Play back the frames in sequence
    play_animation(stdscr, frames)

    # Wait for user input to exit
    stdscr.getch()


# Run the curses application
curses.wrapper(main)
