# -*- encoding: utf-8 -*-
from fatkernel import LogManager
from fatkernel import ActorContainer

def main():
	logger = LogManager.getLogger('main')
	logger.info('----------------')

	ac = ActorContainer()
	ac.createActor('GlobalStarter')
	ac.run()

if __name__ == '__main__':
	main()

