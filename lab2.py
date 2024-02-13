import sys
def print_args():
    script_name = sys.argv[0]
    variables = sys.argv[1:]
    print("Script name: " + script_name)
    print("Variables: " + str(variables))

def helloWorld():
	print("Hello World")


helloWorld()
