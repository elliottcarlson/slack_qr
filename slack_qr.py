#!/bin/env python
import argparse
import qrcode

def emojify(emoji):
    if not emoji.startswith(':'):
        emoji = f':{emoji}'
    if not emoji.endswith(':'):
        emoji = f'{emoji}:'
    return emoji

def qr(light_emoji, dark_emoji, text, border):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )
    qr.add_data(text)
    qr.make()

    emoji = [
        emojify(light_emoji),
        emojify(dark_emoji)
    ]

    output = []
    length = 0
    if border: output.append([emoji[0] * (qr.modules_count + 2)])
    for r in range(qr.modules_count):
        line = [emoji[0]] if border else []
        for c in range(qr.modules_count):
            line.append(emoji[1 if qr.modules[r][c] else 0])
        if border: line.append(emoji[0])
        length = length + sum([len(i) for i in line])
        output.append(line)
    if border:
        output.append([emoji[0] * (qr.modules_count + 2)])
        length = length + (len(emoji[0]) * (qr.modules_count +2))

    if length > 12000:
        print('Warning: Output is longer than 12,000 characters and will not be pastable in Slack.')
        print('         Create aliases of the emoji you want to use to make the message shorter.')
    else:
        print('\n'.join([''.join(i) for i in output]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--light', help='Light emoji', dest='light', action='store', default='white_square')
    parser.add_argument('-d', '--dark', help='Dark emoji', dest='dark', action='store', default='black_square')
    parser.add_argument('-b', '--border', action='store_true', default=False)
    parser.add_argument('text', nargs='*')
    args = parser.parse_args()

    qr(args.light, args.dark, ' '.join(args.text), args.border)

