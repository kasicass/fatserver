# -*- encoding: utf-8 -*-
from fatkernel import Actor
from fatkernel.interface import IStartup

class GlobalStarter(Actor, IStartup):
	def __init__(self, args):
		super(GlobalStarter, self).__init__(args)

	def applicationStartup(self):
		print '[Starter] applicationStartup'
		self.createRepeatTimer(self.makeSomeLog, 1, 10)

	def applicationShutdown(self):
		print '[Starter] applicationShutdown'

	def makeSomeLog(self, handle):
		self.logger.info('hello logger')

