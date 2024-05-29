import argparse

def main():
		parser = argparse.ArgumentParser(description='Example script')
		parser.add_argument('--foo', type=int, help='foo help')
		args = parser.parse_args()
		print(args.foo)

if __name__ == '__main__':
		main()
