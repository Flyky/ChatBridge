import sys

from chatbridge.common import constants
from chatbridge.impl.cli import cli_client, cli_server
from chatbridge.impl.discord import entrance as discord


def main():
	if len(sys.argv) == 2:
		arg = sys.argv[1]
		if arg == 'client':
			cli_client.main()
		elif arg == 'server':
			cli_server.main()
		elif arg == 'discordbot':
			discord.main()
		else:
			print('Unknown argument {}'.format(arg))
	else:
		prefix = 'python -m {}'.format(constants.PACKAGE_NAME)
		print('{} client: Start a simple text-chatting-only ChatBridge client'.format(prefix))
		print('{} server: Start the ChatBridge server'.format(prefix))
		print('{} discordbot: Start a Discord bot as client'.format(prefix))


if __name__ == '__main__':
	main()
