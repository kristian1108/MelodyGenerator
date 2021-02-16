#!venv/bin/python

import pygame
import argparse
import glob
import random
import os

parser = argparse.ArgumentParser()
parser.add_argument('--midi_dir', type=str, help='The path of the midi file you would like to play. Do not include a slash at the end!')
parser.add_argument('--purge', action='store_true', help='If true, remove all files out of the midi_dir.')
parser.add_argument('--play', action='store_true', help='If true, play a random file out of midi_dir')

if __name__ == '__main__':

    args = parser.parse_args()
    midi_files = glob.glob(f'{args.midi_dir}/*.mid')

    if args.purge:
        for f in midi_files:
            os.remove(f)

    elif args.play:

        file_index = random.randint(0, len(midi_files)-1)

        target_file = midi_files[file_index]

        print(f'\n\nPLAYING FILE {target_file}\n\n')

        pygame.init()
        pygame.mixer.music.load(target_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.wait(1000)
