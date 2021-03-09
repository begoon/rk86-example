import click


def read_file(filename: str):
    with open(filename, 'rb') as f:
        binary = f.read()
        return binary


def convert_to_hex(binary, n):
    def hex(line: str):
        return ' '.join(['%02X' % i for i in line])

    lines = [
        ('%04X ' % i) + hex(binary[i : i + n]) for i in range(0, len(binary), n)
    ]
    return lines


@click.command()
@click.option(
    '-i',
    '--input',
    type=str,
    help='input file',
    required=True,
    prompt='input',
)
@click.option(
    '-o',
    '--output',
    type=str,
    help='output file',
    required=True,
    prompt='output',
)
@click.option('-n', '--name', type=str, help='!name tag')
@click.option('-s', '--start', type=str, help='!start tag')
@click.option('-e', '--entry', type=str, help='!entry tag')
@click.option('--verbose', is_flag=True, default=False, help='verbose')
@click.option(
    '-l',
    '--line_length',
    default=16,
    help='number of bytes per line',
)
def main(input, output, name, start, entry, line_length, verbose):
    if verbose:
        print(f'! input={input}')
        print(f'! output={output}')
        print(f'! name={name}')
        print(f'! start={start}')
        print(f'! entry={entry}')
        print(f'! line_length={line_length}')
        print()

    tags = ['#!rk86']
    if name:
        tags.append(f'!name={name}')
    if start:
        tags.append(f'!start={start}')
    if entry:
        tags.append(f'!entry={entry}')
    tags = [' '.join(tags)]

    if verbose:
        print(f'@ tags: {tags}')
        print(f'@ input: {input}')

    image = read_file(input)

    if verbose:
        print(f'# {len(image)} byte(s)')
        print(f'# binary: {image}')

    lines = convert_to_hex(image, line_length)

    if verbose:
        print(f'# parsed: {lines}')

    result = tags + lines

    if verbose:
        print(f'# result: {result}')

    with open(output, 'w') as f:
        if verbose:
            print('\n# output:')
            [print(line) for line in result]
        [print(line, file=f) for line in result]


if __name__ == '__main__':
    main()
