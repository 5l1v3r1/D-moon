# coding=utf-8
import sys, re
import random

header1 = """
   
    ===========================
    ||                       ||
    ||           =           ||
    ||           =           ||
    ||           =           ||
    ||           =           ||
    ||         =====         ||
    ||           =           ||
    ||                       ||
    |=========================|
              [####] 
              [####]
           -----------%|
   ____________________|__________  
  /  oooooooooooooooo  .o.  oooo /,  
 / ==ooooSh4Rk_0ooooo==.o. ooo= //   @@
/_==__==========__==_ooo__ooo=_/'   {||}
`-----------------------------'     (@@)

       \033[1;91m
┌═════════════════════════════════════════════════════════════════════════════┐
█               Author: @Sh4Rk_0                                              █
█                                                                             █
█                       Site: https://hackingpills.blogspot.com               █
█                                                                             █ 
█                             Copyright (C) 2018 D-Moon @Sh4rk_0              █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m      

    """ 
header2 = """

   

    _____________
   [             ]-
   |             ||
   |             ||
   |             ||
   |             ||
   |             ||
   |          {} ||
   |             ||
   |             ||         
   |             ||---------|
   |             ||BackDoor |
   |_____________|-----------------
  
      
       \033[1;91m
┌═════════════════════════════════════════════════════════════════════════════┐
█               Author: @Sh4Rk_0                                              █
█                                                                             █
█                      Site: https://hackingpills.blogspot.com                █
█                                                                             █ 
█                             Copyright (C) 2018 D-Moon @Sh4rk_0              █
└═════════════════════════════════════════════════════════════════════════════┘   \n \033[1;m 
        """

header3 = """

██████╗  ██████╗  ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝
██████╔╝██║   ██║██    ██╗   ██║
██╔══██╗██║   ██║██    ██╗   ██║
██║  ██║╚██████╔╝╚██████╔╝   ██║
╚═╝  ╚═╝╚══════╝ ╚══════╝════╚═╝══════ >_                                      
   
       \033[1;91m
┌═════════════════════════════════════════════════════════════════════════════┐
█               Author: @Sh4Rk_0                                              █
█                                                                             █
█                      Site: https://hackingpills.blogspot.com                █
█                                                                             █ 
█                             Copyright (C) 2018 D-Moon @Sh4rk_0              █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m    
"""

header4 = '''



@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@              \  /   /\   \  /             @
@     0010      \/   /  \   \/ 1         0001101010010
@ ||             \  /    \  /   0           @
@                 \/      \/        101010000    001010100         
@1010100101   %%& /        \ 101                @
@                /#*      *#\   110001010100    1100    #$#    
@               /   #    #   \              @
@110000     ?!= \   #   #    #   #      ####       1010100
@                \#       # /   @@@@@           
@                 \        /             1011101
@           010    \      /   ==           @1010100
@   *****           \    /                  @
@   1010010     !=   \  /       100100              00100     @
@                     \/            10100       @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 0101010 

      \033[1;91m
┌═════════════════════════════════════════════════════════════════════════════┐
█               Author: @Sh4Rk_0                                              █
█                                                                             █
█                      Site: https://hackingpills.blogspot.com                █
█                                                                             █ 
█                             Copyright (C) 2018 D-Moon @Sh4rk_0              █
└═════════════════════════════════════════════════════════════════════════════┘   \n \033[1;m 
      
'''

header5 = '''

\033[1;91m

         █████████   ██████████
██║     ████████████████████████
██║     ████████████████████████ 
██║     ████████████████████████
██║      ██████████████████████ 
██║       ████████████████████ 
██║        ██████████████████ 
██║         ████████████████
██║          ██████████████
               ██████████
                  ████ \033[1;m 
\033[1;36m
██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗     
██║     ██║████╗  ██║██║   ██║╚██╗██╔╝    
██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝     
██║     ██║██║╚██╗██║██║   ██║ ██╔██╗     
███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗   
╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ \033[1;m
 \033[1;91m
┌═════════════════════════════════════════════════════════════════════════════┐
█               Author: @Sh4Rk_0                                              █
█                                                                             █
█                      Site: https://hackingpills.blogspot.com                █
█                                                                             █ 
█                             Copyright (C) 2018 D-Moon @Sh4rk_0              █
└═════════════════════════════════════════════════════════════════════════════┘   \n \033[1;m 

'''

header6 = '''

  ..:::::::::..     "
                     ..:::aad8888888baa:::..  "
                  .::::d:?88888888888?::8b::::.    "
                .:::d8888:?88888888??a888888b:::.  "
              .:::d8888888a8888888aa8888888888b:::.    "
             ::::dP::::::::88888888888::::::::Yb::::   "
            ::::dP:::::::::Y888888888P:::::::::Yb::::  "
           ::::d8:::::::::::Y8888888P:::::::::::8b:::: "
          .::::88::::::::::::Y88888P::::::::::::88::::.    "
          :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::    "
          :::::::Y88888888888P::|::Y88888888888P:::::::    "
          ::::::::::::::::888:::|:::888::::::::::::::::    "
           :::::::::::::::8888888888888b:::::::::::::: "
           ::::::::::::::888888888888888:::::::::::::: "
            :::::::::::::888888888888888::Sh4Rk_0:::::::  "
             ::::::::::::88::88::88:::88::::::::::::   "
               ::::::::::88::88::88:::88:::::::::: "
                 ::::::::88::88::P::::88::::::::   "
                   ::::::88::88:::::::88:::::: "
                       ::::::::::::::::::: "
                            :::::::::  "
\033[1;91m
┌═════════════════════════════════════════════════════════════════════════════┐
█               Author: @Sh4Rk_0                                              █
█                                                                             █
█                      Site: https://hackingpills.blogspot.com                █
█                                                                             █ 
█                             Copyright (C) 2018 D-Moon @Sh4rk_0              █
└═════════════════════════════════════════════════════════════════════════════┘   \n \033[1;m 

'''


def header():
    headers = [header1, header2, header3,header4,header5,header6]
    print random.choice(headers)


class TerminalController:
    """
    A class that can be used to portably generate formatted output to
    a terminal.  
    
    `TerminalController` defines a set of instance variables whose
    values are initialized to the control sequence necessary to
    perform a given action.  These can be simply included in normal
    output to the terminal:

        >>> term = TerminalController()
        >>> print 'This is '+term.GREEN+'green'+term.NORMAL

    Alternatively, the `render()` method can used, which replaces
    '${action}' with the string required to perform 'action':

        >>> term = TerminalController()
        >>> print term.render('This is ${GREEN}green${NORMAL}')

    If the terminal doesn't support a given action, then the value of
    the corresponding instance variable will be set to ''.  As a
    result, the above code will still work on terminals that do not
    support color, except that their output will not be colored.
    Also, this means that you can test whether the terminal supports a
    given action by simply testing the truth value of the
    corresponding instance variable:

        >>> term = TerminalController()
        >>> if term.CLEAR_SCREEN:
        ...     print 'This terminal supports clearning the screen.'

    Finally, if the width and height of the terminal are known, then
    they will be stored in the `COLS` and `LINES` attributes.
    """
    # Cursor movement:
    BOL = ''             #: Move the cursor to the beginning of the line
    UP = ''              #: Move the cursor up one line
    DOWN = ''            #: Move the cursor down one line
    LEFT = ''            #: Move the cursor left one char
    RIGHT = ''           #: Move the cursor right one char

    # Deletion:
    CLEAR_SCREEN = ''    #: Clear the screen and move to home position
    CLEAR_EOL = ''       #: Clear to the end of the line.
    CLEAR_BOL = ''       #: Clear to the beginning of the line.
    CLEAR_EOS = ''       #: Clear to the end of the screen

    # Output modes:
    BOLD = ''            #: Turn on bold mode
    BLINK = ''           #: Turn on blink mode
    DIM = ''             #: Turn on half-bright mode
    REVERSE = ''         #: Turn on reverse-video mode
    NORMAL = ''          #: Turn off all modes

    # Cursor display:
    HIDE_CURSOR = ''     #: Make the cursor invisible
    SHOW_CURSOR = ''     #: Make the cursor visible

    # Terminal size:
    COLS = None          #: Width of the terminal (None for unknown)
    LINES = None         #: Height of the terminal (None for unknown)

    # Foreground colors:
    BLACK = BLUE = GREEN = CYAN = RED = MAGENTA = YELLOW = WHITE = ''
    
    # Background colors:
    BG_BLACK = BG_BLUE = BG_GREEN = BG_CYAN = ''
    BG_RED = BG_MAGENTA = BG_YELLOW = BG_WHITE = ''
    
    _STRING_CAPABILITIES = """
    BOL=cr UP=cuu1 DOWN=cud1 LEFT=cub1 RIGHT=cuf1
    CLEAR_SCREEN=clear CLEAR_EOL=el CLEAR_BOL=el1 CLEAR_EOS=ed BOLD=bold
    BLINK=blink DIM=dim REVERSE=rev UNDERLINE=smul NORMAL=sgr0
    HIDE_CURSOR=cinvis SHOW_CURSOR=cnorm""".split()
    _COLORS = """BLACK BLUE GREEN CYAN RED MAGENTA YELLOW WHITE""".split()

    def __init__(self, term_stream=sys.stdout):
        """
        Create a `TerminalController` and initialize its attributes
        with appropriate values for the current terminal.
        `term_stream` is the stream that will be used for terminal
        output; if this stream is not a tty, then the terminal is
        assumed to be a dumb terminal (i.e., have no capabilities).
        """
        # Curses isn't available on all platforms
        try: import curses
        except: return

        # If the stream isn't a tty, then assume it has no capabilities.
        if not term_stream.isatty(): return

        # Check the terminal type.  If we fail, then assume that the
        # terminal has no capabilities.
        try: curses.setupterm()
        except: return

        # Look up numeric capabilities.
        self.COLS = curses.tigetnum('cols')
        self.LINES = curses.tigetnum('lines')
        
        # Look up string capabilities.
        for capability in self._STRING_CAPABILITIES:
            (attrib, cap_name) = capability.split('=')
            setattr(self, attrib, self._tigetstr(cap_name) or '')

        # Colors
        set_fg = self._tigetstr('setf')
        if set_fg:
            for i,color in zip(range(len(self._COLORS)), self._COLORS):
                setattr(self, color, curses.tparm(set_fg, i) or '')
        set_bg = self._tigetstr('setb')
        if set_bg:
            for i,color in zip(range(len(self._COLORS)), self._COLORS):
                setattr(self, 'BG_'+color, curses.tparm(set_bg, i) or '')

    def _tigetstr(self, cap_name):
        # String capabilities can include "delays" of the form "$<2>".
        # For any modern terminal, we should be able to just ignore
        # these, so strip them out.
        import curses
        cap = curses.tigetstr(cap_name) or ''
        return re.sub(r'\$<\d+>[/*]?', '', cap)

    def render(self, template):
        """
        Replace each $-substitutions in the given template string with
        the corresponding terminal control string (if it's defined) or
        '' (if it's not).
        """
        return re.sub(r'\$\$|\${\w+}', self._render_sub, template)

    def _render_sub(self, match):
        s = match.group()
        if s == '$$': return s
        else: return getattr(self, s[2:-1])
