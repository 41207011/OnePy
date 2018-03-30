from OnePy.environment import Environment
from OnePy.sys_model.signals import Signal


class SignalGenerator(object):

    """存储Signal的信息"""
    env = Environment()

    def __init__(self, order_type):
        self.order_type = order_type

    def func_1(self, size, ticker,
               takeprofit=None, takeprofit_pct=None,
               stoploss=None, stoploss_pct=None,
               trailingstop=None, trailingstop_pct=None,
               price=None, price_pct=None):

        return Signal(
            order_type=self.order_type,
            size=size,
            ticker=ticker,
            takeprofit=takeprofit,
            takeprofit_pct=takeprofit_pct,
            stoploss=stoploss,
            stoploss_pct=stoploss_pct,
            trailingstop=trailingstop,
            trailingstop_pct=trailingstop_pct,
            price=price,
            price_pct=price_pct,
        )

    def func_2(self, size, ticker, price=None, price_pct=None):

        return Signal(
            order_type=self.order_type,
            size=size,
            ticker=ticker,
            price=price,
            price_pct=price_pct,
        )
