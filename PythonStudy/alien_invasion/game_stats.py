import json


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #游戏刚启动时处于非活动状态
        self.game_active = False
        #最高分，不重置，所以不放在reset_stats()
        filename = 'HighScore.json'
        with open(filename) as f_obj:
            self.high_score = json.load(f_obj)
        self.level = 1

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
