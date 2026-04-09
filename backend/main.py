def main(input_data):
	stdin = input_data['stdin']
	a, b = map(int, stdin.split())
	return {'stdout': str(a + b)}
