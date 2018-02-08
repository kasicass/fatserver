# -*- encoding: utf-8 -*-
from fatkernel import Actor
from fatkernel import LogManager
from fatkernel.interface import IStartup

class GlobalStarter(Actor, IStartup):
	def __init__(self, args):
		super(GlobalStarter, self).__init__(args)
		self.logger = LogManager.getLogger(self.__class__.__name__)

	def applicationStartup(self):
		self.logger.info('applicationStartup, %d', 10)
		self.createRepeatTimer(self.makeSomeLog, 1, 10)

	def applicationShutdown(self):
		self.logger.info('applicationShutdown, %d', 10)

	def makeSomeLog(self, handle):
		self.logger.info('hello logger')

