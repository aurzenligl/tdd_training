import sys
import argparse

from .engine import Engine
from .game import Game
from .level import Level

the_level = Level((20, 14),
    '                    '
    '           %%% %    '
    '     %%%%%%%   %%   '
    '    %% % @%%    %   '
    '    %           %   '
    '    %     %%%   %   '
    '    %%% %%%%%o%%%   '
    '    %    %%%   %    '
    '    %      o   %    '
    '    %    %%%   %    '
    '    %    % % ..%    '
    '    %  %%% %%%%%    '
    '    % %%            '
    '                    '
)


the_level2 = Level((20, 14),
    '                    '
    '           %%% %    '
    '     %%%%%%% @ %%   '
    '    %% %  %%    %   '
    '    %           %   '
    '    %     %%%   %   '
    '    %%% %%%%%o%%%   '
    '    %    %%% . %    '
    '    %          %    '
    '    %    %%%   %    '
    '    %    % %   %    '
    '    %  %%% %%%%%    '
    '    % %%            '
    '                    '
)

the_level_demo = Level((20, 14),
    '                    '
    '           %%% %    '
    '     %%%%%%%   %%   '
    '    %% %  %% @  %   '
    '    %        o  %   '
    '    %     %%%   %   '
    '    %%% %%%%% %%%   '
    '    %    %%% .%     '
    '    %   o   . %     '
    '    %    %%%%%%     '
    '    %    %          '
    '    %  %%%          '
    '    % %%            '
    '                    '
)

def main(argv=[]):
    demo_solver = True
    engine = Engine()
    if demo_solver:
        game = Game(engine, the_level_demo)
        engine.demo_solver()
    else:    
        engine.run()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
