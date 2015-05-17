__author__ = 'Gregory'
import  random
programsToWriteList = ["Name Generator",
                       "Higher/Lower | Heads/Tails",
                       "Temperature Converter",
                       "Calculate age in Seconds",
                       "Encrypt/Decrypt Algorithm",
                       "FizzBuzz",
                       "Rock paper scissors",
                       "Hangman",
                       "Love calculator",
                       "Pseudorandom Sentence Generator",
                       "Password Generator",
                       "Atomically correct time from an internet clock",
                       "Haiku Generator",
                       "Magic Eight Ball",
                       "Collatz Conjecture",
                       "Reverse a string",
                       "Simple file explorer",
                       "Count words in a string",
                       "Minesweeper",
                       "Connect four",
                       "BMI Calculator",
                       "4chan thread downloader/images",
                       "Sudoku Generator/Solver",
                       "Maze generator/solver",
                       "Decimal/Binary converter",
                       "Picross solver",
                       "Eulerian Path",
                       "Fibonnaci Sequence",
                       "Calculate and pring 100 Factorial",
                       "Create a cipher encrypt/decrypt tool",
                       "Blackjack",
                       "Dungeons and dragons w/ AI",
                       "Generate ASCII height based on input",
                       "Use Genetic Algorithm on Polygons",
                       "Benford's Law",
                       "Currency Converter",
                       "static website generator",
                       "crossword game",
                       "scientific calculator",
                       "perlin noise algorithm",
                       "image viewer",
                       "ascii digital clock",
                       "dijkstra's algorithm",
                       "text/morse translator",
                       "tic-tac-toe",
                       "snake game",
                       "FTP client",
                       "telnet server",
                       "IMP interpreter",
                       "Tetris",
                       "Conways game of life",
                       "web crawler",
                       "text editor",
                       "RSS Feed Creator",
                       "evaluate binomial coefficients",
                       "RPN calculator",
                       "mandlebrot set",
                       "sorting algorithm",
                       "Convert markup -> HTML",
                       "N Queens problem",
                       "credential validator (exmp. phone # email addr)",
                       "linked list",
                       "mastermind",
                       "Random image generator",
                       "Ulam spiral",
                       "Klingon Translator",
                       "prime number generator using a sieve",
                       "markov chain",
                       "graphical analog clock + gui",
                       "2 separate languages send strings to one another",
                       "triangle number calculator",
                       "calculating typing speed",
                       "name in ascii art",
                       "towers of hanoi",
                       "quine",
                       "IRC bot",
                       "brainfuck interpreter",
                       "visualization of #7 Bonus: add sound",
                       "chip-8 emulator",
                       "geekcode generator",
                       "define, translate, and rotate a polygon",
                       "pong w/ variable vectors",
                       "battleships with AI",
                       "simple paint program",
                       "TCP chat w/ basic encryption (XOR)",
                       "incremental economy simulator (Time of exploration)",
                       "encrypt/decrypt text into an image",
                       "pascal's triagle",
                       "sine wave generator from Psudorandom numbers",
                       "Basic HTML web browser",
                       "flappy bird",
                       "fast fourier transform",
                       "method ringing simulator",
                       "binary search",
                       "nintendo oil panic",
                       "sierpinski triangle generator",
                       "calculate dot-&-cross of two vectors",
                       "little man computer simulator",
                       "basic LISP interpreter",
                       "Enigma Machine simulator with settings.conf"]
print(programsToWriteList[random.randint(0, 99)])

stringManipulationInterpreters = [9, 10, 12, 15, 17, 52, 60, 65, 72, 74, 76, 78, 79, 98, 99]
mathAndCS = [3, 4, 5, 11, 14, 20,
             23, 25, 26, 27, 28, 29, 32, 33, 34, 38, 39, 42,
             48, 54, 55, 56, 57, 59, 61, 63, 64, 66, 67, 69, 70, 77, 80, 86, 87, 88, 91, 92, 93, 95, 96, 97]
games = [6, 7, 13, 18, 19, 22, 30, 31, 37, 44, 45, 49, 50, 62, 73, 81, 82, 85, 90, 94]
converters = [2, 24, 35, 43, 58]
misc = [16, 40, 41, 68, 71, 83]

problemSelection = int(raw_input ("What are you interested in working on? String manipulation/Interpreters (1), Math and CS? (2), Games (3), "
       "Converters? (4), Or, Misc (5)?"))
print (problemSelection)
if problemSelection == 1:
    print(programsToWriteList[stringManipulationInterpreters[random.randint(0, len(stringManipulationInterpreters))]])
elif problemSelection == 2:
    print(programsToWriteList[games[random.randint(0, len(games))]])
elif problemSelection == 3:
    print(programsToWriteList[converters[random.randint(0, len(converters))]])
elif problemSelection == 4:
    print(programsToWriteList[misc[random.randint(0, len(misc))]])
else:
    print ("Please print a number within the ones specified.")



