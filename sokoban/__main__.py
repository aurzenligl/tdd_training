import sys
from .engine import Engine
from .game import Game
from .level import Level

# the_level = Level((20, 14),
#     '                    '
#     '           %%% %    '
#     '     %%%%%%%   %%   '
#     '    %% % @%% oo %   '
#     '    %    o      %   '
#     '    %  o  %%%   %   '
#     '    %%% %%%%%o%%%   '
#     '    % o  %%% ..%    '
#     '    % o o o ...%    '
#     '    %    %%%...%    '
#     '    % oo % %...%    '
#     '    %  %%% %%%%%    '
#     '    % %%            '
#     '                    '
# )

#Simple level
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

def main(argv=[]):
    engine = Engine()
    game = Game(engine, the_level)
    engine.run()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
