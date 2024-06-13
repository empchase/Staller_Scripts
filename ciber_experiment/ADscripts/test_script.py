import argparse


# set up main code to be run
def main(input_file, output_file):
    # Read first line of the input file
    with open(input_file, 'r') as f_in:
        firstline = f_in.readline()


    # write the first line to the output file
    with open(output_file, 'w') as f_out:
        f_out.write(firstline)






if __name__ == "__main__":
    # Check if the script is being run as the main program

    # Create ArgumentParser object with a description
    parser = argparse.ArgumentParser(description='Test script for Makefile')

    # Add arguments to the parser
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file path')
    # Add an argument for the input file path. -i or --input specifies the argument name.
    # It's required (required=True), of type string (type=str), and has a help message.

    parser.add_argument('-o', '--output', type=str, required=True, help='Raw data output file path')
    # Add an argument for the output file path. -o or --output specifies the argument name.
    # It's required (required=True), of type string (type=str), and has a help message.

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args.input, args.output)